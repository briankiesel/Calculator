'''
Scriptable Interpreted Computer Testing Calculator
Parser.py

@author: Brian Kiesel
Due April 18, 2018
'''

tokens = None
token = None

def globalX(tokenlist):
        global tokens
        global token
        
        tokens = tokenlist
        token = tokens[0]
        
def match(expected):
    global token
    global tokens
    if token._kind == expected:
        tokens.pop(0)
        
        if len(tokens) != 0:
            token = tokens[0]
        else:
            print("Empty")
        return True
    else:
        print("Expected:", expected, ", but got:", token._kind)
        return False
    
def match2(expected):
    global token
    global tokens
    if token._value == expected:
        tokens.pop(0)
        
        if len(tokens) != 0:
            token = tokens[0]
        return True
    else:
        print("Expected:", expected, ", but got:", token._value)
        return False
    
def match3(expected):
    global token
    global tokens
    if expected in token._kind:
        tokens.pop(0)
        
        if len(tokens) != 0:
            token = tokens[0]
        return True
    else:
        print("Expected:", expected, ", but got:", token._kind)
        return False

def header():
    return match2("program") and match2(":") and match("Variable") and match2(";") and declarations()

def declarations():
        return match2("var") and match2(":") and idlist() and match2(";")

def idlist():
        return match("Variable") and idlist2()
    
def idlist2():
    global token
    
    if token._value == ",":
        match2(",")
        return idlist()
    #elif token._value == ";":
        #match2(";")
        #return True
    else:
        return True

def body():
    return match2("begin") and match2(":") and statement_list() and match2("halt") and match2(".")

def statement_list():

    if statement():
        return statement_list()
    else:
        return True

def statement():
    global token
    
    if token._kind == "Variable":
        return match("Variable") and match2(":=") and expr() and match2(";")
    elif token._value == "print":
        return match2("print") and match2(":") and match("Variable") and match2(";")
    elif token._value == "if":
        return match2("if") and match2(":") and expr() and match2(",") and match2("then") and match2(":") and statement_list() and match2("end") and match2(".")
    elif token._value == "while":
        return match2("while") and match2(":") and expr() and match2(",") and match2("do") and match2(":") and statement_list() and match2("end") and match2(".")
    else:
        return False

def expr():
    global token
    
    if token._kind == "Variable":
        return match("Variable")
    elif token._kind == "Number":
        return match("Number")
    elif token._kind == "relOp":
        return match("relOp")
    elif token._kind == "openParen":
        return match("openParen") and expr() and match3("tokenTypes") and expr() and match("closeParen")
    else:
        print("*Error*")
        return False

def parse(t):
    globalX(t)

    return header() and body()