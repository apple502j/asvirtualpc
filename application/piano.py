'''
PyPiano Version 1.0 (C) 2018 apple502j

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
from platform import system as _system
from sys import exit as _exit
if _system() != "Windows":
    print("Sorry, This program doesn't work in your OS. Please use Windows!")
else:
    import winsound
    from gpltext import GPL_license
    from linereadw import linereadw
    from msvcrt import getch
    from math import log10
    
    def freq(note):
        return 440*(10**(((note-69)/12)*log10(2)))
    def yesno(s):
        if s.lower()=="yes" or s.lower()=="y" or s=="1" or s.lower()=="true":
            return True
        else:
            return False
    
    keyNote={b"a":59,b"s":60,b"e":61,b"d":62,b"r":63,b"f":64,b"g":65,b"y":66,b"h":67,b"u":68,b"j":69,b"i":70,b"k":71,b"l":72}
    
    def play(k):
        if k in keyNote:
            winsound.Beep(int(freq(keyNote[k])),500)
        
    
    print("""
    PyPiano Version 1.0 (C) 2018 apple502j
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions;
    Use your keyboard to play. Quit? Push 'p'.
    
    Anyway, play with it! Have fun!
    """)
    while True:
        key=getch()
        if key == b'p':
            if yesno(input("Do you really want to quit? (Yes/No)>")):
                break
        play(key)
 
