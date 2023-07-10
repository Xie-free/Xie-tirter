# requests.get() 同步的代码 --> 异步的操作aiohttp
# pip install aiohttp

import asyncio
import aiohttp

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
    "http://kr.shanghai-jiuxin.com/file/2022/0414/e5d9c2e8a189059e61f6f757aedb79e4.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/fdc4cc14a27eddae76d09d7c854b3496.jpg"
]


async def aio_download(url):
    name = url.rsplit("/", 1)[1]  #
    async with aiohttp.ClientSession as session:  # requests
        async with session.get(url) as resp:  # resp = requests.get()
            # resp.content.read() ==> resp.content
            # 请求回来了. 写入文件
            # 可以自己去学习一个模块, aiofiles
            with open("图片/"+name, mode="wb") as f:  # 创建文件
                f.write(await resp.content.read())  # 读取内容是异步的. 需要awiait挂起

    print(name, "搞定")
    # s = aiohttp.ClientSession()  <==> requests
    # requests.get()  .post()
    # s.get()   .post()
    # 发送请求
    # 得到图片内容
    # 保存到文件


async def main():
    tasks = []
    for url in urls:
        tasks.append(aio_download(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
