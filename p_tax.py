import re
import SpecialInput
import p_tax_rates
class Property():
    """this class contains basic information about a propery and is used for creating property and calculating the property and
    tax
    """
    def __init__(self,property_name='',property_location='',property_plot_area=100,property_far=0
                 ,property_bup_area=0,property_age=10,property_type='residential',property_class='1',
                 property_par=0,property_construction_cost=1000,
                 property_arv=0,property_tax=0,circle_rates=0):
        data = p_tax_rates.read_circle_rates()
        data_keys = list((data['residential']).keys())        
        self.property_name = property_name
        if (property_location.lower().strip() in data_keys):
            self.property_location=property_location
        else:
            self.property_location = SpecialInput.gettext('Please enter a valid location')
            self.property_location = self.property_location.strip().lower()
        self.property_type = property_type
        if circle_rates != 0:
            self.circle_rates=circle_rates
        else:
            self.circle_rates=self.read_circle_rate()
        
        self.property_plot_area=property_plot_area
        if property_far==0:
            self.property_far = property_bup_area/property_plot_area
        else:
            self.property_far=property_far
            
        if property_bup_area !=0:
            self.property_bup_area = property_bup_area
        elif property_bup_area==0:
            self.property_bup_area = property_far*property_plot_area
        self.property_age=property_age
        # !!! add some checks here
        self.property_class=str(property_class)
        self.property_construction_cost=property_construction_cost
        # TODO: add checks
        self.p_rates=0
        self.p_rates_applicable()
        self.property_value = self.value_pty()
        if property_par!=0:
            self.property_par=property_par
        else:
            self.property_par= self.presumed_annual_rent()
        if property_arv!=0:
            self.property_arv=property_arv
        else:
            self.property_arv=self.get_arv()
        if property_tax==0:
            self.property_tax=self.p_tax()

        

    def presumed_annual_rent(self):
        arvm = self.rent_valuation_mth()
        arpm = self.rent_par_mth()
        if arvm<arpm:
            return arvm
        else:
            return arpm
    
    def get_arv(self):
        return self.presumed_annual_rent() * 0.9
    
    def get_property_par(self):
        data= p_tax_rates.read_property_par()
        property_par = 0
        if self.property_type == 'residential':
            property_par = float(data['residential'][str(self.property_class)])
        else:
            property_par = float(data['commercial'][str(self.property_class)])
        return (property_par)
    
    def value_pty(self):
        value_property = (self.property_bup_area*self.property_construction_cost*self.get_multi_fac())+ self.property_plot_area*self.circle_rates
        return (value_property)
    
    def rent_valuation_mth(self):
        return self.value_pty()*0.05
    
    def rent_par_mth(self):
        return float(self.property_bup_area)*int(self.get_property_par())
    
    def p_rates_applicable(self):
        data= p_tax_rates.read_rates()
        if self.property_type == 'residential':
            self.p_rates = float(data['residential'])
        else:
            self.p_rates = float(data['commercial'])
              
    def p_tax(self):
        return self.p_rates * self.property_arv/100
    
    def read_circle_rate_sqm(self):
        data= p_tax_rates.read_circle_rates()
        rates=0
        if self.property_type == 'residential':
            rates = data['residential'][self.property_location]
        elif self.property_type=='industrial':
            rates = data['industrial'][self.property_location]
        elif self.property_type=='commercial':
            rates = data['commercial'][self.property_location]

        return rates


    def read_circle_rate(self):
        rates = self.read_circle_rate_sqm()
        rates = rates/(100*10.7639)
        return rates
    
    def read_class(self):
        pass
    
  
    
    def __add__(self, other):
        """the property age, name of the property,property type, property class and the address will be of first object. Others"""
        new_pty_dict = {'property_name':self.property_name,
                        'property_location':self.property_location,
                        'property_plot_area':self.property_plot_area+other.property_plot_area,
                        'property_far':(self.property_far+other.property_far)/2,
                        'property_bup_area':self.property_bup_area+other.property_bup_area,
                        'property_age':self.property_age,
                        'property_type':self.property_type,
                        'property_class':self.property_class,
                        'property_par':self.property_par+other.property_par,
                        'property_construction_cost':self.property_construction_cost + other.property_construction_cost,
                        'property_arv':self.property_arv+other.property_arv,'property_tax':self.property_tax+other.property_tax,}
        return new_pty_dict
    
    def get_dict(self):
        return {'property_name':self.property_name,'property_location':self.property_location,
                'property_plot_area':self.property_plot_area,'property_far':self.property_far,
                'property_bup_area':self.property_bup_area,'property_age':self.property_age,
                'property_type':self.property_type,'property_class':self.property_class,
                'property_par':self.property_par,'property_construction_cost':self.property_construction_cost,
                'property_arv':self.property_arv,'property_tax':self.property_tax,
                'value_pty':self.property_value,'circle_rates':self.circle_rates,'presumed annual rent per feet':self.property_par}
    
    def get_list(self):
        [self.property_name, self.property_location, self.property_plot_area, self.property_far,
         self.property_bup_area, 
         self.property_age, self.property_type, self.property_class, self.property_par, 
         self.property_construction_cost, self.property_arv, self.property_tax]
        
    def get_dict_complete(self):
        complete_dict = {
            'property name':self.property_name,
            'property location':self.property_location,
            'property type':self.property_type,
            'property circle rate /100 sqm':self.read_circle_rate_sqm(),
            'property circle_rates per sq feet':round(self.circle_rates,2),
            'property plot_area':self.property_plot_area,
            'property far':self.property_far,
            'property built up area':self.property_bup_area,
            'property age':self.property_age,
            'property Multi_factor':self.get_multi_fac(),
            'property_construction_cost':round(self.property_construction_cost,2),
            'property valuation':round(self.property_value,2),
            'presumed annual rent by valuation method' :round(self.rent_valuation_mth(),2), 
            'property_class':self.property_class,
            'presumed annual rent per feet':round(self.get_property_par(),2),
            'presumed annual rent by built up method':round(self.rent_par_mth(),2),
            'presumed annual rent for annual rateable value calculation':round(self.property_par,2),
            'annual rateable value': round(self.property_arv,2),
            'property_tax':round(self.property_tax,2)
        }
        return complete_dict
    
    def get_multi_fac(self):
        mf=0
        if self.property_age<=5:
            mf=1
        elif self.property_age>5 and self.property_age<=10:
            mf=0.9
        elif self.property_age>10 and self.property_age<=15:
            mf=0.8
        elif self.property_age>15 and self.property_age<=20:
            mf=0.7
        elif self.property_age>20 and self.property_age<=25:
            mf=0.6
        elif self.property_age>25:
            mf=0.5
        return mf
            
        
    def __str__(self) -> str:
        string_return= f"""
        'property name':{self.property_name}
        'property location':{self.property_location}
        'property type':{self.property_type}
        'property circle rate /100 sqm':{self.read_circle_rate_sqm()}
        'property circle_rates per sq feet':{round(self.circle_rates,2)}
        'property plot_area':{self.property_plot_area},
        'property far':{self.property_far},
        'property built up area':{self.property_bup_area},
        'property age':{self.property_age},
        'property Multi_factor':{self.get_multi_fac()},
        'property_construction_cost(BUP*Cons_Cost*MF+Plot_area*Circle_Rate)':{round(self.property_construction_cost,2)}
        'property valuation':{round(self.property_value,2)}
        'presumed annual rent by valuation
        method i.e. value *0.05':{round(self.rent_valuation_mth(),2)}
        'property_class':{self.property_class},
        'presumed annual rent per feet':{round(self.get_property_par(),2)}
        'presumed annual rent by built up method':{round(self.rent_par_mth(),2)}
        'lower of two value:
        i.e. presumed annual rent for annual rent
        rateable value calculation':{round(self.property_par,2)}
        'annual rateable value': {round(self.property_arv,2)}
        property_tax':{round(self.property_tax,2)},
        """
        return(string_return)   
    
    