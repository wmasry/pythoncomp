#!/usr/bin/python3.6

'''
print pcol 1,2,3 "wael moustafa elmasry";
'''

from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # pcol
        self.lexer.add('PCOL', r'pcol')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Words
        self.lexer.add('WORD', r'\w+')         

        '''
	# Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        '''
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()