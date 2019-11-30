import test4test as Conn
import json
import re
import requests
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index' : item[0],
            'image' : item[1],
            'title' : item[2],
            'actor' : item[3].strip()[3:],
            'time' : item[4].strip()[5:],
            'score' : item[5]+item[6]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf8') as f:
        f.write(json.dumps(content, ensure_ascii = False) + '\n')
        f.close()


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # 拿到游标
    cursor = Conn.conn.cursor()
    for item in parse_one_page(html):
        write_to_file(item)
        data = (int(item['index']),item['image'],item['title'],item['actor'],item['time'],float(item['score']))
        print(data)

        sql = 'insert into maoyan values (%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, data)

        # 涉及写操作注意要提交
    Conn.conn.commit()
    cursor.close()

if __name__ == '__main__':
   for i in range(10):
       main(i*10)
   Conn.conn.close()

