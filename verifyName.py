import re
def check_splcharacter(test): 
    string_check= re.compile('^[a-zA-Z ]+$') 
    if(string_check.search(test) == None): 
        return True
    else: 
        return False