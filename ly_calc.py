import sys
sys.path.insert(0, "../..")

import ply.lex as lex
import ply.yacc as yacc
import tac
import argparse

reserved = {
    'int':'INT', 'float':'FLOAT', 'print':'PRINT', 'boolean':'BOOLEAN',
    'true':'TRUE', 'false':'FALSE', 'if':'IF'
}

tokens = tuple(reserved.values()) + (
    'NAME', 'INUM', 'FNUM',
    'EQUAL', 'NEQUAL', 'GREATER', 'LESS', 'GEQUAL', 'LEQUAL',
    'AND', 'OR'
)

literals = ['=', '+', '-', '*', '/', '^', '(', ')', '{', '}', ';']

t_ignore = ' \t'

t_EQUAL = r'=='
t_NEQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GEQUAL = r'>='
t_LEQUAL = r'<='
t_AND = r'&&'
t_OR = r'\|\|'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_FNUM(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

precedence = (
    ('left', 'AND', 'OR'),
    ('nonassoc', 'LEQUAL', 'GEQUAL', 'EQUAL', 'NEQUAL', 'GREATER', 'LESS'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('left', '^'),
    ('right', 'UMINUS'),
)

abstractTree = {}
names=[]

def p_init(p):
    '''init : statement'''
    global abstractTree
    abstractTree = p[1]


def p_statement(p):
    '''statement : declarations ";" statement
                 | print ";" statement
                 | if_statement statement
                 | empty'''
    if len(p) > 2:  # not empty
        if len(p) == 3:
            p[2] = p[3]
        p[0] = (p[1], ) + p[3]
    else:
        p[0] = ()

def p_empty(p):
    'empty :'
    pass

def p_if_statement(p):
    '''if_statement : IF "(" expression ")" "{" statement "}" '''
    p[0] = ('if', p[3], p[6])

def p_type_specifier(p):
    '''type : INT
            | FLOAT
            | BOOLEAN'''
    p[0] = p[1]


def p_declarations(p):
    '''declarations  : declaration_type_name
                     | declaration_assign_expression
                     | declaration_full'''
    p[0] = p[1]

def p_declaration_type_name(p):
    '''declaration_type_name : type NAME'''
    p[0] = ('declare', p[1], p[2])
    names.append({"type": p[1],"value": p[2] if p[2] is None else 0})

def p_declaration_assign_expression(p):
    '''declaration_assign_expression : NAME "=" expression'''
    p[0] = ('assign', p[1], p[3])

def p_declaration_full(p):
    '''declaration_full : type NAME "=" expression'''
    p[0] = ('declare_assign', p[1], p[2], p[4])

def p_print(p):
    'print : PRINT expression'
    p[0] = ('print', p[2])
    print

def p_expression_binop(p):
    '''expression : expression "+" expression
                  | expression "-" expression
                  | expression "*" expression
                  | expression "/" expression
                  | expression "^" expression
                  | expression EQUAL expression
                  | expression NEQUAL expression
                  | expression GEQUAL expression
                  | expression LEQUAL expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression OR expression
                  | expression AND expression'''
    p[0] = ('operation', p[1], p[2], p[3])

def p_expression_uminus(p):
    'expression : "-" expression %prec UMINUS'
    p[0] = -p[2]


def p_direct_declarator(p):
    'expression : "(" expression ")"'
    p[0] = p[2]


def p_expression_number(p):
    '''expression : INUM
                  | FNUM
                  | BOOLVAL'''
    p[0] = p[1]

def p_expression_name(p):
    "expression : NAME"
    p[0] = p[1]

def p_boolean(p):
    '''BOOLVAL : TRUE
               | FALSE'''
    if p[1] == "true":
        p[0] = True
    elif p[1] == "false":
        p[0] = False

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

yacc.yacc()

# Main

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument('filename', type=argparse.FileType('r'), help="File to Compile")
    args = parse.parse_args()

    if args.filename is not None:

        f = open(args.filename.name)
        r = f.read()
        f.close()
        yacc.parse(r)
        w = open('Tree.txt','w')
        for node in abstractTree:
            w.write(str(node)+'\n')
        
        try:
            for node in abstractTree:
                tac.threeAddressCode(node)
        except:
            print ("Error trying to compile Three Address Code")

        w.close()

    else:
        print(args.filename)

if __name__ == '__main__':
    main()