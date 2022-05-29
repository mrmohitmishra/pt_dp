import os
def initialize():
    if os.path.exists('requirements.txt'):
        os.system("pip install -r requirements.txt")

if __name__ == '__main__':
    initialize()