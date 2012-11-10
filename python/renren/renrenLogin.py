#!/usr/bin/env python
#encoding=utf-8

import urllib, urllib2, cookielib, json, time, hashlib, re, sys
import random

class Renren(object):
	def __init__(self,email,password,idn):
		self.email=email
		self.password=password
		self.idn=idn
		# 人人网的登录主页
		self.origURL='http://www.renren.com/SysHome.do'
		self.domain='renren.com'
		self.requestToken=''
		self.rtk=''
		# 如果有本地cookie，登录时无需验证。
		self.cj = cookielib.LWPCookieJar()
		try:
			self.cj.revert('renren.cookie')
			#print("OK");
		except:
			pass
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		urllib2.install_opener(self.opener)

	def get_token(self,rawHtml):
		try:
			self.requestToken=re.findall('get_check:\'[\d-]*\'?',rawHtml)[0].split(':')[1].strip('\'')
			print self.requestToken
			self.rtk=re.findall('get_check_x:\'.*?\'',rawHtml)[0].split(':')[1].strip('\'')
			print self.rtk
			return True
		except:
			return False

	def login(self):
		"""模拟登录"""
		# 通过查看renren页面源码，找到要填充的变量，如下面的'email', 'password'等
		
		headers=[("User-Agent","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.79 Safari/537.1"),
				 ("Content-Type","application/x-www-form-urlencoded")]
		params = {'email':self.email,'password':self.password}
		# 进行编码，并请求
		req = urllib2.Request(
			'http://www.renren.com/PLogin.do',
			urllib.urlencode(params)
		)
		self.opener.addheaders=headers
		r = self.opener.open(req)
		rawHtml=r.read()
		self.cj.save('renren.cookie')
		open('res.html','w').write(rawHtml)
		return self.get_token(rawHtml)

	def status(self, status):
		#发布状态
		params = {'content':status,'hostid':self.idn,'requestToken':self.requestToken,'channel':'renren','_rtk':self.rtk}
		# 进行编码，并请求
		req = urllib2.Request(
			'http://shell.renren.com/'+self.idn+'/status',
			urllib.urlencode(params)
		)
		rawHtml=self.opener.open(req).read()
		return self.get_token(rawHtml)
		
def sleep_time():
	dt = list(time.localtime())
	hour = dt[3]
	minut = dt[4]
	second = dt[5]
	return 3600-(minut*60+second)

def get_hour():
	dt = list(time.localtime())
	hour = dt[3]
	return int(hour)


if __name__ == "__main__":
	#fill in your user account here
	_renren=Renren('username','password','yourid')
	if(_renren.login()):
		print "working..."
	else:
		print 'login error'
		exit(0)
	showlist=[' (吃饭) ',' (调皮) ',' (惊恐) ',' (可爱) ',' (囧) ',' (流口水) ',' (偷笑) ',' (吻) ',' (害羞) ',' (sbq) ',' (mb) ',' (色) ',' (xx) ']
	while(1):
		t=sleep_time()
		print 'next bell: ',t,'(s)'
		if(t>=100):
			time.sleep(100)
			continue
		else:
			time.sleep(t)
		status='整点报时:'
		now=get_hour()
		now_show=random.choice(showlist)
		if(now==0): now=24
		for i in xrange(now):
			status+=now_show
		_renren.login()
		if(_renren.status(status+' 北京时间'+str(now)+'点整')):
			print get_hour() + 'OK'

