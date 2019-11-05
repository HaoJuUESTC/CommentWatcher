# -*- encoding: utf-8 -*-
import requests
import os
import time
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA

oids=['63148356']
pages = 30

count = 0

while True:
	for oid in oids:
		lines = []
		ctime2uid = {}
		lines.append('uname,message,uid,ctime\n')
		for page in range(1, pages+1):

			print('Getting '+oid+' page '+str(page)+' - '+str(count))
			success = False
			for retry in range(0,5):
				try:
					response = requests.get('https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn='+str(page)+'&type=1&oid='+oid+'&sort=0&_=1562316459358', timeout=5)
				except Exception as e:
					print(e)
					time.sleep(5)
					continue
				success = True
				break

			if success:
				print('Success')
				try:
					responselist = response.json()['data']['replies']
					for comment in responselist:
						mid = comment['member']['mid']
						uid = comment['member']['uname']
						message = comment['content']['message']
						message = message.replace('\n','\\n')
						message = message.replace('\r','\\r')
						ctime = comment['ctime']
						if (ctime not in ctime2uid or ctime2uid[ctime] != uid):
							ctime2uid[ctime] = uid
							lines.append(','.join([uid,message,mid,str(ctime)])+'\n')
				except TypeError:
					break
				except Exception as e:
					print(e)
					lines.append('Failed to get page '+page+'\n')
					time.sleep(5)
				else:
					time.sleep(1)

		print('Saving to Zip')
		try:
			with ZipFile('.\\'+oid+'.zip', mode='a', compression=ZIP_BZIP2, allowZip64=True) as zfile:
				zfile.writestr(oid+'-'+str(int(time.time()))+'-'+str(count)+'.csv', ''.join(lines))
		except Exception as e:
			print('Failed')
			print(e)
			pass
	time.sleep(1)
	count += 1
