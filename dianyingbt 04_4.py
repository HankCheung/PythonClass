# -*- coding:utf-8 -*-
import urllib.request
import os

url = "http://www.bttt.la"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=url, headers=headers)
index_data = urllib.request.urlopen(req).read().decode("utf-8")
con_url_data = index_data.split('<div class="title">')
page = 1
os.mkdir("down_data\\"+str(page))
for eve in con_url_data[1:]:
    eve_con_url = url+eve.split('<a href="')[1].split('" target=')[0]
    print(eve_con_url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=eve_con_url, headers=headers)
    eve_con_data = urllib.request.urlopen(req).read().decode("utf-8").split('<div class="tinfo">')
    print("-" * 50)
    i = 0
    for ieve in eve_con_data[1:]:
        ieve_downpage_url =url + ieve.split('<a href="')[1].split('" title=')[0]
        ieve_downpage_title =  ieve.split('title="')[1].split('" target=')[0]
        print(ieve_downpage_url)
        print(ieve_downpage_title)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=ieve_downpage_url, headers=headers)
        down_url =url+ urllib.request.urlopen(req).read().decode("utf-8").split('<form action="')[1].split('" method')[0]
        print(down_url)
        print("-" * 50)
        file_name =  ieve_downpage_title.replace("/"," ") + '.torrent'


        with open("down_data\\"+str(page)+"\\"+file_name, "wb") as f:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            req = urllib.request.Request(url=down_url, headers=headers)
            f.write(urllib.request.urlopen(req).read())
    # print(eve_con_data)
    # print("-"*50)