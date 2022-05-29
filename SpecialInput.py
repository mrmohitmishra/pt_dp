DEBUG_MODE = True
from datetime import datetime
import time
import PySimpleGUI as sg
import inspect
from text_parser import *
import json

def gettext(prompt):
    """Simple function to get any text in GUI in place of terminal

    Args:
        prompt (_type_): Text which shall be displayed

    Returns:
        str: what is inputed by user
    """
    layout = [[sg.Text(prompt)],
                [sg.InputText()],
                [sg.Submit(),sg.Cancel()]]
    name = inspect.stack()[len(inspect.stack())-2].function
    window = sg.Window(name ,layout)
    event,values = window.Read()
    window.Close()
    text_gettext = values[0]
    return text_gettext

def displayprompt(prompt):
    """layout = [[sg.Text(prompt)],
            [sg.OK()]]

    # Create the Window
    window = sg.Window('Message', layout)
    # Event Loop to process "events"
    event, values = window.Read()
    window.Close()"""
    sg.Popup(inspect.stack()[len(inspect.stack())-2].function,prompt)


def timestamp():
    """This function is supposed to return a date and time stamp in string """
    current_time = time.localtime()
    time_stamp = str(current_time.tm_mday) + "/" + str(current_time.tm_mon) + "/" + str(
        current_time.tm_year) + "    " + str(current_time.tm_hour)+":"+str(current_time.tm_min)+":"+str(current_time.tm_sec)
    displayprompt(f"funtion :: timeStamp. returned timestamp is {time_stamp}")
    return time_stamp


