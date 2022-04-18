import requests
import os
#password admin is 'I1Rc,#4b/a'


def upload_video(video_id: str):
    print('Начата загрузка файлов на хостинг, подождите...')
    headers = {"X-Auth-User": "160387", "X-Auth-Key": "I1Rc,#4b/a"}
    r = requests.get("https://api.selcdn.ru/auth/v1.0", headers=headers)

    auth_token = r.headers.get("X-Auth-Token")
    storage_url = r.headers.get("X-Storage-Url")

    file = open('./output/' + video_id + '.tar', 'rb')
    header_token = {"X-Auth-Token": auth_token}

    container_name = '/videos/' + video_id + '/?extract-archive=tar'

    r_containers = requests.put(
        storage_url + container_name,
        headers=header_token,
        data=file
    )

    print('Урок № ' + video_id + ' успешно загружен на хостинг Selectel!')
