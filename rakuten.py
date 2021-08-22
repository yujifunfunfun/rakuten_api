import csv
import sys
import codecs
import math
import random
import requests
from time import sleep
import re
import pandas as pd
import urllib.parse


def main(keyword,sort,count,csv):

    s_quote = urllib.parse.quote(keyword)

    url = f'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?applicationId=1071977349781880110&keyword={s_quote}&sort={sort}&hits={count}'

    r = requests.get(url)
    resp = r.json()

    df = pd.DataFrame()

    for i in resp['Items']:
        item = i['Item']
        name = item['itemName']
        price = item['itemPrice']
        url = item['itemUrl']
        shopname = item['shopName']
        caption = item['itemCaption']
        review_count = item['reviewCount']
        review_average = item['reviewAverage']

        # DataFrameに対して辞書形式でデータを追加する
        df = df.append(
            {"商品名": name, 
             "価格": price,
             "URL": url,
             "ショップ名": shopname,
             "キャプション": caption,
             "レビュー数": review_count,
             "レビュー平均": review_average
             }, 
            ignore_index=True)
    
    df.to_csv(csv,encoding="utf_8-sig")



if __name__ == "__main__":
    main()