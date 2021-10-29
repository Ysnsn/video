# 课题：美桌壁纸小姐姐壁纸爬取
# requests
# parsel

# 爬虫的一般思路
# 1、分析目标网页，确定爬取的url路径，headers参数
# 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
# 3、解析数据 -- parsel  转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
# 4、保存数据


# 课题：爬取ip代理，构建ip代理池
# requests
# parsel

# 爬虫的一般思路
# 1、分析目标网页，确定爬取的url路径，headers参数
# 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
# 3、解析数据 -- parsel  转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
# 4、保存数据

import requests
import parsel
for page in range(1, 6):
    print('================正在爬取第{}页数据================'.format(page))
    # 1、确定爬取的url路径，headers参数
    base_url = 'http://www.win4000.com/mobile_2340_0_0_{}.html'.format(str(page))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

    # 2、发送请求 -- requests 模拟浏览器发送请求，获取响应数据
    response = requests.get(base_url, headers=headers)
    data = response.text
    # print(data)

    # 3、解析数据 -- parsel  转化为Selector对象，Selector对象具有xpath的方法，能够对转化的数据进行处理
    html_data = parsel.Selector(data)
    data_list = html_data.xpath('//div[@class="Left_bar"]//ul/li/a/@href').extract()
    # print(data_list)

    # 遍历列表元素
    for alist in data_list:
        # print(alist)
        # 发送相册的url地址请求解析相册内部图片的url地址
        response_2 = requests.get(alist, headers=headers).text

        # 解析相册内部图片的url地址
        html_2 = parsel.Selector(response_2)
        img_url = html_2.xpath('//div[@class="pic-meinv"]//img/@src').extract_first()
        # print(img_url)

        # 请求图片URL地址的图片数据
        img_data = requests.get(img_url, headers=headers).content

        # 4、保存数据
        # 4、1 准备图片文件名
        file_name = img_url.split('/')[-1]
        # print(file_name)
        # 保存数据
        with open('img\\' + file_name, 'wb') as f:
            print('正在保存图片：', file_name)
            f.write(img_data)




