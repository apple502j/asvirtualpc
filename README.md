# asvirtualpc
&lt;Work-in-Progress> Virtual PC with Python

# Credits
* Made by apple502j <https://scratch.mit.edu/users/apple502j/>
* Including own linereadw (2-clause BSD,MIT,CC BY)

# License
* GPL v2 or later
* CC BY-SA 1.0,2.0,2.5,3.0,4.0

# How to boot
Just do main.py. to quit, please push CTRL+C.

# Commands
1. license Show GPLv2
2. licenses same as license
3. credit Show credit
4. credits same as credit

# Settings
settings.json is setting.  
`   {`  
`      "user": {`  
`        "lang": "ja",`  Languages see below  
`        "name": "user"`  Username.  
`       },`  
`       "style": {`  
`        "prompt": "{nowtime} @ {user}>",`  Prompt message. You can use {nowtime},{user},{year},{month},{day},{hour},{minute},{second}.  
`        "datetime": "%Y/%m/%d %H:%M:%S"`  Python format datetime.  
`      }`  
`    }`  

# Translation
translate.json - The key is the first arg of tr().

# How to add a command
1. put like `if (regex or equal): um.func() ` in cmdline.py, def docommand()
2. put your source code in userModules.py, in a new define
