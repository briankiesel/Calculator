'''
Scriptable Interpreted Computer Testing Calculator
Scanner.py

@author: Brian Kiesel
Due April 4, 2018
'''

import string
import Token

'''
each array holds the characters that should be labeled under each name
'''
keyword = ["begin", "do", "end", "false", "halt", "if", "print", "program", "then", "true", "var", "while"]
arithOp = ["+", "-", "*", "/", "%"]
relOp = ["=", "!=", "<", "<=", ">", ">="]
assignOp = [":="]
punc = [":", ";", ".", ","]
openParen = ["("]  # separates open and close parenthesis as their own types as done in the class example
closeParen = [")"]
mult = ["!", ":", "<", ">"]  # holds the first character of characters that could have 2 labels
tokenTypes = list(keyword + arithOp + relOp + assignOp + punc + openParen + closeParen)  # labels all token types under one name to make a later reference easier


'''
checks what kind of token each character is and then assigns it to the correct token type
'''
def tokenize(characters):
    tokenlist = []

    x = 0;
    while x < len(characters):
        if characters[x] in string.ascii_letters:
            word = ""
            while True:
                word += characters[x]
                if characters[x+1] not in string.ascii_letters:
                    break
                else:
                    x += 1
                    
            if word.lower() in keyword:
                tokenlist.append(Token.token("Keyword", word))
            else:
                tokenlist.append(Token.token("Variable", word))
    
        if characters[x] in string.digits:
            number = ""
            while True:
                number += str(characters[x])
                if characters[x+1] not in string.digits:
                    break
                else:
                    x += 1

            tokenlist.append(Token.token("Number", number))

        if characters[x] in mult:
            if characters[x] == "!" and characters[x+1] == "=":
                tokenlist.append(Token.token("Relational Operator", "!="))
                x += 2
                continue
            
            if characters[x] == ":" and characters[x+1] == "=":
                tokenlist.append(Token.token("Assignment Operator", ":="))
                x += 2
                continue
            elif characters[x] == ":":
                tokenlist.append(Token.token("Punctuation", characters[x]))
                x += 1
                continue
                
            if characters[x] == "<" and characters[x+1] == "=":
                tokenlist.append(Token.token("Relational Operator", "<="))
                x += 2
                continue
            elif characters[x] == "<":
                tokenlist.append(Token.token("Relational Operator", characters[x]))
                x += 1
                continue
            
            if characters[x] == ">" and characters[x+1] == "=":
                tokenlist.append(Token.token("Relational Operator", ">="))
                x += 2
                continue
            elif characters[x] == ">":
                tokenlist.append(Token.token("Relational Operator", characters[x]))
                x += 1
                continue
                
        if characters[x] in arithOp:
            tokenlist.append(Token.token("Arithmetic Operator", characters[x]))
            x += 1
            continue
        
        if characters[x] in relOp:
            tokenlist.append(Token.token("Relational Operator", characters[x]))
            x += 1
            continue
        
        if characters[x] in punc and characters[x] not in mult:
            tokenlist.append(Token.token("Punctuation", characters[x]))
            x += 1
            continue
        
        if characters[x] in openParen:
            tokenlist.append(Token.token("Open Parenthesis", characters[x]))
            x += 1
            continue
        
        if characters[x] in closeParen:
            tokenlist.append(Token.token("Close Parenthesis", characters[x]))
            x += 1
            continue
        
        x += 1 

    return tokenlist


'''
opens specified file and runs tokenize(); also ignores whitespce and comments in the file
'''
def scanner(userFile):
    comment = False
    chars = []

    with open(userFile) as file:
        for line in file:
            for ch in line:
                if ch in string.whitespace:
                    continue
                
                if ch == "#":
                    comment = not comment
                    continue

                if comment == True:
                    continue
                
                elif ch in tokenTypes or ch in string.ascii_letters or ch in string.digits or ch in "!":
                    chars.append(ch)
                    
                else:
                    print("Symbol " + ch + " not recognized")
                    return False
  
    return(tokenize(chars))

userFile = input("Please input the file you wish to tokenize:\n")
tokens = scanner(userFile)
'''
for i in range(0, len(tokens)):
    tokens[i].string()
originally this ^ printed out the results of the scanner but I commented it out so it wasn't printed in my parser
'''