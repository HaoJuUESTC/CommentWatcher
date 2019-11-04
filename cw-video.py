# -*- encoding: utf-8 -*-
import requests
import os
import time
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA

oids=['63148356']
pages = 50

count = 0

while True:
	for oid in oids:
		lines = []
		lines.append('uname,message,uid,ctime\n')
		for page in range(1, pages+1):
			try:
				print('Getting '+oid+' page '+str(page)+' - '+str(count))
				response = requests.get('https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn='+str(page)+'&type=1&oid='+oid+'&sort=0&_=1562316459358')
				responselist = response.json()['data']['replies']
				for comment in responselist:
					mid = comment['member']['mid']
					uname = comment['member']['uname']
					message = comment['content']['message']
					message = message.replace('\n','\\n')
					ctime = comment['ctime']
					lines.append(','.join([uname,message,mid,str(ctime)])+'\n')
			except TypeError:
				break
			except Exception as e:
				print('Error, wait 10 sec')
				print(e)
				lines.append('Failed to get page '+page+'\n')
				time.sleep(10)
				pass
			time.sleep(1)
		print('Saving to Zip')
		try:
			with ZipFile('.\\'+oid+'.zip', mode='a', compression=ZIP_BZIP2, allowZip64=True) as zfile:
				zfile.writestr(oid+'-'+str(int(time.time()))+'-'+str(count)+'.csv', ''.join(lines))
		except Exception as e:
			print(e)
			pass
	time.sleep(1)
	count += 1
