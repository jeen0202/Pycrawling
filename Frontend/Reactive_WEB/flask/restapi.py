from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import requests #html load를 위한 library
from bs4 import BeautifulSoup # parsing을 위한 library

app = Flask(__name__)
CORS(app)

@app.route('/news',methods=['GET','POST'])
def news():
    res = requests.get('https://news.naver.com',
    headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(res.content, 'html.parser')
    myData = soup.find(class_ ='lnk_hdline_article') 
    ## list crawling
    myList = soup.select("#_rankingList0 > li > div > div > div > a.list_tit")
    myPics = soup.select("#_rankingList0 > li > a > img")    
    #print(type(myList))
    #print(myData.string)
    news_data = dict()    
    news_data['info'] = myData.string
    news_data['status'] = True
    news_data['newsList'] = list()
    news_data['newsLinks'] = list()
    news_data['newsImgs'] = list()
    for item in myList:
        news_data['newsList'].append(item.get_text())
        news_data['newsLinks'].append(item['href'])
    
    for item in myPics:
        news_data['newsImgs'].append(item['src'])    

    #print(news_data['newsList'])
    if request.method == "POST":
        #print("POST")
        data = request.get_json()
        #print(data)
        #print(data['email'])
    if request.method == 'GET':
        print("GET")
        user = request.args.get('email')
        print(user)

    stock_res = requests.get('https://finance.naver.com/',
    headers={'User-Agent':'Mozilla/5.0'})
    stock_soup = BeautifulSoup(stock_res.content, 'html.parser')
    stockLists = stock_soup.select("#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > th > a")
    stockCosts = stock_soup.select("#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > td:nth-child(2)")
    stockChanges = stock_soup.select("#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > td:nth-child(3) > span")

    news_data['stocks'] = list()
    news_data['stock_costs'] = list()
    news_data['stock_changes'] = list()
    for item in stockLists:
        news_data['stocks'].append(item.get_text())
    for item in stockCosts:
        news_data['stock_costs'].append(item.get_text())
    for item in stockChanges:
        news_data['stock_changes'].append(item.get_text())
    return make_response(jsonify(news_data), 200)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8085")