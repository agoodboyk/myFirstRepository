import requests,re
from bs4 import BeautifulSoup
#自定义头文件
header={'Referer':'http://www.chsi.com.cn/cet/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Host':'www.chsi.com.cn'}
url="http://www.chsi.com.cn/cet/query"
proxies = {"http":"http://111.202.92.115:8541",
           "https":"https://122.193.14.109:8450"}
pattern = re.compile(r'\b\d{1,3}\b')
patternStyle = re.compile(r'英语\w级')

def getSorce(numId,name):
    param={'zkzh':numId,'xm':name}
    try:
        r=requests.get(url,headers=header,params=param,timeout=5)
    except Exception as e:
        print('请求失败: ',e)
        return False
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content,'html.parser')
    RAW = soup.find('table',class_='cetTable')
    if RAW != None:
        text = RAW.get_text()
    else:
        print('BS解析后',RAW)
        return False
    #print(text)
    style = re.findall(patternStyle,text)[0]
    grade = re.findall(pattern,text)
    grade.append(style)
    #print(grade , style)
    return grade

if __name__ == '__main__':
    sorce =getSorce(360651171101624,'陈美高')
    print(type(sorce[0])  , sorce)
    
