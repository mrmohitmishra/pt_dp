import csv
import p_tax
import os
import read_from_csv
import SpecialInput

def read_tax_data():
    with open('practice.csv','r') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        
        for i in csv_reader:
            a = p_tax.Property(property_name=i[0],property_location=i[1],property_plot_area=float(i[2]),property_bup_area=float(i[3]),
                            property_age=int(i[4]),property_type=i[5],property_class=i[6],property_construction_cost=int(i[7]))
            yield str(a)

def write_tax_data_csv(dictionary_pty):
    if os.path.exists('property_tax.csv'):
        with open('property_tax.csv', 'a+',newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file,dictionary_pty.keys())
            csv_writer.writerow(dictionary_pty)
    else:
        with open('property_tax.csv', 'w',newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file,dictionary_pty.keys())
            csv_writer.writeheader()
            csv_writer.writerow(dictionary_pty)

if __name__ == '__main__':
        
    with open('practice.csv') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        
        for i in csv_reader:
            a = p_tax.Property(property_name=i[0],property_location=i[1],property_plot_area=float(i[2]),property_bup_area=float(i[3]),
                            property_age=int(i[4]),property_type=i[5],property_class=i[6],property_construction_cost=int(i[7]))
            print(a)
            dictdata = a.get_dict_complete()
            print(dictdata)
            read_from_csv.write_tax_data_csv(dictdata)
            SpecialInput.writefile(nameoffile='property_text.txt',text=(str(a)+'\n'+'-------------------------------------'+'\n'+'-------------------------------------'+'\n').title())
        