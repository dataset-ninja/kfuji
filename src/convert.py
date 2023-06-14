import os
import xml.etree.ElementTree as ET

import supervisely as sly
from supervisely.io.fs import file_exists, get_file_name


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/home/alex/DATASETS/TODO/KFuji/KFuji_RGB-DS_dataset/preprocessed data"
    images_folder_name = "images"
    anns_folder = "square_annotations1"
    images_ext = "hr.jpg"
    bbox_ext = ".xml"
    ds_split = "sets"
    batch_size = 30

    def create_ann(image_name):
        labels = []

        image_path = os.path.join(images_folder, image_name + images_ext)
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        bbox_path = os.path.join(anns_path, image_name + bbox_ext)

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

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    obj_class = sly.ObjClass("apple", sly.Rectangle)

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=[obj_class])
    api.project.update_meta(project.id, meta.to_json())

    ds_splits_folder = os.path.join(dataset_path, ds_split)
    images_folder = os.path.join(dataset_path, images_folder_name)
    anns_path = os.path.join(dataset_path, anns_folder)

    for ds_split_file in os.listdir(ds_splits_folder):
        ds_name = get_file_name(ds_split_file)
        if ds_name not in ["train", "val", "test"]:
            continue
        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)
        with open(os.path.join(ds_splits_folder, ds_split_file)) as f:
            content = f.read().split("\n")

            images_names = [item for item in content if len(item) != 0]

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for img_names_batch in sly.batched(images_names, batch_size=batch_size):
                img_pathes_batch = [
                    os.path.join(images_folder, im_name + images_ext) for im_name in img_names_batch
                ]

                img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_name) for image_name in img_names_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(img_names_batch))

    return project
