Please visit dataset [homepage](https://zenodo.org/record/3715991#.YguSZnVBzmg) to download the data. 

Afterward, you have the option to download it in the universal supervisely format by utilizing the *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='KFuji RGB-DS', dst_path='~/dtools/datasets/KFuji RGB-DS.tar')
```
