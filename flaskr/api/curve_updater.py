import cool_climate
import pdb

class CurveUpdater:
    params = ['input_footprint_transportation_miles1',
              'input_footprint_shopping_food_meatfisheggs', 
              'input_footprint_shopping_food_dairy']
    def __init__(self):
        self.api = cool_climate.CoolClimate()
    def vary_param(self,param):
        
        #get default value of input param
        param_default = float(self.api.default_inputs[param])

        if param_default == 0:
            param_default = '100'
            C02_default = float(self.api.get_total_C02({param:param_default}))
        else:
            C02_default = float(data_default['result_grand_total'])
        #now set value of input param to 0

        C02_0 = float(self.api.get_total_C02({param:'0'}))
        rate = (C02_default - C02_0)/param_default
        return rate
    def update_all_curves(self):
        rates = []
        for param in self.params:
            rates.append(self.vary_param(param))
        return rates
        