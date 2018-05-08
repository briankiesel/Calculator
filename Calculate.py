'''
Created on May 8, 2018

@author: csam
'''

from SICTC import Scanner
from SICTC import Parser

tokens = Scanner.scanner(Scanner.userFile)
parsed = Parser.parse(tokens)
print("Correct:", parsed)