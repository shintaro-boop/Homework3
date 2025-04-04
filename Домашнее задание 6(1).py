number = 1
string = 'Hello'
def global_changes() :
    global nubmer
    global string
    number = 5
    string = 'Hello, dear friend'
    return print(f'number = {number} \nstring = {string}')
global_changes()