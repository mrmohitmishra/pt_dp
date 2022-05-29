import re
import SpecialInput
import p_tax_rates
class Property():
    """this class contains basic information about a propery and is used for creating property and calculating the property and
    tax
    """
    def __init__(self,property_name='',property_location='',property_plot_area=100,
                 property_age=10,property_type='residential',property_class=1,
                 property_par=0,property_construction_type='normal',
                 property_arv=0,property_tax=0,property_far=0,property_bup_area=0,circle_rates=0):
        self.property_name = property_name        
        self.property_location=property_location
        self.property_plot_area=property_plot_area
        if property_far==0 and property_bup_area !=0:
            self.property_far = property_bup_area/property_plot_area
        if property_far!=0 and property_bup_area ==0:
            self.property_bup_area = property_far * property_plot_area
        if property_far==0 and property_bup_area ==0:
            self.property_bup_area = SpecialInput.read_int_ranged("Please enter builtup area", min_value=0,max_value=property_plot_area)
        self.property_bup_area=property_bup_area
        self.property_age=property_age
        self.property_type=property_type
        self.property_class=property_class
        self.property_par=property_par
        self.property_construction_type=property_construction_type
        self.property_arv=property_arv
        self.property_tax=property_tax
        self.p_rates= self.p_rates_applicable()
        self.property_value = self.value_pty()
        if circle_rates != 0:
            self.circle_rates=circle_rates
        else:
            self.circle_rates=self.read_circle_rate()

    def presumed_annual_rent(self):
        pass
    
    def value_pty(self):
        value_property = self.property_bup_area*
        return ()
    
    def rent_valuation_mth(self):
        pass
    
    def rent_par_mth(self):
        return float(self.property_bup_area)*int(self.property_par)
    
    def p_rates_applicable(self):
        data= p_tax_rates.read_rates()
        if self.property_type == 'residential':
            self.p_rates = float(data['residential'])
        else:
            self.p_rates = float(data['commercial'])
              
    def p_tax(self):
        return self.p_rates * self.property_arv
    
    def read_circle_rate(self):
        data= p_tax_rates.read_circle_rates()
        rates=0
        if self.property_type == 'residential':
            rates = data['residential'][self.property_location]
        elif self.property_type=='industrial':
            rates = data['industrial'][self.property_location]
        elif self.property_type=='commercial':
            rates = data['commericial'][self.property_location]
        rates = rates/(100*10.76)
        return rates

    def read_class(self):
        pass
    
    def __str__(self) -> str:
        return(' ')
    
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
                        'property_construction_type':self.property_construction_type,
                        'property_arv':self.property_arv+other.property_arv,'property_tax':self.property_tax+other.property_tax,}
        return new_pty_dict
    
    def get_dict(self):
        return {'property_name':self.property_name,'property_location':self.property_location,
                'property_plot_area':self.property_plot_area,'property_far':self.property_far,
                'property_bup_area':self.property_bup_area,'property_age':self.property_age,
                'property_type':self.property_type,'property_class':self.property_class,
                'property_par':self.property_par,'property_construction_type':self.property_construction_type,
                'property_arv':self.property_arv,'property_tax':self.property_tax,}
    
    def get_list(self):
        [self.property_name, self.property_location, self.property_plot_area, self.property_far,
         self.property_bup_area, 
         self.property_age, self.property_type, self.property_class, self.property_par, 
         self.property_construction_type, self.property_arv, self.property_tax]
    
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
            
        
    
    
    