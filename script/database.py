from bs4 import BeautifulSoup
import requests

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
}
cookies = {

    "_identity": "NULL"
}
url = r"NULL"
html = requests.get(url, cookies=cookies, headers=header).text


def FIND_SINGLE(ITEM):
    count = 0
    for i in range(0, len(ITEM)):
        count += 1
        print("\n---------------")
        items = BeautifulSoup(str(ITEM[i]), "lxml").find_all("p")
        ans = BeautifulSoup(str(ITEM[i]), "lxml").find(
            "div", class_="Answer11").text
        if(len(items) == 1):
            print(items[0].text)
        else:
            for j in range(0, len(items)):
                print(items[j].text)
        print("答案: "+ans+"\n------------------")
    print(count)


# 选择题
qs = BeautifulSoup(html, "lxml").find_all(
    "div", class_="row 100020101", id="100020101")
FIND_SINGLE(qs)

# 编程题
qs = BeautifulSoup(html, "lxml").find_all(
    "div", class_="row 1000206", id="1000206")
print(len(qs))
for i in range(0, len(qs)):
    print(qs[i].text)

# 判断题
qs = BeautifulSoup(html, "lxml").find_all(
    "div", class_="row 1000203", id="1000203")
print(len(qs))

for i in range(0, len(qs)):
    items = BeautifulSoup(str(qs[i]), "lxml").find(
        "div", class_="noFlow").text
    ans = BeautifulSoup(str(qs[i]), "lxml").find(
        "div", class_="Answer11").text
    print(items+"\n答案: "+ans+"\n")
