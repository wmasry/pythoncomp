#!/usr/bin/python3.6

'''
print pcol 1,2,3 "wael moustafa elmasry";
'''

from rply import ParserGenerator
#from ast import Number, Sum, Sub, Print
from ast import Number, Print, Word


class Parser():
    
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'PCOL', 'SEMI_COLON', 'WORD']
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT PCOL expression SEMI_COLON')

        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])


        @self.pg.production('expression : NUMBER expression')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.production('expression : WORD')
        def word(p):
            return Word(self.builder, self.module, p[0].value)


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
