import ply.lex as lex

# Lista de palabras reservadas en PostgreSQL
reserved = {
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'create': 'CREATE',
    'drop': 'DROP',
    'table': 'TABLE',
    'database': 'DATABASE',
    'from': 'FROM',
    'where': 'WHERE',
    'into': 'INTO',
    'values': 'VALUES',
    'set': 'SET',
    'and': 'AND',
    'or': 'OR',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE'
}

# Tokens
tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'DOT',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'ID',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_THAN_EQUAL',
    'GREATER_THAN_EQUAL',
    'EQUAL_EQUAL',
    'NOT_EQUAL'
] + list(reserved.values())

# Reglas para expresiones regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUAL = r'<='
t_GREATER_THAN_EQUAL = r'>='
t_EQUAL_EQUAL = r'=='
t_NOT_EQUAL = r'!='

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Definir la expresión regular para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Definir la expresión regular para cadenas
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Definir identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')  # Verificar si es palabra reservada
    return t

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Inicializar el analizador léxico
lexer = lex.lex()

# Función para reiniciar el contador de líneas
def reset_lexer():
    lexer.lineno = 1