import ply.yacc as yacc
from lexer import tokens

# Definir la producción de inicio
start = 'instrucciones'

# Resultados del análisis sintáctico
resultado_sintactico = []

# Reglas para las producciones

def p_instrucciones_lista(p):
    '''instrucciones : instrucciones instruccion
                     | instruccion'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_instruccion(p):
    '''instruccion : crear_db
                   | usar_db
                   | crear_tabla
                   | insertar_datos
                   | consulta_datos
                   | modificar_datos
                   | eliminar_datos'''
    resultado_sintactico.append(p[1])
    p[0] = p[1]

# Producción para `CREATE DATABASE`
def p_crear_db(p):
    '''crear_db : CREATE DATABASE IDENTIFICADOR PUNTOCOMA'''
    p[0] = ('crear_db', p[3])

# Producción para `USE`
def p_usar_db(p):
    '''usar_db : USE IDENTIFICADOR PUNTOCOMA'''
    p[0] = ('usar_db', p[2])

# Producción para `CREATE TABLE`
def p_crear_tabla(p):
    '''crear_tabla : CREATE TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ columnas PARDER PUNTOCOMA'''
    p[0] = ('crear_tabla', p[3], p[5], p[7])

def p_columnas_lista(p):
    '''columnas : columnas COMA columna
                | columna'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_columna(p):
    '''columna : IDENTIFICADOR tipos_datos atributos'''
    p[0] = (p[1], p[2], p[3])

def p_tipos_datos(p):
    '''tipos_datos : BIGINT
                   | CHARACTER VARYING PARIZQ NUMERO PARDER
                   | CHAR'''
    p[0] = p[1]

def p_atributos(p):
    '''atributos : NOT NULL
                 | NULL
                 | '''
    p[0] = p[1] if len(p) > 1 else 'NULL'

# Producción para `INSERT INTO`
def p_insertar_datos(p):
    '''insertar_datos : INSERT INTO IDENTIFICADOR PUNTO IDENTIFICADOR VALUES PARIZQ valores PARDER PUNTOCOMA'''
    p[0] = ('insertar_datos', p[3], p[5], p[8])

def p_valores(p):
    '''valores : valores COMA valor
               | valor'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_valor(p):
    '''valor : NUMERO
             | CADENA'''
    p[0] = p[1]

# Producción para `SELECT`
def p_consulta_datos(p):
    '''consulta_datos : SELECT IDENTIFICADOR FROM IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMA'''
    p[0] = ('consulta_datos', p[2], p[4], p[6])

# Producción para `UPDATE`
def p_modificar_datos(p):
    '''modificar_datos : UPDATE IDENTIFICADOR PUNTO IDENTIFICADOR SET asignaciones WHERE condicion PUNTOCOMA'''
    p[0] = ('modificar_datos', p[2], p[4], p[6], p[8])

def p_asignaciones_lista(p):
    '''asignaciones : asignaciones COMA asignacion
                    | asignacion'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_asignacion(p):
    '''asignacion : IDENTIFICADOR IGUAL valor'''
    p[0] = (p[1], p[3])

# Producción para `DELETE`
def p_eliminar_datos(p):
    '''eliminar_datos : DELETE FROM IDENTIFICADOR PUNTO IDENTIFICADOR WHERE condicion PUNTOCOMA'''
    p[0] = ('eliminar_datos', p[3], p[5], p[7])

# Condición para `WHERE`
def p_condicion(p):
    '''condicion : IDENTIFICADOR operador valor'''
    p[0] = (p[1], p[2], p[3])

def p_operador(p):
    '''operador : IGUAL
                | DIFERENTE
                | MAYORQUE
                | MENORQUE
                | MAYORIGUAL
                | MENORIGUAL'''
    p[0] = p[1]

# Error de sintaxis
def p_error(p):
    print(f"Error de sintaxis en '{p.value}'" if p else "Error de sintaxis en EOF")

# Construimos el parser
parser = yacc.yacc()

# Función de análisis
def parse(data):
    resultado_sintactico.clear()
    parser.parse(data)
    return resultado_sintactico
