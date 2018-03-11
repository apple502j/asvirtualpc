'''
    Copyright (C) 2017  apple502j

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

'''
    You can also use this program and/or screenshots under CC BY-SA 1.0,
    2.0,2.5,3.0,4.0 or later.

    http://creativecommons.org/licenses/by-sa/1.0/
    http://creativecommons.org/licenses/by-sa/2.0/
    http://creativecommons.org/licenses/by-sa/2.5/
    http://creativecommons.org/licenses/by-sa/3.0/
    http://creativecommons.org/licenses/by-sa/4.0/

'''

# This is a module called from main.py.

from gpltext import GPL_license
from linereadw import linereadw
from tr import tr
from importlib import reload
import sys
import random
import json
import os
import platform
import application.brainff as _brainff

global settings

global pypianoload
pypianoload=0

def defaultset():
	filename="settings.json"
	with open(filename,"r") as fp:
		global settings
		settings = json.load(fp)

def license():
	linereadw(GPL_license,20)
	

def credits():
	print('''
	AS Virtual PC (C)2017 apple502j
	This program is licensed under
	GPLv2 or any later version.
	To see the license, do "license".
	
	This program is also licensed
	under CC BY-SA 1.0,2.0,2.5,3.0,4.0.
	
	Library linereadw is made by apple502j.
	(MIT,2-clause-BSD,CC BY 1.0,2.0,2.5,3.0,4.0)

	PyPiano is made by apple502j.
	(GPLv3-or-later)

	Brainduck-duck(d to f) by Kenny2github under MIT License
	(C) 2017-2018 Kenny2github All rights reserved.

	Getch by ActiveState under Python Software License
	(C) 2017 ActiveState All rights reserved.

	See all credits in CREDITS.
	\r''',end="")

def quit():
	print(tr("SEEYOU","See you!"))
	sys.exit()

def dice():
	random.seed()
	print(str(random.randint(1,6)) + tr("DICE"," came out."))

def whatIsTheNumber():
	try:
		random.seed()
		num = random.randint(1,1000)
		print(tr("WITN_BEGIN","What is the number?(from 1 to 1000)"))
		n=0
		while True:
			n+=1
			b=""
			if n!=1:
				b="s"
			answer=int(input(tr("WITN_INPUT","({a} time{s})Number >").format(a=n,s=b)))
			if answer == num:
				print(tr("WITN_CORRECT","Correct!"))
				break
			elif answer > num:
				print(tr("WITN_BIG","That's big."))
			else:
				print(tr("WITN_SMALL","That's small."))
	
	except KeyboardInterrupt:
		print(tr("WITN_CLOSED","The number is {a}. See you!").format(a=num))
	except:
		pass

def brainduck():
        # Be "duck".
	try:
		while True:
			_brainff.fuck(input("Brainduck >"))
	except KeyboardInterrupt:
		print("")
	except:
		print(tr("BRAIN_ERR","Something wrong happened, so Brainduck was crashed."))

def pypiano():
	global pypianoload
	if pypianoload==0:
		import application.piano as piano
		pypianoload=1
	else:
		reload(piano)

def sysinfo():
	defaultset()
	print(str(tr('SYSINFO_OS','Your OS:\t {0}\n') +
	tr('SYSINFO_LOCATION','ASVirtualPC Location:\t {1}\n')+
	tr('SYSINFO_PCNAME','Computer Name:\t {2}\n\n')+
	tr('SYSINFO_USERNAME','Your Userame:\t {3}\n')+
	tr('SYSINFO_LANG','Your Language:\t {4}\n\n')+
	tr('SYSINFO_PYTHONVER','Pyhon Version:\t {5}')).format(
		platform.system(),
		os.getcwd(),
		platform.node(),
		settings.get("user",{"name":""}).get("name",""),
                settings.get("user",{"lang":""}).get("lang",""),
		platform.python_version()
	))
