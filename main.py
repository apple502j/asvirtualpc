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

import datetime
import json
from cmdlist import docommand
from tr import begintr,tr

cmd="";

def defaultset():
	filename="settings.json"
	with open(filename,"r") as fp:
		global settings
		settings = json.load(fp)


try:
	defaultset()
	begintr()
	print(tr("ASVPC","AS Virtual PC"))
	while True:
		ndo=datetime.datetime.now()
		now=ndo.strftime(settings["style"]["datetime"])
		cmd=input(str(settings["style"]["prompt"]).format(nowtime=now,user=settings["user"]["name"],year=ndo.year,month=ndo.month,day=ndo.day,hour=ndo.hour,minute=ndo.minute,second=ndo.second))
		docommand(cmd)
		
		
except KeyboardInterrupt:
	print(tr("SEEYOU","\nSee you!"))

