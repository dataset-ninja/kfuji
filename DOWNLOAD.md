Dataset **KFuji RGB-DS** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/k/G/HP/ns3PRDIssQTlkJKxl82hhvWTYEoofDpYJajWUFgNIJKTox605Y4J06fQMSm8s1C7FL74YR9ZkHJVUpepVGpTtMtY26prcUU7YQwGqDWG0BtFFJIko9bbPlJhXXoU.tar)

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
