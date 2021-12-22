import requests
#杯子
# url1="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11600832514977741391&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E6%9D%AF%E5%AD%90&queryWord=%E6%9D%AF%E5%AD%90&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn="
# url2="&rn=30&gsm=3c&1640072795289="
#剪刀
# url1="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11224354450780956549&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E5%89%AA%E5%88%80&queryWord=%E5%89%AA%E5%88%80&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn="
# url2="&rn=30&gsm=5a&1640087805403="
#手机
url1="https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10844385999817288927&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E6%89%8B%E6%9C%BA&queryWord=%E6%89%8B%E6%9C%BA&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn="
url2="&rn=30&gsm=3c&1640088238902="
header={
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
}
cnt=1
for i in range(7):
	z=i+20
	print(z)
	# if i==14 or i==15 or i==16:
	# 	continue
	url=url1+str(z*30)+url2
	r=requests.get(url,headers=header)
	js=r.json()
	for j in range(30):
		url3=js["data"][j]["middleURL"]
		r2=requests.get(url3,headers=header)
		f=open("validation\\手机\\"+str(cnt)+".jpg","wb")
		cnt+=1
		f.write(r2.content)
		f.close()