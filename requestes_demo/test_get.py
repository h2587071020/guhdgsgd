import allure
import requests




@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例1")
def test_no_params():
    # r = requests.request(method="get",url="https://www.baidu.com/")
    r=requests.get("https://www.baidu.com/")
    # sess=requests.session()
    # r = sess.request(method="get", url="https://www.baidu.com/")
    # r = sess.request(method="get", url="https://www.baidu.com/")

    print(r.text)


@allure.feature("get请求")
@allure.story("有参数")
@allure.title("用例2")
def test_params():
    dfg={"accountName":"xuepl123"}
    w=requests.get("http://qa.yansl.com:8084/acc/getAccInfo",params=dfg)
    print(w.text)

@allure.feature("get请求")
@allure.story("path参数")
@allure.title("用例3")
def test_get_path():
    # w = requests.request("get","http://qa.yansl.com:8084/acc/getAllAccs/{}/{}".format(1, 3))
    w=requests.get("http://qa.yansl.com:8084/acc/getAllAccs/{}/{}".format(1,3))
    print(w.text)



@allure.feature("get请求")
@allure.story("下载文件")
@allure.title("用例4")
def test_get_file(pub_data):
    with allure.step("第一步、准备测试数据"):pass
    h={"token":pub_data["token"]}
    c={"pridCode":"63803y"}
    with allure.step("第二步、发送请求"): pass
    r = requests.request("GET", "http://qa.yansl.com:8084/product/downProdRepertory",params=c,headers=h)
    with allure.step("第三步、请求数据"):
        allure.attach("请求行,请求头,请求正文","请求信息",allure.attachment_type.TEXT)
    with open("heheaa.xls","wb")as f:
        f.write(r.content)











