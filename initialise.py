import os
from pathlib import Path
def initialize():
    if os.path.exists('requirements.txt'):
        os.system("pip install -r requirements.txt")
    if os.path.exists('requirements.txt'):
        pathrequirementfile = Path('requirements.txt')
        Path.unlink(pathrequirementfile)
        os.system('pip freeze > requirements.txt')
    if os.path.exists('practice.csv'):
        pathtaskfile = Path('practice.csv')
        Path.unlink(pathtaskfile)
    if os.path.exists('property_tax.csv'):
        pathtaskfile = Path('property_tax.csv')
        Path.unlink(pathtaskfile)
    if os.path.exists('property_tax.txt'):
        pathtaskfile = Path('property_tax.txt')
        Path.unlink(pathtaskfile)       
    if not os.path.exists('requirement.txt'):
        os.system('pip freeze > requirements.txt')
    

if __name__ == '__main__':
    initialize()