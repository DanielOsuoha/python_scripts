import os

def file_exists():
    if os.path.exists('test.txt'):
        os.remove('test.txt')
    else:
        print("The path does not exist")
    
def check_modification(file):
    import datetime
    timestamp = os.path.getmtime(file)
    print(datetime.datetime.fromtimestamp(timestamp))
    
check_modification('organize.py')


def check_size_type(file):
    if os.path.isfile(file):
        print("The object passed is a file")
        print('The size of the file:', os.path.getsize(file))
    else:
        print("The object is not a file")