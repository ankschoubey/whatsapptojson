from datetime import datetime

from .constants import devices

def get_date(string, device_type='iphone'):
    DATE_FORMAT = devices[device_type]['date_format']
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
    print(get_date(date, 'iphone'))

    date = '12/15/18, 11:28 AM'
    print(get_date(date, 'android'))

    date = '12/15/18, 11:28'
    print(get_date(date, 'android_24'))

    date = '20/07/16, 4:51:01 PM'
    print(get_date(date, 'iphone'))

    date = '20/07/16, 4:51:01'
    print(get_date(date, 'iphone_24'))
