import requests
from bs4 import BeautifulSoup

def crawling_template(url, css_selctor):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas1 = soup.select(css_selctor)
    for item in datas1:
        return_data.append(item.get_text())
    return return_data
print(crawling_template('https://davelee-fun.github.io/', 'a[href*=product-83]'))
