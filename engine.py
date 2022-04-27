import json

import requests
import os
import html2text
url = 'https://<yourSite>.clients.site/api/get-posts?bizId=<bizId>&limit=556&offset=0'
headers = { 'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': '<yourCookie>',
            'Host': '<yourSite>.clients.site',
            'Pragma': 'no-cache',
            'Referer': 'https://<yourSite>.clients.site/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'}



def main():
    response = requests.get(url, headers=headers)
    data = response.json()
    with open('Save_auto1.json', 'a',
              encoding='UTF-8') as file:  # Открываем файл Save_auto1.txt (создаётся автоматически), на дозапись (ключ a)
        file.write(str(data))
    results = data['result']
    parent_dir = "D:/Programming/YandexSiteParser/posts" #edit your parent dir
    for item in results:
        current = str(results.index(item))
        path = os.path.join(parent_dir, current)
        try:
            os.mkdir(path)
            print(f'Создана папка {path}')
        except:
            print(f'Папка {path} уже существует')
        description_text = html2text.html2text(item['description']['string'])
        # description_text.handle(item['description']['string'])
        with open(f'posts/{current}/description.txt', 'w', encoding='UTF-8') as description:
            description.write(description_text)

        with open(f'posts/{current}/media.json', 'w', encoding='UTF-8') as media:
            json_text = {}
            json_text['id'] = item['id']
            json_text['media'] = item['mediaUrls']
            media_json = json.dumps(json_text)
            media.write(str(json_text))


if __name__ == '__main__':
    main()