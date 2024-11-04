import ply.lex as lex

resultadoLex = []

# Palabras reservadas de PostgreSQL
reservadas = {
    'select': 'SELECT',
    'insert': 'INSERT',
    'update': 'UPDATE',
    'delete': 'DELETE',
    'create': 'CREATE',
    'drop': 'DROP',
    'alter': 'ALTER',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'in': 'IN',
    'is': 'IS',
    'null': 'NULL',
    'table': 'TABLE',
    'into': 'INTO',
    'values': 'VALUES',
    'set': 'SET',
    'join': 'JOIN',
    'on': 'ON',
    'as': 'AS',
    'distinct': 'DISTINCT',
    'order': 'ORDER',
    'by': 'BY',
    'group': 'GROUP',
    'having': 'HAVING',
    'limit': 'LIMIT',
    'offset': 'OFFSET',
    'union': 'UNION',
    'all': 'ALL',
    'primary': 'PRIMARY',
    'key': 'KEY',
    'foreign': 'FOREIGN',
    'references': 'REFERENCES',
    'constraint': 'CONSTRAINT',
    'check': 'CHECK',
    'default': 'DEFAULT',
    'unique': 'UNIQUE',
    'index': 'INDEX',
    'view': 'VIEW',
    'trigger': 'TRIGGER',
    'procedure': 'PROCEDURE',
    'function': 'FUNCTION',
    'begin': 'BEGIN',
    'end': 'END',
    'commit': 'COMMIT',
    'rollback': 'ROLLBACK',
    'grant': 'GRANT',
    'revoke': 'REVOKE',
    'use': 'USE',
    'database': 'DATABASE',
}

tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'CADENA',
    # Operadores
    'MAS',  # +
    'MENOS',  # -
    'MULTIPLICACION',  # *
    'DIVISION',  # /
    'MODULO',  # %
    # Operadores de comparación
    'IGUAL',        # =
    'DIFERENTE',    # <> or !=
    'MENORQUE',     # <
    'MAYORQUE',     # >
    'MENORIGUAL',   # <=
    'MAYORIGUAL',   # >=
    # Símbolos
    'PARIZQ',       # (
    'PARDER',       # )
    'COMA',         # ,
    'PUNTO',        # .
    'PUNTOCOMA',    # ;
    'DOS_PUNTOS',   # :
] + list(reservadas.values())  # Incluimos las palabras reservadas como tokens

# Reglas de expresiones regulares para tokens simples
t_MAS             = r'\+'
t_MENOS           = r'-'
t_MULTIPLICACION  = r'\*'
t_DIVISION        = r'/'
t_MODULO          = r'%'

t_IGUAL           = r'='
t_DIFERENTE       = r'<>|!='
t_MENORIGUAL      = r'<='
t_MAYORIGUAL      = r'>='
t_MENORQUE        = r'<'
t_MAYORQUE        = r'>'

t_PARIZQ          = r'\('
t_PARDER          = r'\)'
t_COMA            = r','
t_PUNTO           = r'\.'
t_PUNTOCOMA       = r';'
t_DOS_PUNTOS      = r':'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Identificadores y palabras reservadas
def t_IDENTIFICADOR(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reservadas.get(t.value.lower(), 'IDENTIFICADOR')  # Verificar palabras reservadas
    return t

# Literales de cadena
def t_CADENA(t):
    r"\'([^\\']|(\\.))*?\'"
    t.value = t.value[1:-1]  # Eliminar las comillas simples
    return t

# Números (enteros y flotantes)
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

# Identificadores entre comillas dobles
def t_IDENTIFIER_QUOTED(t):
    r'\"([^\\"]|(\\.))*?\"'
    t.type = 'IDENTIFICADOR'
    t.value = t.value[1:-1]  # Eliminar las comillas dobles
    return t

# Manejo de comentarios de una línea
def t_COMENTARIO_SIMPLE(t):
    r'--.*'
    pass  # Ignorar comentarios

# Manejo de comentarios de múltiples líneas
def t_COMENTARIO_MULTILINEA(t):
    r'/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # Ignorar comentarios

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def prueba(data):
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        # Convertir el valor del token a cadena para garantizar la serialización
        valor = str(tok.value)
        tokens.append((tok.lineno, tok.type, valor))
    return tokens
