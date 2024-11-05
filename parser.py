# parser.py
import ply.yacc as yacc
from lexer import tokens

# Lista para almacenar errores de sintaxis
syntax_errors = []

# Precedencia de operadores (si es necesario)
precedence = (
    ('left', 'AND', 'OR'),
    ('nonassoc', 'IGUAL', 'DIFERENTE', 'MENORQUE', 'MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
)

# Definición de la gramática

def p_inicio(p):
    '''inicio : sentencias'''
    p[0] = p[1]

def p_sentencias(p):
    '''sentencias : sentencias sentencia PUNTOCOMA
                  | sentencia PUNTOCOMA
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_sentencia(p):
    '''sentencia : crear_base_datos
                 | usar_base_datos
                 | crear_tabla
                 | insertar_datos
                 | consulta_select
                 | actualizar_datos
                 | eliminar_datos
    '''
    p[0] = p[1]

def p_crear_base_datos(p):
    'crear_base_datos : CREATE DATABASE IDENTIFICADOR'
    p[0] = ('CREATE_DATABASE', p[3])

def p_usar_base_datos(p):
    'usar_base_datos : USE IDENTIFICADOR'
    p[0] = ('USE_DATABASE', p[2])

def p_crear_tabla(p):
    'crear_tabla : CREATE TABLE IDENTIFICADOR PARIZQ definicion_columnas PARDER'
    p[0] = ('CREATE_TABLE', p[3], p[5])

def p_definicion_columnas(p):
    '''definicion_columnas : definicion_columnas COMA definicion_columna
                           | definicion_columna
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_definicion_columna(p):
    'definicion_columna : IDENTIFICADOR tipo_dato'
    p[0] = (p[1], p[2])

def p_tipo_dato(p):
    '''tipo_dato : IDENTIFICADOR'''
    p[0] = p[1]

def p_insertar_datos(p):
    'insertar_datos : INSERT INTO IDENTIFICADOR PARIZQ lista_columnas PARDER VALUES PARIZQ lista_valores PARDER'
    p[0] = ('INSERT_INTO', p[3], p[5], p[9])

def p_lista_columnas(p):
    '''lista_columnas : lista_columnas COMA IDENTIFICADOR
                      | IDENTIFICADOR
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_lista_valores(p):
    '''lista_valores : lista_valores COMA valor
                     | valor
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_valor(p):
    '''valor : NUMERO
             | CADENA
             | NULL
    '''
    p[0] = p[1]

def p_consulta_select(p):
    'consulta_select : SELECT lista_seleccion FROM IDENTIFICADOR'
    p[0] = ('SELECT', p[2], p[4])

def p_lista_seleccion(p):
    '''lista_seleccion : MULTIPLICACION
                       | lista_columnas
    '''
    p[0] = p[1]

def p_actualizar_datos(p):
    'actualizar_datos : UPDATE IDENTIFICADOR SET asignaciones where_clause'
    p[0] = ('UPDATE', p[2], p[4], p[5])

def p_asignaciones(p):
    '''asignaciones : asignaciones COMA asignacion
                    | asignacion
    '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_asignacion(p):
    'asignacion : IDENTIFICADOR IGUAL valor'
    p[0] = (p[1], p[3])

def p_eliminar_datos(p):
    'eliminar_datos : DELETE FROM IDENTIFICADOR where_clause'
    p[0] = ('DELETE', p[3], p[4])

def p_where_clause(p):
    '''where_clause : WHERE condicion
                    | empty
    '''
    p[0] = p[2] if len(p) > 2 else None

def p_condicion(p):
    '''condicion : expresion'''
    p[0] = p[1]

def p_expresion(p):
    '''expresion : valor operador valor'''
    p[0] = (p[2], p[1], p[3])

def p_operador(p):
    '''operador : IGUAL
                | DIFERENTE
                | MENORQUE
                | MAYORQUE
                | MENORIGUAL
                | MAYORIGUAL
    '''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        error_msg = f"Error de sintaxis en '{p.value}' en la línea {p.lineno}"
    else:
        error_msg = "Error de sintaxis al final de la entrada"
    syntax_errors.append(error_msg)
    # Imprimir el stack de análisis para depuración
    parser.errok()


parser = yacc.yacc()
