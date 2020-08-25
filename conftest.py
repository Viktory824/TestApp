import os
import yaml

import requests
from pytest import fixture

from core.put_template import Template


@fixture(scope='function', name='temp')
def template_info():
    return Template()


@fixture(scope='function', name='templates')
def add_templates(temp: Template):
    files_lst = os.listdir('../data')
    for file in files_lst:
        files = {'file': open(f'../data/{file}', 'rb')}
        requests.put(url=f'{temp.host}{temp.url}', )
        temp.put_template(files=files, data={'tmpl_id': file})
    return files_lst


@fixture(scope='function', name='teml_for_del')
def add_template_for_del(temp: Template):
    file = open(f'../data/4.yml', 'rb')
    id_ = yaml.load(file)['id']
    files = {'file': file}
    requests.put(url=f'{temp.host}{temp.url}', files=files, data={'tmpl_id': id_})
    return id_
