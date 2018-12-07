'''
Created on 2014年9月7日

@author: atheq33
'''

'''
Created on 2014/1/17
bing catch with methods of JSON
@author: atheq33
'''
#-*-coding:utf-8-*-
import json, os, urllib.request as urlrequest, sys,time
import requests
from bs4 import BeautifulSoup 

def CatchBing():
    proxies = {
     "http":"proxy.cht.com.tw:8080" ,
     "https":"proxy.cht.com.tw:8080"
     }
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1389160527752&pid=hp'
    soup = BeautifulSoup(requests.get(url, proxies=proxies).text)
#     json_data = soup.html.body.p.get_text()
    content = json.loads(soup.text)
    images_dic = content['images'][0]
    pic_url = 'http://www.bing.com/'+images_dic['url']
    pic_date = images_dic['startdate']
    pic_info = images_dic['copyright'].split('(')[0].strip()
    pic_name = r'D:\桌布\{}_{}.jpg'.format(pic_date,pic_info)
    
    try:
        if os.path.exists(pic_name):
            print('{} has Already Existed!'.format(pic_info))
            # sys.exit(0)
        else:
            #urlretrieve(file_url,filename)
            r = requests.get(pic_url,proxies=proxies,stream=True)
            #r = requests.get(file_url,stream=True)
            with open(pic_name,"wb") as f:
                 for chunk in r.iter_content(chunk_size=1024):
                     f.write(chunk)
            # print("download "+filename)
            # urlrequest.urlretrieve(pic_url,pic_name)
            print("Finish!\nToday's picture is {}".format(pic_info))
    except Exception as ex:
        print(ex)
    time.sleep(3)
#     os.system('pause')
#     try:
#         urlreuest.urlretrieve(pic_url,)

if __name__ == '__main__':
    CatchBing()
    # os.system('pause')