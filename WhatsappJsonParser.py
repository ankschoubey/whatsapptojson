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
    def format(text: str):

        participants = set()
        attachment_extensions = set()

        output = []
        for i in text.split('\n'):
            splitted = re.split(']|: ', i)

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
                    line['date']).strftime(constants.DATE_FORMAT)
            except:  # if not in date format then it is continuation of last message
                output[-1]['message'] += '\n'+i
                continue

            if len(splitted) == 2 and line['message'] == '':  # Whatsapp Meta
                line['message'] = line['sender']
                del line['sender']
                line['type'] = 'whatsapp meta'
            elif line['message'].endswith('<\u200eattached>'):
                file_name, * \
                    meta = re.split(' • ‎| <\u200eattached>',
                                    line['message'])[:-1]
                extention = file_name[file_name.rfind('.')+1:]
                line['type'] = 'attachment'
                line['attachment'] = {
                    'file_name': file_name,
                    'meta': '' if len(meta) == 0 else meta[0],
                    'extention': extention
                }
                attachment_extensions.add(extention)
                del line['message']

            sender = line.get('sender',False)

            if sender:
                participants.add(sender)
            output.append(line)

        return {
            'attachment_extensions': list(attachment_extensions),
            'participants': list(participants),
            'chats': output
            }

    @staticmethod
    def formatFile(source: str, destination: str = None):
        text = ''
        with open(source) as f:
            text = f.read()

        output = WhatappToJson.format(text)

        if destination is None:
            return output

        with open(destination, 'w') as file:
            
            file.write(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    for i in sys.argv[1:]:
        output = WhatappToJson().formatFile(source=i, destination='temp.json')

        pprint(output)