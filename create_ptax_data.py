import csv
import p_tax
import read_from_csv
import SpecialInput
import random
import string
import json
import initialise

def create_property_tax_data():
    with open('practice.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        n=0
        parvm=0
        parbm=0
        
        for i in csv_reader:
            n+=1
            a = p_tax.Property(property_name=i[0],property_location=i[1],property_plot_area=float(i[2]),property_bup_area=float(i[3]),
                            property_age=int(i[4]),property_type=i[5],property_class=i[6],property_construction_cost=int(i[7]))
            dictdata = a.get_dict_complete()
            if dictdata['presumed annual rent by built up method'] < dictdata['presumed annual rent by valuation method']:
                parbm+=1
            else:
                parvm+=1
            read_from_csv.write_tax_data_csv(dictdata)
            SpecialInput.writefile(nameoffile='property_text.txt',text=(str(a)+'\n'+'-------------------------------------'+'\n'+'-------------------------------------'+'\n').title())
        return {'total_records':n,'rent_by_val_met':parvm,'rent_by_bup_meth':parbm}

def create_property_data(list_of_villages,list_of_types,list_of_plot_area,list_of_age,list_of_class,list_of_construction_cost):
        
    with open('practice.csv','a+',newline='') as csvfile:
        list_complete_name=['property_name','property_location','property_plot_area','property_bup_area','property_age','property_type','property_class','property_construction_cost']
        csvwrite=csv.writer(csvfile)
        csvwrite.writerow(list_complete_name)
        for property_location in list_of_villages:
            for property_plot_area in list_of_plot_area:
                for property_bup_area in range(int(property_plot_area/2),int(property_plot_area*1.2),int(property_plot_area/4)):
                    for property_type in list_of_types:
                        for property_class in list_of_class:
                            for property_age in list_of_age:                    
                                for property_construction_cost in list_of_construction_cost:
                                    property_name=(''.join(random.choices(string.ascii_lowercase, k=5)))
                                    list_complete=[property_name,property_location,property_plot_area,property_bup_area,property_age,property_type,property_class,property_construction_cost]
                                    csvwrite.writerow(list_complete)

def get_data_funtion(y):
    if y==True:        
        with open('circle_rates.json','r+') as jsonfile:
            datadict=json.load(jsonfile)
        list_of_villages=list(datadict['residential'].keys())
        range_beg_plot_area= int(input('please enter beginning plot area'))
        range_end_plot_area= int(input('please enter ending plot area'))
        step_plot_area= int(input('please enter step of property'))
        range_beg_age=int(input('please enter building begginging age'))
        range_end_age=int(input('please enter  building end age'))
        step_age=int(input('please enter step age'))
        list_construction_cost=input('please enter list of construction cost separated by space')
        list_ccost = list_construction_cost.split(' ')
        list_of_construction_cost = [int(i.strip()) for i in list_ccost]
        return {'list_of_villages':list_of_villages,'range_beg_plot_area':range_beg_plot_area,
                'range_end_plot_area':range_end_plot_area,'step_plot_area':step_plot_area,
                'range_beg_age':range_beg_age,'range_end_age':range_end_age,'step_age':step_age,'list_of_types':['residential','commercial'],
                'list_of_class':['1','2'],
                'list_of_construction_cost':list_of_construction_cost}
    
if __name__ == '__main__':
    choice=input('Do you want to enter new data')
    choice = SpecialInput.check_string(choice)
    if choice:
        infodict= get_data_funtion(True)
        list_of_villages=infodict['list_of_villages']
        range_beg_plot_area= infodict['range_beg_plot_area']
        range_end_plot_area= infodict['range__plot_area']
        step_plot_area= infodict['step_plot_area']
        range_beg_age=infodict['range_beg_age']
        range_end_age=infodict['range_end_age']
        step_age=infodict['step_age']
        list_of_types = infodict['list_of_types']
        list_of_class = infodict['list_of_class']
        list_of_construction_cost = infodict['list_of_construction_cost']
        list_of_plot_area=[i for i in range(range_beg_plot_area,range_end_plot_area,step_plot_area)]
        list_of_age=[i for i in range(range_beg_age,range_end_age,step_age)]

    else:   
        datadict={}
        with open('circle_rates.json','r+') as jsonfile:
            datadict=json.load(jsonfile)
        list_of_villages=list(datadict['residential'].keys())
        list_of_types=['residential','commercial']
        list_of_plot_area=[i for i in range(200,2201,1000)]
        list_of_age=[i for i in range(1,26,5)]
        list_of_class=['1','2']
        list_of_construction_cost=[700,1000,1100,1300]
    initialise.initialize()
    create_property_data(list_of_villages,list_of_types,list_of_plot_area,list_of_age,list_of_class,list_of_construction_cost)
    create_property_tax_data()
