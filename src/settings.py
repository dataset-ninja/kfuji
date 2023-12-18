from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "KFuji RGB-DS"
PROJECT_NAME_FULL: Optional[
    str
] = "KFuji RGB-DS Database: Fuji Apple Multi-Modal Images for Fruit Detection with Color, Depth and Range-Corrected IR Data"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_SA_4_0(
    source_url="https://zenodo.org/records/3715991#.YguSZnVBzmg"
)
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Agricultural()]
CATEGORY: Category = Category.Agriculture()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection(), CVTask.MonocularDepthEstimation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2020-05-11"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/3715991#.YguSZnVBzmg"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 11602885
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/kfuji"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "KFuji_RGB-DS_dataset.zip": "https://zenodo.org/record/3715991/files/KFuji_RGB-DS_dataset.zip?download=1",
    "LICENSE.txt": "https://zenodo.org/record/3715991/files/LICENSE.txt?download=1",
    "README.txt": "https://zenodo.org/record/3715991/files/README.txt?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://www.sciencedirect.com/science/article/pii/S2352340919306432?via%3Dihub"

CITATION_URL: Optional[str] = "https://zenodo.org/record/3715991/export/hx"

AUTHORS: Optional[List[str]] = [
    "Jordi Gené-Mola",
    "Verónica Vilaplana",
    "Joan R. Rosell-Polo",
    "Josep-Ramon Morros",
    "Javier Ruiz-Hidalgo",
    "Eduard Gregorio",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["gregorio@eagrof.udl.cat"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Universitat de Lleida, Spain",
    "Universitat Politècnica de Catalunya, Spain",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://www.udl.cat/",
    "https://www.upc.edu/ca",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "__PRETEXT__": "Additionally, every channel of the image is grouped by its ***im_id***. Explore image groups in supervisely."
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
