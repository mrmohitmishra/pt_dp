from dataclasses import replace
import datefinder
from datetime import datetime
from datetime import timedelta
import re
from SpecialInput import *
import PySimpleGUI as sg3

def modifying_text_input(text_input):
    """_will replace any number from ninety nine to one in any text by it's numerical counterpart. Return modified text_

    Args:
        text_input (_type_): _description_

    Returns:
        _type_: _description_
    """
    number_dict = {'one hundred': '100', 'ninety nine': '99', 'ninety eight': '98', 'ninety seven': '97', 'ninety six': '96', 'ninety five': '95', 'ninety four': '94', 'ninety three': '93', 'ninety two': '92', 'ninety one': '91', 'ninety': '90', 'eighty nine': '89', 'eighty eight': '88', 'eighty seven': '87', 'eighty six': '86', 'eighty five': '85', 'eighty four': '84', 'eighty three': '83', 'eighty two': '82', 'eighty one': '81', 'eighty': '80', 'seventy nine': '79', 'seventy eight': '78', 'seventy seven': '77', 'seventy six': '76', 'seventy five': '75', 'seventy four': '74', 'seventy three': '73', 'seventy two': '72', 'seventy one': '71', 'seventy': '70', 'sixty nine': '69', 'sixty eight': '68', 'sixty seven': '67', 'sixty six': '66', 'sixty five': '65', 'sixty four': '64', 'sixty three': '63', 'sixty two': '62', 'sixty one': '61', 'sixty': '60', 'fifty nine': '59', 'fifty eight': '58', 'fifty seven': '57', 'fifty six': '56', 'fifty five': '55', 'fifty four': '54', 'fifty three': '53', 'fifty two': '52', 'fifty one': '51', 'fifty': '50', 'forty nine': '49', 'forty eight': '48', 'forty seven': '47', 'forty six': '46', 'forty five': '45', 'forty four': '44', 'forty three': '43', 'forty two': '42', 'forty one': '41', 'forty': '40', 'thirty nine': '39', 'thirty eight': '38', 'thirty seven': '37', 'thirty six': '36', 'thirty five': '35', 'thirty four': '34', 'thirty three': '33', 'thirty two': '32', 'thirty one': '31', 'thirty': '30', 'twenty nine': '29', 'twenty eight': '28', 'twenty seven': '27', 'twenty six': '26', 'twenty five': '25', 'twenty four': '24', 'twenty three': '23', 'twenty two': '22', 'twenty one': '21', 'twenty': '20', 'nineteen': '19', 'eighteen': '18', 'seventeen': '17', 'sixteen': '16', 'fifteen': '15', 'fourteen': '14', 'thirteen': '13', 'twelve': '12', 'eleven': '11', 'ten': '10', 'nine': '9', 'eight': '8', 'seven': '7', 'six': '6', 'five': '5', 'four': '4', 'three': '3', 'two': '2', 'one': '1'}
    # I am using reversed order as reversed order is necessar to allow for larger strings to be searched before smaller ones
    # Otherwise smaller ones will be replaced first and then it will break
    text_input = text_input.lower().strip()
    for key,value in number_dict.items():
        if key in text_input:
            text_input = text_input.replace(key,value)
            break
    matches = re.search(r'\s*(in|after|within)\s*a\s*(day|week|month|year)',text_input)
    if matches:
        text_inside = matches.group()
        text_inside_replaced = text_inside.replace(' a ', ' 1 ')
        text_input = text_input.replace(text_inside,text_inside_replaced)
    return text_input

def number_of_days_till_due_date(date_time_object):
    present_date = datetime.today()
    number_of_days = date_time_object - present_date
    return number_of_days.days
    

