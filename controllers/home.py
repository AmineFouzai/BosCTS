
'''
Preset controller by torn for / route
'''
from .modules import *
import configparser

class DNSHandler(tornado.web.RequestHandler):
	def get(self):
		conf=configparser.ConfigParser()
		conf.read('DNS.ini')
		self.write(tornado.escape.json_encode({"DNS":conf.get('DNSSection','host')}))
	
	def post(self):
		data=tornado.escape.json_decode(self.request.body)
		print(data)
		conf=configparser.ConfigParser()
		confile=open('DNS.ini','w')
		conf.add_section('DNSSection')
		conf.set('DNSSection','host',data['DNS'].replace('http://',''))
		conf.write(confile)
		self.write(tornado.escape.json_encode({"result":"DNS Resolved"}))
	