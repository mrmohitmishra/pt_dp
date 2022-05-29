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

if __name__ == '__main__':
    # rate_tax_resid =  SpecialInput.read_float_ranged('enter residential tax rates',0,100) 
    # rate_tax_commer = SpecialInput.read_float_ranged('enter commercial tax rates',0,100)
    rates =  read_rates()
    print(rates)
    print(rates['residential'])
    print(rates['commercial'])
    commercial_circle_rate ={
        'marwad':150000,
        'dalwada':150000,
        'kadaiya':100000,
        'devka':100000,
        'bhimpore':150000,
        'jani vankad':150000,
        'varkund':150000,
        'dunetha':150000,
        'dabhel':175000,
        'ringanwada':175000,
        'kachigam':175000,
        'palhit':75000,
        'bhamti':75000,
        'dholar':75000,
        'damanwada':75000,
        'pariyari':75000,
        'patlara':75000,
        'naila pardi':75000,
        'deva pardi':75000,
        'jampore':75000,
        'patlara':75000
    }
    residential_circle_rate ={
        'marwad':75000,
        'dalwada':75000,
        'kadaiya':75000,
        'devka':75000,
        'bhimpore':75000,
        'jani vankad':75000,
        'varkund':100000,
        'dunetha':100000,
        'dabhel':100000,
        'ringanwada':100000,
        'kachigam':100000,
        'palhit':75000,
        'bhamti':75000,
        'dholar':75000,
        'damanwada':75000,
        'pariyari':75000,
        'patlara':75000,
        'naila pardi':75000,
        'deva pardi':75000,
        'jampore':75000,
        'patlara':75000
    }

    industrial_circle_rate ={
    'marwad':100000,
    'dalwada':100000,
    'kadaiya':100000,
    'devka':100000,
    'bhimpore':150000,
    'jani vankad':150000,
    'varkund':150000,
    'dunetha':150000,
    'dabhel':225000,
    'ringanwada':225000,
    'kachigam':225000,
    'palhit':100000,
    'bhamti':100000,
    'dholar':100000,
    'damanwada':100000,
    'pariyari':100000,
    'patlara':100000,
    'naila pardi':100000,
    'deva pardi':100000,
    'jampore':100000,
    'patlara':100000
}

    write_circle_rates(residential_circle_rate,commercial_circle_rate,industrial_circle_rate)
    print(read_circle_rates())