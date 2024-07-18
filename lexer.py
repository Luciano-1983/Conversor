import ply.lex as lex

# Lista de nomes de tokens
reserved = {
    'def': 'DEF',
    'if': 'IF',
    'elif': 'ELIF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'while': 'WHILE',
    'print': 'PRINT',
    'range': 'RANGE',
}

tokens = ('ID', 'NUMBER', 'STRING', 'DEF', 'IF', 'ELIF', 'ELSE', 'FOR', 'IN',
          'WHILE', 'PRINT', 'RANGE', 'LPAREN', 'RPAREN', 'COLON', 'COMMA',
          'ASSIGN', 'EQ', 'NE', 'GT', 'LT', 'PLUS', 'MINUS', 'MULT', 'DIV',
          'PLEQUAL', 'MIEQUAL', 'MTEQUAL', 'DIEQUAL', 'MOEQUAL', 'DBEQUAL',
          'NEQUAL', 'DBPLUS', 'DBMINUS', 'MOD') + tuple(reserved.values())

# Regras simples para tokens de palavras-chave
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_LT = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PLEQUAL = r'\+='
t_MIEQUAL = r'-='
t_MTEQUAL = r'\*='
t_DIEQUAL = r'/='
t_MOEQUAL = r'%='
t_DBEQUAL = r'=='
t_NEQUAL = r'!='
t_DBPLUS = r'\+\+'
t_DBMINUS = r'--'
t_MOD = r'%'


# Regras para tokens de identificadores, números e strings
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_DEF(t):
    r'def'
    t.type = reserved.get(t.value, 'DEF')
    return t


def t_IF(t):
    r'if'
    t.type = reserved.get(t.value, 'IF')
    return t


def t_ELIF(t):
    r'elif'
    t.type = reserved.get(t.value, 'ELIF')
    return t


def t_ELSE(t):
    r'else'
    t.type = reserved.get(t.value, 'ELSE')
    return t


def t_FOR(t):
    r'for'
    t.type = reserved.get(t.value, 'FOR')
    return t


def t_IN(t):
    r'in'
    t.type = reserved.get(t.value, 'IN')
    return t


def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value, 'WHILE')
    return t


def t_PRINT(t):
    r'print'
    t.type = reserved.get(t.value, 'PRINT')
    return t


def t_RANGE(t):
    r'range'
    t.type = reserved.get(t.value, 'RANGE')
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\"]|\\.)*\"'
    t.value = t.value
    #t.value = t.value[1:-1]
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere não reconhecido: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()
