import urllib.request
import urllib.parse
import  json

while True:
    input_data = input("please input: ")

    url ='http://fanyi.baidu.com/v2transapi'
    post_data = {}
    post_data["from"] = "en"
    post_data["query"] = input_data
    post_data["simple_means_flag"] = 3
    post_data["to"] = "zh"
    post_data["transtype"] = "translang"

    data_encode = urllib.parse.urlencode(post_data).encode("utf-8") #数据处理
    set_request = urllib.request.Request(url,data_encode)
    get_answer = urllib.request.urlopen(set_request)
    answer_data = get_answer.read().decode("utf-8")
    # print(answer_data)
    json_data = json.loads(answer_data)["trans_result"]["data"][0]["dst"]
    print("翻译结果是："+json_data)
