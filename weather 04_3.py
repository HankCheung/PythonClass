import urllib.request
import urllib.parse
import json
city = input("请输入您要查询的城市：")
search_city = "http://tianqi.2345.com/t/searchCity.php?q="+urllib.parse.quote(city)+"&pType=local"  # parse
search_data = urllib.request.urlopen(search_city).read().decode("utf-8")
search_json_data = json.loads(search_data)['res'][0]['href']
main_url = "http://tianqi.2345.com"
city_url = main_url + search_json_data
weather_data = urllib.request.urlopen(city_url).read().decode("gbk", "ignore")
nowtemperture = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>当前气温：<i>')[1].split('</i>')[0]
nowshidu = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>湿度：<i>')[1].split('</i>')[0]
nowfengli = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>风力：<i>')[1].split('</i>')[0]
nowqiya = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>气压：<i>')[1].split('</i>')[0]
nowrichu = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>日出：<i>')[1].split('</i>')[0]
nowriluo = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>日落：<i>')[1].split('</i>')[0]
nowziwaixian = weather_data.split('<div class="wea-about" id="weaLiveInfo">')[1].split('<li>紫外线强度：<i>')[1].split('</i>')[0]

print(nowtemperture)
print(nowshidu)
print(nowfengli)
print(nowqiya)
print(nowrichu)
print(nowriluo)
print(nowziwaixian)

print(city_url)