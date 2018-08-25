import config
import requests
import xmltodict
import pdb
from collections import OrderedDict
class CoolClimate:
    def __init__(self):
        self.default_inputs = {'input_location': '02143',
                         'input_location_mode': '1', 
                         'input_size': '1',#one person in household
                         'input_income': '1'}
        self.app_key = config.app_key
        self.app_id = config.app_id
        
        # start by retriving default values for everything
        self.url = 'https://apis.berkeley.edu/coolclimate/footprint-defaults' 
        #two dicts, one for inputs, one for outputs
        default_data = self.get() # get everything into one dict
        self.default_inputs = {}
        self.default_outputs = {}
        #split inputs and outputs into different dicts
        for key, value in default_data.items():
            if 'result' in key:
                self.default_outputs[key] = value #add results to output dict
            else:
                self.default_inputs[key] = value#add results to input dict
        self.default_total_C02 = self.default_outputs['result_grand_total']
        self.default_inputs['input_changed'] = '1' #in general specify that inputs have been changed 
        
        #from now on, we set all the parameters
        self.url = 'https://apis.berkeley.edu/coolclimate/footprint'
               
    def get(self,params = {}):
        headers =  {'app_key':self.app_key,'app_id':self.app_id}
        params = {**self.default_inputs,**params}
        
        req = requests.get(self.url,headers = headers,params = params)
        r_dict = xmltodict.parse(req.text)
        return dict(r_dict['response']) #convert to regular dict
    def get_total_C02(self,params = {}):
        data = self.get(params)
        return data['result_grand_total']