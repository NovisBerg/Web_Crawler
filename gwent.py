import json

import requests
from requests.exceptions import RequestException

def get_page_cards(page):
    form = {
        'token' : '',
        'page' : page,
        'size' : 30,
        'collect' : 0
    }
    url = "https://www.iyingdi.com/gwent/card/search/vertical"
    try:
        response = requests.post(url, data=form)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('获取页面出错')
        return None

#将结果写入cards.txt
def write_to_file(card):
    with open('cards.py','a',encoding='utf8') as f:
        f.write(json.dumps(card, ensure_ascii = False) + '\n')
        f.close()

# 从源码中提取卡牌信息
def parse_page_cards(html):
    data = json.loads(html)  #把请求结果中的json字符串转为字典
    cards = data['data']['cards'] #取出字典结果中的'data'的value
    return cards



# 主函数
def main():
    html = get_page_cards(0)
    cards = parse_page_cards(html)
    for card in cards:
        if 'attribute' in card:
            print('存在')
        else:
            print('不存在')
        write_to_file(card)
    # for x in range(0, 28):
    #     html = get_page_cards(x)
    #     # print(html)
    #     cards = parse_page_cards(html)
    #     for card in cards: #card类型是dic
    #         write_to_file(card)

if __name__ == '__main__':
    main()