import json
import ast
import requests
import urllib.request

from tqdm import tqdm

def main():
    for i in tqdm(range(532)):#532
        with open(f'posts/{str(i)}/media.json', 'r', encoding='UTF-8') as file:
            media = ast.literal_eval(file.read())
            # print(media)
            for item in media['media']:
                try:
                    if item['type'] == 'IMAGE':
                        image_url = item['url']
                        img_data = requests.get(image_url).content
                        with open(f'posts/{str(i)}/{media["media"].index(item)}.jpg', 'wb') as handler:
                            handler.write(img_data)
                    if item['type'] == 'VIDEO':
                        video_url = item['url']
                        urllib.request.urlretrieve(video_url, f'posts/{str(i)}/{media["media"].index(item)}_video.mp4')
                except:
                    print(f'error at object {str(i)}')
            print(f' Success at {media["id"]}')
                    # r = requests.get(video_url, stream=True)
                    #
                    # img_data = requests.get(image_url).content
                    # with open(f'posts/{str(i)}/{media["media"].index(item)}.jpg', 'wb') as handler:
                    #     handler.write(img_data)






if __name__ == '__main__':
    main()