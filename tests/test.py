from core.put_template import Template


def test_put_template(temp: Template):
    """
    Успешное добавление шаблона
    :return:
    """
    files = {'file': open('../data/1.yml', 'rb')}
    data = {"tmpl_id": "my_custom_id"}
    response = temp.put_template(files=files, data=data)
    assert response.status_code == 201, 'На запрос добавления темплейта сервис ответил некорректно'
    templ_id_lst = response.json()['message'].split('=')
    templ_id = templ_id_lst[1]
    templ = Template()
    temp_lst = templ.get_template_lst().json()['templates']
    assert templ_id in temp_lst, 'Добавленный шаблон отсутствует в системе'


def test_get_all_templates(templates, temp: Template):
    """
    Успешное получение списка всех шаблонов
    :return:
    """
    response = temp.get_template_lst()
    assert response.status_code == 200, 'На запрос добавления темплейта сервис ответил некорректно'
    templ_lst = response.json()['templates']
    compare = set(templates).issubset(templ_lst)
    assert compare, 'В списке шаблонов отсутствуют ожидаемые шаблоны'


def test_delete_template_by_id(teml_for_del, temp: Template):
    """
    Успешное удаление шаблона по его id
    :return:
    """
    response = temp.delete_template(teml_for_del)
    assert response.status_code == 200
    temp_lst = temp.get_template_lst()
    assert teml_for_del not in temp_lst.json()['templates']