def date_parser(text_input):
    """_this will take date out of the text and give a datetime object and
    it will search and identify terms like next day, next week, in a day, in two days
    and so on_
    

    Args:
        text_input (_type_): _description_
    """
    due_date = datetime.today()
    text_inside = ""
    match = ""
    today = datetime.now()
    if re.search(r"in\s*\d+",text_input):
        for i in range(1):
            match= re.search(r"in\s*\d+\s*(day)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int(inside_digit)
                days_to_add = timedelta(days=inside_digit)
                due_date  = today + days_to_add
                break
            match= re.search(r"in\s*\d+\s*(week)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int(inside_digit)*7
                    # becasue every week will contain 7 days
                days_to_add = timedelta(days=inside_digit)
                due_date = today+days_to_add
                break
            match= re.search(r"in\s*\d+\s*(month)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int((int(inside_digit))*30.5)
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add   
                break
            match= re.search(r"in\s*\d+\s*(year)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=(int(inside_digit))*365
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add   
    elif re.search(r"\s*aft.*\s*\d+",text_input):
        for i in range(1):
            match= re.search(r"aft.*\d+\s*(day)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int(inside_digit)+1
                    # after excludes today
                days_to_add = timedelta(days=inside_digit)
                due_date = today+days_to_add   
                break
            match= re.search(r"aft.*\s*\d+\s*(week)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=(int(inside_digit))*7 + 1
                    
                    # after excludes present week
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add   
                break
            match= re.search(r"aft.*\s*\d+\s*(month)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int((int(inside_digit))*30.5) + 1
                    
                    # after excludes present week
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add 
                break
            match= re.search(r"aft.*\s*\d+\s*(year)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=(int(inside_digit))*365 + 1
                    
                    # after excludes present day
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add 
            
    elif "within" in text_input:
        for i in range(1):
            match= re.search(r"within\s*\d+\s*(day)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int(inside_digit)
                days_to_add = timedelta(days=inside_digit)
                due_date  = today + days_to_add
                break
            match= re.search(r"within\s*\d+\s*(week)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int(inside_digit)*7
                    # becasue every week will contain 7 days
                days_to_add = timedelta(days=inside_digit)
                due_date = today+days_to_add
                break
            match= re.search(r"within\s*\d+\s*(month)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=int((int(inside_digit))*30.5)
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add  
                break
            match= re.search(r"within\s*\d+\s*(year)\s*",text_input)
            if match:
                text_inside = match.group()
                inside_match = re.search(r"\d+",text_inside)
                inside_digit = inside_match.group()
                if inside_digit == None:
                    days_to_add = 0
                else:
                    inside_digit=(int(inside_digit))*365
                days_to_add = timedelta(days=inside_digit)
                due_date =  today+days_to_add    
    
    elif "tomorrow" in text_input:
        due_date = today + timedelta(days=1) 
    elif "day after tomorrow" in text_input:
        due_date = today + timedelta(days=2)      
    elif "next week" in text_input:
        due_date = today + timedelta(days=7)       
    elif "next month" in text_input:
        due_date = today + timedelta(days=30)  
    elif "next year" in text_input:
        due_date = today + timedelta(days=365)
    else:
        matches = datefinder.find_dates(text_input)
        for match in matches:
            due_date = match
            break
    return due_date
    

def text_parser(text_input):
    """_summary: This function is one of the most important  function of FollowUp app. It will take a text and return
    due date , project name and  assigned to text from the received text_

    Args:
        text_input (_type_): _Any thing  which resembles date is automatically parsed. If there is a #the word which
        comes after it will be a project and if there is an @ the word which comes after is the assigned person name_
    Returns: Due Date, Project Name and Assigned Person
    """
    text_input = modifying_text_input(text_input)
    assigned_person = ""
    project_name=""
    priority = ''
    list_name=''
    due_date = date_parser(text_input)
    
    if "@" in text_input:
        assigned_word= re.search(r'@(\w+)',text_input)
        assigned_person = assigned_word.group()
        assigned_person = assigned_person.replace("@","").strip().lower()
    if "#" in text_input:
        project_word= re.search(r'#(\w+)',text_input)
        project_name = project_word.group()
        project_name = project_name.replace("#","").strip().lower()
    if "!" in text_input:
        priority_word= re.search(r'!+\S*',text_input)
        priority_name = priority_word.group()
        priority_name = priority_name.strip()
        if priority_name == '!':
            priority = 'normal'
        elif priority_name == '!!':
            priority = 'high'
        elif priority_name == '!!!':
            priority = 'very_high'
        elif priority_name == '!!!!':
            priority = 'very_very_high'
        else:
            priority = priority_name.replace("!","").strip().lower()
    if "^" in text_input:
        list_word= re.search(r'\^(\w+)',text_input)
        list_name = list_word.group()
        list_name = list_name.replace("^","").strip().lower()
        if list_name == 'n':
            list_name = 'next_action'
        elif list_name == 'i':
            list_name = 'inbox'
        elif list_name == 's':
            list_name = 'some_day'
        
    return {"due_date":due_date,"project_name":project_name,"assigned_person":assigned_person,"priority":priority,"list_name":list_name}  
            
if __name__ == '__main__':
    while True:
        textDate = read_text('please enter any text @AssignedTo, #projectName !Priority ^ListName')
        if len(textDate)==0:
            break
        list_of_things = text_parser(textDate)
        displayprompt(list_of_things)
        displayprompt('number of days till due date' + str(number_of_days_till_due_date(list_of_things["due_date"])))