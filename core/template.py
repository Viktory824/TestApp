import requests


class Template:
    host = 'http://localhost:5000'
    url = '/api/v1/templates'

    def put_template(self, files, data=None):
        return requests.put(url=f'{self.host}{self.url}', files=files, data=data, verify=False)

    def get_template_lst(self):
        return requests.get(url=f'{self.host}{self.url}')

    def delete_template(self, temp_id):
        return requests.delete(url=f'{self.host}{self.url}/{temp_id}')
