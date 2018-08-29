from .cool_climate import CoolClimate
import pdb

class CurveUpdater:
    params = ['input_footprint_transportation_miles1',
              'input_footprint_shopping_food_meatfisheggs', 
              'input_footprint_shopping_food_dairy']
    def __init__(self):
        self.api = CoolClimate()
    def vary_param(self,param,req_flags={}):
        
        #get default value of input param
        param_default = float(self.api.default_inputs[param])
        if param_default == 0:
            #use 100 as default data, rerequest api 
            param_default = 100
            CO2_default = float(self.api.get_total_CO2({**{param:'100'},**req_flags}))
        else:
            CO2_default = float(self.api.default_total_CO2)
        #now set value of input param to 0

        CO2_0 = float(self.api.get_total_CO2({**{param:'0'},**req_flags}))
        rate = (CO2_default - CO2_0)/param_default
        return rate
    def update_all_curves(self):
        rates = []
        for param in self.params:
            rates.append(self.vary_param(param))
        return rates
        