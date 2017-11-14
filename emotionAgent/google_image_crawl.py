# -*-coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib
import datetime

# python파일의 위치
while True:
    emotion_num = int(raw_input("감정 종류를 숫자로 입력하시오 [1/2/3/4]: "))

    if emotion_num == 1:
        save_dir = "angery emotion"
        break
    elif emotion_num == 2:
        save_dir = "happy emotion"
        break
    elif emotion_num == 3:
        save_dir = "sad emotion"
        break
    elif emotion_num == 4:
        save_dir = "surprised emotion"
        break
    print "잘못된 입력"

find_target = raw_input(save_dir +"  에 저장할 다운할 검색어는? :")

data = {}

req = requests.get('https://www.google.co.kr/search?newwindow=1&biw=725&bih=910&tbm=isch&sa=1&q='+find_target,
         headers={'user-agent': ':Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select('div > a > img')

dirname = './LData/'+save_dir
if not os.path.isdir(dirname):
    os.mkdir(dirname)
os.chdir(dirname)

for title in my_titles:
    data[title.text] = title.get('data-src')
    try:
        s = str(datetime.datetime.now())
        s.replace(" ","")
        urllib.urlretrieve(data[title.text],s +".jpg")
        print(data[title.text])

    except:
        print("pass")
