from lexer import tokens

import ply.yacc as yacc

# Definir la gramática para las declaraciones básicas de PostgreSQL

def p_statement_create_table(p):
    'statement : CREATE TABLE ID LPAREN column_definitions RPAREN'
    print("Tabla creada correctamente")

def p_column_definitions(p):
    '''column_definitions : column_definitions COMMA column_definition
                          | column_definition'''
    pass

def p_column_definition(p):
    'column_definition : ID'
    pass

def p_statement_insert(p):
    'statement : INSERT INTO ID LPAREN values RPAREN VALUES LPAREN values RPAREN'
    print("Datos insertados correctamente")

def p_values(p):
    '''values : values COMMA value
              | value'''
    pass

def p_value(p):
    '''value : ID
             | STRING'''
    pass

def p_statement_select(p):
    'statement : SELECT TIMES FROM ID'
    print("Consulta realizada correctamente")

def p_statement_update(p):
    'statement : UPDATE ID SET ID EQUALS STRING WHERE ID EQUALS NUMBER'
    print("Datos actualizados correctamente")

def p_statement_delete(p):
    'statement : DELETE FROM ID WHERE ID EQUALS NUMBER'
    print("Datos eliminados correctamente")

def p_error(p):
    print(f"Error de sintaxis en '{p.value}'")

# Construir el analizador sintáctico
parser = yacc.yacc()

# Función para analizar una entrada
def parse_input(input_string):
    parser.parse(input_string)

# Ejemplos de uso
if __name__ == "__main__":
    inputs = [
        "CREATE TABLE users (id, name);",
        "INSERT INTO users (id, name) VALUES (1, 'John');",
        "SELECT * FROM users;",
        "UPDATE users SET name = 'John' WHERE id = 1;",
        "DELETE FROM users WHERE id = 1;"
    ]

    for input_string in inputs:
        print(f"Analizando: {input_string}")
        parse_input(input_string)
        print()