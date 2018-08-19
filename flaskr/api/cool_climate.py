import config
import requests
import xmltodict
import pdb
class CoolClimate:
	
	def __init__(self):
		self.default_params = {'input_location': '02143','input_location_mode': '1', 'input_size': '1', 'input_income': '1'}
		self.app_key = config.app_key
		self.app_id = config.app_id
		self.url = 'https://apis.berkeley.edu/coolclimate/footprint-defaults'
	def get(self,params = {}):
		headers =  {'app_key':self.app_key,'app_id':self.app_id}
		params = {**self.default_params,**params}
		req = requests.get(self.url,headers = headers,params = params)
		r_dict = xmltodict.parse(req.text)
		return r_dict['response']