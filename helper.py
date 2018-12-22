from datetime import datetime
from constants import DATE_FORMAT

def get_date(string):
    if len(string.strip()) == 0:
        return None

    string = string.replace('[','').replace(']','').replace(',','')
    if string.index('/')==1:
        string = '0'+string

    try:
        return datetime.strptime(string, DATE_FORMAT)
    except:
        return None

if __name__ == "__main__":
    date = '[2/11/17, 10:59:41 AM]'
    print(get_date(date))