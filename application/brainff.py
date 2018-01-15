"""
Brainfuck time!

This module contains a single function, "fuck", that does the work.
"""

# Copyright (C) 2017-2018 kenny2github All rights reserved.
# Under MIT License, https://github.com/Kenny2github/brainfuck-fuck

'''
MIT License

Copyright (c) 2018 Ken Hilton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import time

from .getch import getch

if sys.version_info.major < 3:
    CFA = unichr
else:
    CFA = chr

def fuck(raw_program):
    """Fuck the brain! :DDD"""
    prog = ''.join([c for c in raw_program if (c in [
        ',', '.', '[', ']', '<', '>', '+', '-',
        '=', '?', ':', '!', '@', '|', '^',
        ] or raw_program[raw_program.index(c)-1] in ['=', '@', '^'])])

    prog = ''.join(prog)
    cells = [0]
    cell = 0
    pos = 0
    cond = []
    lvl = 0
    funcs = {}
    func = False
    start = time.time()

    while pos < len(prog):
        if prog[pos] == '+':
            cells[cell] += 1
        elif prog[pos] == '-':
            cells[cell] -= 1
        elif prog[pos] == '>':
            cell += 1
            if len(cells) <= cell:
                cells.append(0)
        elif prog[pos] == '<':
            cell -= 1
        elif prog[pos] == '.':
            sys.stdout.write(CFA(cells[cell]))
            sys.stdout.flush()
        elif prog[pos] == ',':
            cells[cell] = ord(getch())
        elif prog[pos] == '[':
            if cells[cell] == 0:
                inc = 0
                pos += 1
                while prog[pos] != ']' or inc > 0:
                    if prog[pos] == '[':
                        inc += 1
                    if prog[pos] == ']':
                        inc -= 1
                    pos += 1
                pos -= 1
        elif prog[pos] == ']':
            if cells[cell] != 0:
                inc = 0
                pos -= 1
                while prog[pos] != '[' or inc > 0:
                    if prog[pos] == ']':
                        inc += 1
                    if prog[pos] == '[':
                        inc -= 1
                    pos -= 1
                pos -= 1
        elif prog[pos] == '=':
            pos += 1
            cells[cell] = ord(prog[pos])
        elif prog[pos] == '?':
            if cells[cell] == 0:
                inc = 0
                pos += 1
                while prog[pos] != ':' or inc > 0:
                    if prog[pos] == '?':
                        inc += 1
                    if prog[pos] == '!':
                        inc -= 1
                    pos += 1
                pos -= 1
            try:
                cond[lvl] = bool(cells[cell])
            except IndexError:
                cond.append(bool(cells[cell]))
            lvl += 1
        elif prog[pos] == ':':
            if cond[lvl-1]:
                inc = 0
                pos += 1
                while prog[pos] != '!' or inc > 0:
                    if prog[pos] == '?':
                        inc += 1
                    if prog[pos] == '!':
                        inc -= 1
                    pos += 1
                pos -= 1
            else:
                try:
                    cond[lvl] = False
                except IndexError:
                    cond.append(False)
        elif prog[pos] == '!':
            lvl -= 1
        elif prog[pos] == '@':
            pos += 1
            funcs[prog[pos]] = pos
            inc = 0
            pos += 1
            while prog[pos] != '|' or inc > 0:
                if prog[pos] == '@':
                    inc += 1
                if prog[pos] == '|':
                    inc -= 1
                pos += 1
            pos -= 1
        elif prog[pos] == '^':
            pos += 1
            prev = pos
            pos = funcs[prog[pos]]
            func = True
        elif prog[pos] == '|':
            if func:
                func = False
                pos = prev
        pos += 1

    end = time.time()
    return (cells, prog, end-start)
