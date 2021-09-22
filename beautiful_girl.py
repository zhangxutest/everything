import requests
import re
import os
import sys


def download_beautiful_girl():
    os.mkdir("image")
    num = 0
    page = 8
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
    for i in range(1, page):
        img_url = f'https://www.mn52.com/tags/%E4%B8%9D%E8%A2%9C%E7%BE%8E%E5%A5%B3/{i}/'
        resp = requests.get(img_url, headers)
        pattern = re.compile('class="item-media entry".*?data-original="(.*?)"', re.S)
        result = re.findall(pattern, resp.text)
        for img_url in result:
            resp = requests.get('https:' + img_url)
            with open('image/img_%d.jpg' % num, 'wb') as fin:
                fin.write(resp.content)
            num += 1
            print(f"下载第{num}张图片")


if __name__ == '__main__':
    a = input("按任意键开始!!!")
    print("我们开车了！")
    print("坐好！")
    print("出发！")
    download_beautiful_girl()
    print("下载完毕！")
    b = input("按任意键退出!!!")
    sys.exit()
