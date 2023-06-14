**KFuji RGB-DS** is a dataset for instance segmentation tasks. It is used in the agriculture industry.

The dataset consists of 967 images with 13835 labeled objects belonging to 1 single class (*apple*).

Each image in the KFuji RGB-DS dataset has pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 3 splits in the dataset: *test* (193 images), *train* (619 images), and *val* (155 images). The dataset was released in 2020.

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/kfuji/raw/main/visualizations/horizontal_grid.png">
