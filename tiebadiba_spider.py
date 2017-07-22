# -*- coding: utf-8 -*-
import urllib.request
#help(open)

main_url = r'https://tieba.baidu.com'
page = 0;
for page in range(0,1000,50):
    url = "https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=" + str(page) + ".html"
    print(url)
    url_data = urllib.request.urlopen(url).read().decode("utf-8")
    first_ana_data = url_data.split('<div class="threadlist_title pull_left j_th_tit ">')
    with open('diba_data.txt',encoding="utf-8",mode='a') as f:
        f.write(str(page/50)+'\n')
        for eve in first_ana_data[1:]:
            title_url = eve.split('<a href="')[1].split('"')[0]
            title = eve.split('title="')[1].split('"')[0]
            ele_data =title+"   "+main_url+title_url
            print(ele_data)
            # ele_data=ele_data.replace('\U0001f697', u' ')
            f.write(ele_data+'\n')

        print("-"*80)