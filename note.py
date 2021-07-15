from bs4 import BeautifulSoup
import lxml
import requests


def request_html(url):
    headers = {
        "Content-Type": "text/html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    res.encoding = 'gbk2312'
    return res.text


def main():
    i = 1
    url = f"http://jinyongxiaoshuo.com/xiaoaojianghu/{1538 - i}.html"
    html = request_html(url)
    soup = BeautifulSoup(html, "lxml")
    part_list = soup.find(class_="entry").find_all("p")
    with open(r"C:\Users\admin\Desktop\1.txt", "w")as f:
        for item in part_list:
            f.write(str(item).replace("<p>", "").replace("</p>", "\r\n"))
    i += 1


if __name__ == '__main__':
    main()
