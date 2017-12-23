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
import sys
import random

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
	\r''',end="")

def quit():
	print(tr("SEEYOU","See you!"))
	sys.exit()

def dice():
        random.seed()
        print(str(random.randint(1,6)) + tr("DICE"," came out."))
