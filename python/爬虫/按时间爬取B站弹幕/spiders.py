import re
import datetime
import time
import requests

header={'cookie': "buvid3=D00C8C61-9E86-B5FE-BB08-74A1262A493772975infoc; _uuid=BAE13F99-84D9-4B73-4C9F-4E119A01AE7F75056infoc; blackside_state=1; rpdid=|(um~RY||k~l0J'uY|mYRYR~~; fingerprint3=18908b59be9c8bf87cf1f64439fc19ab; buvid_fp=D00C8C61-9E86-B5FE-BB08-74A1262A493772975infoc; LIVE_BUVID=AUTO1016153772875827; PVID=1; fingerprint=d436f0536a834d565fefff1439c04cde; buvid_fp_plain=999ED077-060D-430F-B6C5-BBF662671FF0148811infoc; SESSDATA=7ca84984,1652008091,05ff5*b1; bili_jct=322ec71b8eb67217b20231808bc1b324; DedeUserID=258150796; DedeUserID__ckMd5=62a6a6f15868161a; sid=azlyxhcs; i-wanna-go-back=1; b_ut=6; video_page_version=v_old_home; CURRENT_BLACKGAP=0; CURRENT_FNVAL=2000; CURRENT_QUALITY=0; innersign=1", 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}

url1="https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=73717870&date="   #查看历史弹幕的接口，后面接日期，下载的文件时乱码



regex=re.compile(":.*@")   #弹幕部分不是乱码，用正则表达式提取



start=datetime.date(2019,1,26)  #设置日期
end=datetime.date(2020,1,17)
k=start
f=open("dm","w",encoding="utf-8")
while (int(end.__sub__(k).days)>=0):
	z=k.strftime("%Y-%m-%d")
	k = (k + datetime.timedelta(days = 1))
	url=url1+z
	r = requests.get(url, headers=header)
	text = regex.findall(r.text)
	print(z)
	for i in text:
		f.write(i[2:-1])
		f.write("\n")
