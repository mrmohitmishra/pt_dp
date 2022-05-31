import json
import SpecialInput
def write_rates(rate_tax_resid,rate_tax_commer):
    with open('p_tax_rates.json','w') as json_file:
        json.dump({'residential':rate_tax_resid,'commercial':rate_tax_commer},json_file)
    return True
    
def read_rates(json_file_name='p_tax_rates.json'):
    with open(json_file_name , 'r') as json_file:
        data=json.load(json_file)
    return data

def write_circle_rates(residential_circle_rate_dict,commercial_circle_rate_dict,industrial_circle_rate_dict):
    with open('circle_rates.json','w') as json_file:
        json.dump({'residential':residential_circle_rate_dict,'commercial':commercial_circle_rate_dict,'industrial':industrial_circle_rate_dict},json_file,indent=4)
    return True
    
def read_circle_rates(json_file_name='circle_rates.json'):
    with open(json_file_name , 'r') as json_file:
        data=json.load(json_file)
    return data

def write_property_par(residential_dict,commercial_dict):
    with open('presumed_annual_rent.json','w') as json_file:
        json.dump({'residential':residential_dict,'commercial':commercial_dict},json_file)
    return True
    
def read_property_par(json_file_name='presumed_annual_rent.json'):
    with open(json_file_name , 'r') as json_file:
        data=json.load(json_file)
    return data


if __name__ == '__main__':
    # rate_tax_resid =  SpecialInput.read_float_ranged('enter residential tax rates',0,100) 
    # rate_tax_commer = SpecialInput.read_float_ranged('enter commercial tax rates',0,100)
    rates =  read_rates()
    print(rates)
    print(rates['residential'])
    print(rates['commercial'])
    commercial_circle_rate ={
        "marwad": 188764.80,
        "dalwada": 188764.80,
        "kadaiya": 125843.2,
        "devka": 125843.2,
        "bhimpore": 188764.80,
        "jani vankad": 188764.80,
        "varkund": 188764.80,
        "dunetha": 188764.80,
        "dabhel": 283147.20,
        "ringanwada": 283147.20,
        "kachigam": 283147.20,
        "palhit": 125843.20,
        "bhamti": 125843.20,
        "dholar": 125843.20,
        "damanwada": 125843.20,
        "pariyari": 125843.20,
        "patlara": 125843.20,
        "naila pardi": 125843.20,
        "deva pardi": 125843.20,
        "jampore": 125843.20
    }
    residential_circle_rate ={
        "marwad": 90956.25,
        "dalwada": 90956.25,
        "kadaiya": 90956.25,
        "devka": 90956.25,
        "bhimpore": 90956.25,
        "jani vankad": 90956.25,
        "varkund": 121275,
        "dunetha": 121275,
        "dabhel": 121275,
        "ringanwada": 121275,
        "kachigam": 121275,
        "palhit": 90956.25,
        "bhamti": 90956.25,
        "dholar": 90956.25,
        "damanwada": 90956.25,
        "pariyari": 90956.25,
        "patlara": 90956.25,
        "naila pardi": 90956.25,
        "deva pardi": 90956.25,
        "jampore": 90956.25
    }
    

    industrial_circle_rate ={
        "marwad": 188764.80,
        "dalwada": 188764.80,
        "kadaiya": 125843.2,
        "devka": 125843.2,
        "bhimpore": 188764.80,
        "jani vankad": 188764.80,
        "varkund": 188764.80,
        "dunetha": 188764.80,
        "dabhel": 283147.20,
        "ringanwada": 283147.20,
        "kachigam": 283147.20,
        "palhit": 125843.20,
        "bhamti": 125843.20,
        "dholar": 125843.20,
        "damanwada": 125843.20,
        "pariyari": 125843.20,
        "patlara": 125843.20,
        "naila pardi": 125843.20,
        "deva pardi": 125843.20,
        "jampore": 125843.20
    }

    write_circle_rates(residential_circle_rate,commercial_circle_rate,industrial_circle_rate)
    choice=input('Do you want to enter new data')
    choice = SpecialInput.check_string(choice)
    if choice:
        r_par_1=input('please enter rates for residential class 1')
        r_par_2=input('please enter rates for residential class 2')
        c_par_1=input('please enter rates for commercial class 1')
        c_par_2 =input('please enter rates for commercial class 2')
        residen_par = {'1':r_par_1,'2':r_par_2}
        commerc_par = {'1':c_par_1,'2':c_par_2}
    else:
        residen_par = {'1':100,'2':50}
        commerc_par = {'1':150,'2':80}

    write_property_par(residential_dict=residen_par,commercial_dict=commerc_par)
    print(read_property_par())