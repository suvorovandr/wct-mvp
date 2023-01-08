## Author: Andrey Suvorov
## Date: 09/01/2023
import requests
from bs4 import BeautifulSoup
import csv

def html_file(URLs):
    print("HTML 文件获取")
    n = 0
    for URL in URLs:
        n = n+1
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser") 
        with open("{}_output.html".format(n), "w", encoding = 'utf-8') as file:
            file.write(str(soup.prettify()))

def data_collect(URLs, csv_1):
    print("设备信息和价格信息获取中...")
    csv_report = open('price_monitoring_W1.csv', 'w')
    write_file = csv.writer(csv_report)
    if csv_1:
        print("数据导入csv中...")
    for URL in URLs:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        device_group = soup.find('div', {"class": "Catalog-information-right-block-left-center-info"}).h4
        price_group = soup.find('div', {"class": "Catalog-information-right-block-right-main"}).h1
        if csv_1:
            print(device_group.text, price_group.text)
            data = [device_group.text, price_group.text]
            write_file.writerow(data)
        else:
            print(device_group.text, price_group.text)
    csv_report.close()

## 设备页面列子（mvp不使用数据库）
device_1 = "https://www.mediapark.uz/products/view/15948"
device_2 = "https://www.mediapark.uz/products/view/16336"
device_3 = "https://www.mediapark.uz/products/view/15451"
device_4 = "https://www.mediapark.uz/products/view/15636"
device_5 = "https://www.mediapark.uz/products/view/15928"
device_html = "https://www.mediapark.uz/products/category/210"

URLs = [device_1, device_2, device_3, device_4, device_5]
html_file(URLs)
data_collect(URLs, True)
## data_collect(URLs,True)











