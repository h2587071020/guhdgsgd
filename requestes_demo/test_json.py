import requests




def test_post_json(pub_data):
    data={
  "pwd": "tjf123456",
  "userName": "tan406813"
}
    h = {"token": pub_data["token"]}
    w=requests.post("http://qa.yansl.com:8084/login",json=data,headers=h)
    print(w.text)

# def test_post_formdata(pub_data):
#     data={
#   "userName": "tan406813"
# }
#     h = {"token": pub_data["token"]}
#     w=requests.post("http://qa.yansl.com:8084/user/lock",data=data,headers=h)
#     print(w.text)




# def test_post_formdata(pub_data):
#     data={
#   "file": open("heheaa.xls","rb")
# }
#     h = {"token": pub_data["token"]}
#     w=requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory",files=data,headers=h)
#     print(w.text)

    def test_post_json(pub_data):
        data = {
            "pwd": "tjf123456",
            "userName": "tan406813"
        }
        h = {"token": pub_data["token"]}
        w = requests.post("http://qa.yansl.com:8084/login", json=data, headers=h)
        print(w.text)







# 请求信息
    # 请求方法
    print("请求方法:",w.request.method)
    # url
    print("url:", w.request.url)
    # 请求头
    print("请求头:", w.request.headers)
    # 请求正文
    print("请求正文:", w.request.body)


    # 响应信息
    # 响应状态码
    print("响应状态码 :", w.status_code)
    # 响应头
    print("响应头 :", w.headers)
    # 响应正文
    print("响应正文 :", w.text) # 获取响应文本
    print("响应正文 :", w.content) # 获取响应字节码
    print("响应正文 :", w.json()["message"]) # 获取响应字典





