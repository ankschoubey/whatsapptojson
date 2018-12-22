import helper
from functools import lru_cache
import re
import sys 
from pprint import pprint
class WhatappToJson(object):

    def __init__(self):
        pass
    
    @staticmethod
    def get_message_type(message):
        pass

    @staticmethod
    def format(text: str):
        
        output = []
#        for i in [line for line in text.split('\n') if len(line.strip()) != 0]:

        for i in text.split('\n'):
            splitted  = re.split(']|: ',i)

            if len(splitted) == 1: #Continuation of last message
                output[-1]['message']+='\n'+i
                continue


            line = {
                'date': splitted[0],
                'sender': splitted[1],
                'message': ''.join(splitted[2:]),
                'type': 'conversation'
            }     

            try:
                line['date'] = helper.get_date(line['date']) #
            except: #if not in date format then it is continuation of last message
                output[-1]['message']+='\n'+i
                continue

            if len(splitted) == 2 and line['message'] == '': #Whatsapp Meta
                line['message'] = line['sender']
                del line['sender']
                line['type'] = 'whatsapp meta'
            elif line['message'].endswith('<\u200eattached>'):
                file_name, *meta = re.split(' • ‎| <\u200eattached>',line['message'])[:-1]
                extention = file_name[file_name.rfind('.')+1:]
                line['type'] = 'attachment'
                line['attachment'] = {
                    'file_name': file_name,
                    'meta': '' if len(meta) == 0 else meta[0],
                    'extention': extention
                }
                del line['message'] 

            output.append(line)

        return output
    
    @staticmethod
    def formatFile(source: str, destination: str = None):
        text = ''
        with open(source) as f:
            text = f.read()

        output = WhatappToJson.format(text)

        if destination is None:
            return output
        
        with open(destination,'w') as file:
            file.write(output)

if __name__ == "__main__":
    for i in sys.argv[1:]:
        output = WhatappToJson().formatFile(source=i)
        
        pprint(output)
    

    pass