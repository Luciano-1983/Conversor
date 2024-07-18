import ply.yacc as yacc
from lexer import tokens

# Definições de precedência (se necessário)
precedence = (('left', 'PLUS', 'MINUS'), ('left', 'MULT', 'DIV', 'MOD'),
              ('left', 'EQ', 'NE', 'GT',
               'LT'), ('right', 'ASSIGN', 'PLEQUAL', 'MIEQUAL', 'MTEQUAL',
                       'DIEQUAL', 'MOEQUAL'))


# Definir a estrutura da árvore sintática
def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_statement(p):
    '''statement : function_def
                 | if_statement
                 | for_statement
                 | while_statement
                 | print_statement
                 | assignment_statement'''
    p[0] = p[1]


def p_function_def(p):
    '''function_def : DEF ID LPAREN parameters RPAREN COLON block'''
    p[0] = f"function {p[2]}({p[4]}) {{\n{p[7]}}}\n"


def p_parameters(p):
    '''parameters : ID
                  | parameters COMMA ID
                  | '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + ', ' + p[3]
    else:
        p[0] = ''


def p_if_statement(p):
    '''if_statement : IF expression COLON block elif_statements else_statement'''
    p[0] = f"if ({p[2]}) {{\n{p[4]}}}{p[5]}{p[6]}\n"


def p_elif_statements(p):
    '''elif_statements : ELIF expression COLON block elif_statements
                       | '''
    if len(p) == 6:
        p[0] = f" else if ({p[2]}) {{\n{p[4]}}}{p[5]}"
    else:
        p[0] = ''


def p_else_statement(p):
    '''else_statement : ELSE COLON block
                      | '''
    if len(p) == 4:
        p[0] = f" else {{\n{p[3]}}}"
    else:
        p[0] = ''


def p_for_statement(p):
    '''for_statement : FOR ID IN RANGE LPAREN expression RPAREN COLON block'''
    p[0] = f"for (let {p[2]} = 0; {p[2]} < {p[6]}; {p[2]}++) {{\n{p[9]}}}\n"


def p_while_statement(p):
    '''while_statement : WHILE expression COLON block'''
    p[0] = f"while ({p[2]}) {{\n{p[4]}}}\n"


def p_print_statement(p):
    '''print_statement : PRINT LPAREN print_arguments RPAREN'''
    p[0] = f"console.log({p[3]});\n"


def p_print_arguments(p):
    '''print_arguments : expression
                       | print_arguments COMMA expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]


def p_assignment_statement(p):
    '''assignment_statement : ID ASSIGN expression
                            | ID PLEQUAL expression
                            | ID MIEQUAL expression
                            | ID MTEQUAL expression
                            | ID DIEQUAL expression
                            | ID MOEQUAL expression'''
    if p[2] == '=':
        p[0] = f"{p[1]} = {p[3]};\n"
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]};\n"


def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | STRING
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression EQ expression
                  | expression NE expression
                  | expression GT expression
                  | expression LT expression'''
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"


def p_block(p):
    '''block : statement
             | block statement'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_error(p):
    print(f"Erro de sintaxe: {p}")


parser = yacc.yacc()
