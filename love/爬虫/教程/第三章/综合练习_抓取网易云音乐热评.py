# 1. 找到未加密的参数                   # window.arsea(参数, xxx, xxx, xxx)
# 2. 想办法把参数进行加密(必须参考网易的逻辑)  params ==> encText, encSecKey ==> encSenKey
# 3. 请求到网易, 拿到评论信息

# 需要安装pycrypto
from base64 import b64encode
from Crypto.Cipher import AES
import requests
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求方式是post
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_64561"
}

f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "'0CoJUm6Qyw8W8jud'"
e = "010001"
i = "'0CoJUm6Qyw8W8jud'"


def get_encSeckey():
    return "67979cdd17352f53b44da59236b81751d9aca08ddf7adb79025c2fc524570915c03fd1713751b287cbaa19d1e3b5ec564b05eacb56889d2b7c4083500a2f8d4bf190c3e0f4c8cf9c1adda13ccc0fb92546b7900e93a0fcdb051a7b56f9d69f45cce6ebf51b722a4c385f73fec11b7ab62f8407d82cd9803c800c4a4eccdbd304"


def get_params(data):  # 默认这里接收到的是字符串
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second  # 返回的就是params


def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(data, key):  # 加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)  # 创造加密
    bs = aes.encrypt(data.encode("utf-8"))  # 加密, 加密的内容长度必须是16的倍数
    return str(b64encode(bs), "utf-8")  # 转换成字符串


# 处理加密过程
"""
    function a(a) {  # 随机的十六位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  # 循环16次
            e = Math.random() * b.length,  # 随机数
            e = Math.floor(e),  # 取整
            c += b.charAt(e);  # 取字符串
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e 是数据
          , f = CryptoJS.AES.encrypt(e, c, {  # c 加密的密钥
            iv: d,  # 偏移量
            mode: CryptoJS.mode.CBC  # 加密模式: cbc
        });
        return f.toString()
    }
    function c(a, b, c) {  # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {   # d: 数据,    e: 010001,  f:很长, 等于外面的f,   g=外面的g
        var h = {}  # 空对象
          , i = a(16);  # i就是一个16位的随机值  把i设置成定值
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),  # 返回的就是params,  i 也是密钥
        h.encSecKey = c(i, e, f),  # 得到的就是encSecKey, e和f是定死的, 如果此时我把i固定, 得到的key一定是固定的
        h
    }
    
    两次加密:
    数据+g => b => 第一次加密的+i => b = params
"""
resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSeckey()
})

print(resp.text)