def writefile(nameoffile="not",text=""):
    """this simple function writes a text in a given file and then closes the
     same. The file should be in same folder"""
    if nameoffile=="not":
        event, values = sg.Window('Get filename', [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()
        nameoffile = values[0]
    if text =="":
        text = gettext("enter some text to put in file")
    currentfile = open(nameoffile,"a+")
    currentfile.write(text)
    currentfile.close()

def write_json_file(nameoffile="task.json",text={}):
    """this simple function writes a text in a given file and then closes the
     same. The file should be in same folder"""
    # try:
    
    currentfile = open(nameoffile,"a+")
    json.dump(text,currentfile)
    currentfile.close()
    # except:
    #     print('json write error')
    #     return "Error"

def createfile(nameoffile = "not"):
    """ This function will create a file. The file should be ideally in the same folder
    as the function . If the file exists then it returns content of the file in a message box
    and then also """
    if nameoffile == "not":
        while nameoffile == "not" or nameoffile == "":
            nameoffile = gettext("Please supply a valid file name")

    try:
        file = open(nameoffile,"x")
        file.close()
        return True
    except  FileExistsError :
        displayprompt("File Already Exists")
        file = open(nameoffile,"r")
        material = file.read()
        sg.PopupScrolled("Content of File", material)
        file.close()
        return True
    except FileNotFoundError:
        sg.Popup("File Not Found", "XXX")
        return False
        #this code will run no matter what. The name of file will be sent to the
        #concerned function and the function will add the name or not
        #depending on whether the name exists in the list or not.

def getdate(datestring="01/01/0001"):
    """This is a simple function which gets date in a specific format and keeps of
    prompting the user so long as date is not entered in correct format. If something is
    entered as a parameter, the function converts that string in date. If the passed string is
    incorrect, it seeks to ask for another date. If passed string is in right format then
    nothing at all. It converts and returns. if passed string is in wrong format then the
    funtion gives today's date"""
    if datestring == "01/01/0001":
        while True:
            try:
                datestring = gettext("date in dd/mm/yyyy format")
                desired_date = datetime.strptime(datestring, '%d/%m/%Y')
                return desired_date
            except :
                try:
                    desired_date = date_parser(datestring)
                    return desired_date
                except:
                    continue
    else:
        while True:
            try:
                desired_date = datetime.strptime(datestring, '%d/%m/%Y')
                return desired_date
            except:
                try:
                    desired_date = date_parser(datestring)
                    return desired_date
                except:
                    return datetime.today()
                    

def validatedate(datetimestring):

    """this function valiidates whether a string is a date in format dd/mm/yyyy.
    If yes, it returns true else, it returns
    false. """
    try:
        datefromstring = datetime.strptime(datetimestring,'%d/%m/%Y')
        displayprompt(f"function name validatedate {datetimestring} is a valid date. ")
        return True
    except:
        displayprompt(f"function name::validatedate {datetimestring} is not a valid date. ")
        return False

def check_string( chkStr ):
    """ this will check a string and return (1, 2, 3 ) depending on whether the user enters 'display' or 'abort' """
    chkStr = chkStr.strip()
    chkStr = chkStr.lower()
    if chkStr in ["abort","end","quit","quit()","bye","no","nahi","nope","not at all",
                  "n","x"] :
        return 0
    elif chkStr in ["display","open","read","yes","yup",'ha','yeah','ok','y','ye','aye']:
        return 1
    else:
        return 2


def read_text(prompt):
    '''
    Displays a prompt and reads in a string of text.
    Keyboard interrupts (CTRL+C) are ignored
    returns a string containing the string gettext by the user
    '''
    while True:  # repeat forever
        try:
            result=gettext(prompt) # read the gettext
            # if we get here no exception was raised
            # break out of the loop
            break
        except KeyboardInterrupt:
            # if we get here the user pressed CTRL+C
            displayprompt('Please enter text')
            if DEBUG_MODE:
                raise Exception('Keyboard interrupt')

    # return the result
    return result


def read_number(prompt,function):
    '''
    Displays a prompt and reads in a floating point number.
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a float containing the value gettext by the user
    '''
    while True:  # repeat forever
        try:
            number_text=read_text(prompt)
            result=function(number_text) # read the gettext
            # if we get here no exception was raised
            # break out of the loop
            break
        except ValueError:
            # if we get here the user entered an invalid number
            displayprompt('Please enter a number')

    # return the result
    return result

def read_number_ranged(prompt, function, min_value, max_value):
    '''
    Displays a prompt and reads in a number.
    min_value gives the inclusive minimum value
    max_value gives the inclusive maximum value
    Raises an exception if max and min are the wrong way round
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a number containing the value gettext by the user
    '''
    if min_value>max_value:
        # If we get here the min and the max
        # are wrong way round
        raise Exception('Min value is greater than max value')
    while True:  # repeat forever
        result=read_number(prompt,function)
        if result<min_value:
            # Value entered is too low
            displayprompt('That number is too low')
            displayprompt('Minimum value is:',min_value)
            # Repeat the number reading loop
            continue
        if result>max_value:
            # Value entered is too high
            displayprompt('That number is too high')
            displayprompt('Maximum value is:',max_value)
            # Repeat the number reading loop
            continue
        # If we get here the number is valid
        # break out of the loop
        break
    # return the result
    return result

def read_float(prompt):
    '''
    Displays a prompt and reads in a floating point number.
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a float containing the value gettext by the user
    '''
    return read_number(prompt,float)

def read_int(prompt):
    '''
    Displays a prompt and reads in an integer number.
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns an int containing the value gettext by the user
    '''
    return read_number(prompt,int)

def read_float_ranged(prompt, min_value, max_value):
    '''
    Displays a prompt and reads in a floating point number.
    min_value gives the inclusive minimum value
    max_value gives the inclusive maximum value
    Raises an exception if max and min are the wrong way round
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a number containing the value gettext by the user
    '''
    return read_number_ranged(prompt,float,min_value,max_value)

def read_int_ranged(prompt, min_value, max_value):
    '''
    Displays a prompt and reads in an integer point number.
    min_value gives the inclusive minimum value
    max_value gives the inclusive maximum value
    Raises an exception if max and min are the wrong way round
    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a number containing the value gettext by the user
    '''
    return read_number_ranged(prompt,int,min_value,max_value)
