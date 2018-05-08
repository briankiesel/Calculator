'''
Scriptable Interpreted Computer Testing Calculator
Token.py

@author: Brian Kiesel
Due April 4, 2018
'''

class token():
    
    def __init__(self, kind, value):
        self._kind = kind
        self._value = value
        
    def string(self):
        print("Token Type: " + self._kind + ", Value: " + self._value)