Dataset **KFuji RGB-DS** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/uf4qcpdy5p97pxip01qxw/kfuji-rgbds-DatasetNinja.tar?rlkey=d1yi2hsvo5eh2b3x1w89n6oyx&dl=1)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='KFuji RGB-DS', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [KFuji_RGB-DS_dataset.zip](https://zenodo.org/record/3715991/files/KFuji_RGB-DS_dataset.zip?download=1)
- [LICENSE.txt](https://zenodo.org/record/3715991/files/LICENSE.txt?download=1)
- [README.txt](https://zenodo.org/record/3715991/files/README.txt?download=1)
