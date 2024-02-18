import os

from pcloud import PyCloud


def upload_message(file):
    pc = PyCloud(os.environ.get('PCLOUD_EMAIL'),
                 os.environ.get('PCLOUD_PASSWORD'),
                 endpoint="eapi")
    pc.uploadfile(files=[file], path=os.environ.get('PCLOUD_PATH'))
