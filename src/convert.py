# https://zenodo.org/record/3715991#.YguSZnVBzmg

import os
import xml.etree.ElementTree as ET

import cv2
import numpy as np
import scipy.io
import supervisely as sly
from dotenv import load_dotenv
from supervisely.io.fs import (
    dir_exists,
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    mkdir,
    remove_dir,
)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # project_name = "KFuji"
    ds_path = "/home/grokhi/rawdata/kfuji"
    dataset_path = "/home/grokhi/rawdata/kfuji/preprocessed data"
    original_data_path = "/home/grokhi/rawdata/kfuji/row data"
    images_folder_name = "images"
    anns_folder = "square_annotations1"
    images_ext = "hr.jpg"
    full_images_ext = "RGBhr.jpg"
    mat_ext = "DS.mat"
    depth_ext = "d.png"
    ir_ext = "ir.png"
    bbox_ext = ".xml"
    ds_split = "sets"
    batch_size = 30
    group_tag_name = "im_id"

    def create_ann(image_path):
        labels = []

        id_data = get_file_name_with_ext(image_path)[:-10]
        group_id = sly.Tag(group_tag_meta, value=id_data)

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        bbox_path = os.path.join(anns_path, get_file_name_with_ext(image_path[:-6]) + bbox_ext)

        if file_exists(bbox_path):
            tree = ET.parse(bbox_path)
            root = tree.getroot()

            coords_xml = root.findall(".//bbox")
            for curr_coord in coords_xml:
                left = int(curr_coord[0].text)
                top = int(curr_coord[1].text)
                right = int(curr_coord[2].text)
                bottom = int(curr_coord[3].text)

                rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
                label = sly.Label(rect, obj_class)
                labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[group_id])

    obj_class = sly.ObjClass("apple", sly.Rectangle)

    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class], tag_metas=[group_tag_meta])
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    ds_splits_folder = os.path.join(dataset_path, ds_split)
    images_folder = os.path.join(dataset_path, images_folder_name)
    anns_path = os.path.join(dataset_path, anns_folder)

    for ds_split_file in os.listdir(ds_splits_folder):
        ds_name = get_file_name(ds_split_file)
        if ds_name not in ["train", "val", "test"]:
            continue
        dataset = api.dataset.create(project.id, "cropped-" + ds_name, change_name_if_conflict=True)
        with open(os.path.join(ds_splits_folder, ds_split_file)) as f:
            content = f.read().split("\n")

            images_names = [item for item in content if len(item) != 0]

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                img_pathes_batch = []
                images_names_batch = []
                for im_name in img_names_batch:
                    image_name = im_name + images_ext
                    images_names_batch.append(image_name)
                    im_path = os.path.join(dataset_path, images_folder, image_name)
                    img_pathes_batch.append(im_path)
                    # TODO ======================================================================================
                    temp_folder = os.path.join(ds_path, "temp")
                    mkdir(temp_folder)
                    mat_path = im_path.replace(full_images_ext, mat_ext)
                    mat = scipy.io.loadmat(mat_path)

                    depth_im_np = mat["NIR_DEPTH_res_crop"][:, :, 0]
                    ir_im_np = mat["NIR_DEPTH_res_crop"][:, :, 1]

                    depth_path = os.path.join(
                        temp_folder,
                        get_file_name_with_ext(im_path).replace(full_images_ext, depth_ext),
                    )
                    cv2.imwrite(depth_path, depth_im_np)
                    images_names_batch.append(get_file_name_with_ext(depth_path))
                    img_pathes_batch.append(depth_path)

                    ir_path = os.path.join(
                        temp_folder,
                        get_file_name_with_ext(im_path).replace(full_images_ext, ir_ext),
                    )
                    cv2.imwrite(ir_path, ir_im_np)
                    images_names_batch.append(get_file_name_with_ext(ir_path))
                    img_pathes_batch.append(ir_path)

                    # TODO =======================================================================================

                img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = []
                for i in range(0, len(img_pathes_batch), 3):
                    ann = create_ann(img_pathes_batch[i])
                    anns.extend([ann, ann, ann])
                api.annotation.upload_anns(img_ids, anns)
                remove_dir(temp_folder)

                progress.iters_done_report(len(img_names_batch))

    # ==================ORIGINAL DATA===========================================================
    ds_name = "original_images"
    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = [
        im_name for im_name in os.listdir(original_data_path) if get_file_ext(im_name) == ".jpg"
    ]

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(original_data_path, im_name) for im_name in img_names_batch
        ]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)

        progress.iters_done_report(len(img_names_batch))
    return project
