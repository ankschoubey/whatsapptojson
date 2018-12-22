import helper
from functools import lru_cache
import re
import sys
from pprint import pprint
import constants
import json


class WhatappToJson(object):

    def __init__(self):
        pass

    @staticmethod
    def get_device_specific_metas(device: str):
        return constants.devices[device]['delimeter_format'], constants.devices[device]['attachment_tag'], constants.devices[device]['attachment_delimeters']

    @staticmethod
    def format(text: str, device: str = 'iphone'):
        delimiter_format, attachment_format, attachment_delimiters = WhatappToJson.get_device_specific_metas(
            device=device)
        
        participants = set()
        attachment_extensions = set()

        output = []
        for i in text.split('\n'):
            splitted = re.split(delimiter_format, i)

            if len(splitted) == 1:  # Continuation of last message
                output[-1]['message'] += '\n'+i
                continue

            line = {
                'date': splitted[0],
                'sender': splitted[1],
                'message': ''.join(splitted[2:]),
                'type': 'conversation'
            }

            try:
                line['date'] = helper.get_date(
                    line['date'], device).strftime(constants.devices['iphone']['date_format'])
            except:  # if not in date format then it is continuation of last message
                output[-1]['message'] += '\n'+i
                continue
                
            if len(splitted) == 2 and line['message'] == '':  # Whatsapp Meta
                line['message'] = line['sender']
                del line['sender']
                line['type'] = 'whatsapp meta'
            elif line['message'].endswith(attachment_format):
                file_name, * \
                    meta = re.split(attachment_delimiters,
                                    line['message'])[:-1]
                extention = file_name[file_name.rfind('.')+1:].strip()
                line['type'] = 'attachment'
                line['message'] = ''
                line['attachment'] = {
                    'file_name': file_name,
                    'meta': '' if len(meta) == 0 else meta[0],
                    'extention': extention
                }
                attachment_extensions.add(extention)

            sender = line.get('sender', False)

            if sender:
                participants.add(sender)
            output.append(line)

        return {
            'device': device,
            'attachment_extensions': list(attachment_extensions),
            'participants': list(participants),
            'chats': output
        }

    @staticmethod
    def formatFile(source: str, destination: str = None, device: str = 'iphone'):
        text = ''
        with open(source) as f:
            text = f.read()

        output = WhatappToJson.format(text, device=device)

        if destination is not None:
            with open(destination, 'w') as file:
                file.write(json.dumps(output, ensure_ascii=False, indent=2))
        return output

if __name__ == "__main__":
    for i in sys.argv[1:]:
        output = WhatappToJson().formatFile(
            source=i, destination='temp.json', device='iphone')

        pprint(output)
