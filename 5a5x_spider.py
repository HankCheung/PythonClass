import urllib.request
import os

page = 1
fenlei_list = ["etools","eimage","emedia","egame"]
for eve_tpye in fenlei_list:
    for page in range(1,156):
        os.mkdir("down_data\\"+str(page))
        url = "http://www.5a5x.com/wode_source/etools"+list+"/" + str(page) + ".html"
        web_list_data = urllib.request.urlopen(url).read().decode("gbk")
        first_ana_data = web_list_data.split('<dl class="down_list">')[1:]
        # print(web_list_data)
        main_url = "http://www.5a5x.com/"
        for eve in first_ana_data:
            # print(eve)
            # print("-"*50)

            url_test_data = eve.split('<dt><a href="')[1].split('"')[0]
            content_url = main_url + url_test_data
            content_page_data = urllib.request.urlopen(content_url).read().decode("gbk")
            title = content_page_data.split('<title>')[1].split('_')[0]
            # print(content_page_data)
            print(title)
            # print("-"*80)
            # print(content_page_data)
            down_page_url=main_url + content_page_data.split('<div id="down_address">')[1].split("<a href='")[1].split("'")[0]
            down_data = urllib.request.urlopen(down_page_url).read().decode('gbk')
            down_data_url =main_url + down_data.split('<div align="center">')[1].split('<a href="')[1].split('"')[0]
            # print(down_page_url)
            print(down_data_url)
            with open("down_data\\"+str(page)+"\\"+title+'.zip',"wb") as f:
                file_data = urllib.request.urlopen(down_data_url).read()
                f.write(file_data)

            # print(url_test_data)

            print("-"*50)