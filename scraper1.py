import requests
import time
from bs4 import BeautifulSoup
url = 'https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt'

for i in range(1,4):
    print(f"第 {i} 頁")
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'html.parser')
    datas=sp.select('h2')
    for j,bbc in enumerate(datas):
      print(f'{j+1} {bbc.text}' ,end='\t')
      print(bbc.a.get('href'))
    url = 'https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt'+'?page='+str(i+1)
    time.sleep(3)