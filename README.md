# Whatsapp-Text-To-Json-Converter

Converts Whatsapp chat files to dictionary or JSON format.

**Works with exports from iPhone and Android. Be sure to mention device.**

# Arg Parser

```
usage: WhatsappJsonParser.py [-h] -f FILE -d DEVICE [-s SAVE] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  chat text file
  -d DEVICE, --device DEVICE
                        can be 'iphone' or 'android'
  -s SAVE, --save SAVE  path of file/direction to save json, 'default' would
                        be same as text file name in same directory
  -v, --verbose         Verbose (Print output)
```


# Usage

## Converting Text to Dict

```python
output = WhatsappToJson().format(text = 'string with complete chat data', device = 'android'`)
```

## Converting Whatsapp File to dictionary.
```python
output = WhatappToJson().formatFile(source='source_file_path', device = 'iphone')
```

## Exporting Whatsapp File to Json.

```python
WhatappToJson().formatFile(source='source_file_path', destination='destination_path.json', device = 'android')
```

# Sample Export

```json
{
  "attachment_extensions": [
    "pdf",
    "mp4",
    "jpg"
  ],
  "participants": [
    "sender name 1",
    "sender name 2",
    "sender name n"
  ],
  "chats": [
    {
      "date": "25/03/16 07:03:45 PM",
      "message": "‎Messages to this group are now secured with end-to-end encryption.",
      "type": "whatsapp meta"
    },
     {
      "date": "15/08/17 12:27:34 PM",
      "sender": "sender name",
      "type": "attachment",
      "attachment": {
        "file_name": "file_name_with.pdf",
        "meta": "8 pages",
        "extention": "pdf"
      }
    },  {
      "date": "15/08/17 01:37:28 PM",
      "sender": "sender name",
      "message": "message",
      "type": "conversation"
    },
    ...
    ]
}
 ```
Each item in chats could have type of "whatsapp meta" or "attachment" or "conversation".
