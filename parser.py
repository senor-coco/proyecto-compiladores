import ply.yacc as yacc
from lexer import tokens

# Definir la producción de inicio
start = 'instrucciones'

# Resultados del análisis sintáctico
resultado_sintactico = []
error_sintactico = None  # Variable para almacenar errores

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
                   | eliminar_tabla
                   | insertar_datos
                   | consulta_datos
                   | modificar_datos
                   | eliminar_datos
                   | transaccion'''
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
    '''crear_tabla : CREATE TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ definiciones PARDER PUNTOCOMA'''
    p[0] = ('crear_tabla', p[3], p[5], p[7])

# Producción para `DROP TABLE`
def p_eliminar_tabla(p):
    '''eliminar_tabla : DROP TABLE IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMA'''
    p[0] = ('eliminar_tabla', p[3], p[5])

# Producción para manejar las definiciones de columnas y claves en una tabla
def p_definiciones_lista(p):
    '''definiciones : definiciones COMA definicion
                    | definicion'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

# Producción para definir una columna, clave primaria o clave foránea
def p_definicion(p):
    '''definicion : columna
                  | primary_key
                  | foreign_key'''
    p[0] = p[1]

# Producción para una columna
def p_columna(p):
    '''columna : IDENTIFICADOR tipos_datos atributos'''
    p[0] = ('columna', p[1], p[2], p[3])

# Producción para `PRIMARY KEY`
def p_primary_key(p):
    '''primary_key : PRIMARY KEY PARIZQ IDENTIFICADOR PARDER'''
    p[0] = ('primary_key', p[4])

# Producción para `FOREIGN KEY`
def p_foreign_key(p):
    '''foreign_key : FOREIGN KEY PARIZQ IDENTIFICADOR PARDER REFERENCES IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ IDENTIFICADOR PARDER'''
    p[0] = ('foreign_key', p[4], p[7], p[9], p[11])

# Tipos de datos
def p_tipos_datos(p):
    '''tipos_datos : BIGINT
                   | INTEGER
                   | DECIMAL
                   | CHARACTER VARYING PARIZQ NUMERO PARDER
                   | CHARACTER VARYING
                   | CHAR
                   | VARCHAR PARIZQ NUMERO PARDER
                   | TEXT'''
    if len(p) == 6:
        p[0] = f"{p[1]} {p[2]}({p[4]})"
    elif len(p) == 3:
        p[0] = f"{p[1]} {p[2]}"
    else:
        p[0] = p[1]

# Atributos opcionales para las columnas
def p_atributos(p):
    '''atributos : NOT NULL
                 | NULL
                 | '''
    p[0] = p[1] if len(p) > 1 else 'NULL'

# Producción para `INSERT INTO` con soporte para múltiples filas
def p_insertar_datos(p):
    '''insertar_datos : INSERT INTO IDENTIFICADOR PUNTO IDENTIFICADOR PARIZQ identificadores PARDER VALUES listas_valores PUNTOCOMA'''
    p[0] = ('insertar_datos', p[3], p[5], p[8])

# Producción para listas de valores
def p_listas_valores(p):
    '''listas_valores : listas_valores COMA PARIZQ valores PARDER
                      | PARIZQ valores PARDER'''
    if len(p) == 6:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[2]]

# Lista de identificadores
def p_identificadores(p):
    '''identificadores : identificadores COMA IDENTIFICADOR
                       | IDENTIFICADOR'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_valores(p):
    '''valores : valores COMA valor
               | valor'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_valor(p):
    '''valor : NUMERO
             | CADENA
             | expresion'''
    p[0] = p[1]

# Producción para `SELECT` con soporte para `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`
def p_consulta_datos(p):
    '''consulta_datos : SELECT seleccion FROM IDENTIFICADOR PUNTO IDENTIFICADOR joins group_by having order_by limit PUNTOCOMA
                      | SELECT seleccion FROM IDENTIFICADOR PUNTO IDENTIFICADOR PUNTOCOMA'''
    if len(p) == 13:
        p[0] = ('consulta_datos', p[2], p[4], p[6], p[7], p[8], p[9], p[10], p[11])
    else:
        p[0] = ('consulta_datos', p[2], p[4], p[6])

def p_seleccion(p):
    '''seleccion : MULTIPLICACION
                 | seleccion COMA IDENTIFICADOR
                 | IDENTIFICADOR
                 | agregacion'''
    if len(p) == 2:
        p[0] = '*' if p[1] == '*' else [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]



def p_joins(p):
    '''joins : joins join
             | join'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_join(p):
    '''join : JOIN IDENTIFICADOR PUNTO IDENTIFICADOR ON IDENTIFICADOR operador IDENTIFICADOR'''
    p[0] = ('join', p[2], p[4], p[6], p[7], p[8])

def p_agregacion(p):
    '''agregacion : SUM PARIZQ IDENTIFICADOR PARDER
                  | COUNT PARIZQ IDENTIFICADOR PARDER
                  | AVG PARIZQ IDENTIFICADOR PARDER
                  | MAX PARIZQ IDENTIFICADOR PARDER
                  | MIN PARIZQ IDENTIFICADOR PARDER'''
    p[0] = ('agregacion', p[1], p[3])

def p_group_by(p):
    '''group_by : GROUP BY IDENTIFICADOR
                | '''
    if len(p) > 1:
        p[0] = ('group_by', p[3])
    else:
        p[0] = None

def p_having(p):
    '''having : HAVING condicion
              | '''
    if len(p) > 1:
        p[0] = ('having', p[2])
    else:
        p[0] = None

def p_order_by(p):
    '''order_by : ORDER BY IDENTIFICADOR
                | ORDER BY IDENTIFICADOR ASC
                | ORDER BY IDENTIFICADOR DESC
                | '''
    if len(p) == 4:
        p[0] = ('order_by', p[3], 'ASC')
    elif len(p) == 5:
        p[0] = ('order_by', p[3], p[4])
    else:
        p[0] = None

def p_limit(p):
    '''limit : LIMIT NUMERO
             | '''
    if len(p) > 1:
        p[0] = ('limit', p[2])
    else:
        p[0] = None

# Producción para `UPDATE` con condiciones múltiples
def p_modificar_datos(p):
    '''modificar_datos : UPDATE IDENTIFICADOR PUNTO IDENTIFICADOR SET asignaciones WHERE condiciones PUNTOCOMA'''
    p[0] = ('modificar_datos', p[2], p[4], p[6], p[8])

# Lista de asignaciones para `SET`
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

# Producción para `DELETE` con condiciones múltiples
def p_eliminar_datos(p):
    '''eliminar_datos : DELETE FROM IDENTIFICADOR PUNTO IDENTIFICADOR WHERE condiciones PUNTOCOMA'''
    p[0] = ('eliminar_datos', p[3], p[5], p[7])

# Producción para condiciones múltiples con operadores `AND` y `OR`
def p_condiciones_lista(p):
    '''condiciones : condiciones operador_logico condicion
                   | condicion'''
    if len(p) == 4:
        p[0] = ('condicion_multiple', p[1], p[2], p[3])
    else:
        p[0] = p[1]

def p_condicion(p):
    '''condicion : IDENTIFICADOR operador valor
                 | IDENTIFICADOR operador PARIZQ consulta_datos PARDER'''
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])
    else:
        p[0] = ('subconsulta', p[1], p[2], p[4])

def p_operador_logico(p):
    '''operador_logico : AND
                       | OR'''
    p[0] = p[1]

def p_operador(p):
    '''operador : IGUAL
                | DIFERENTE
                | MAYORQUE
                | MENORQUE
                | MAYORIGUAL
                | MENORIGUAL'''
    p[0] = p[1]

# Producción para expresiones aritméticas
def p_expresion(p):
    '''expresion : valor MAS valor
                 | valor MENOS valor
                 | valor MULTIPLICACION valor
                 | valor DIVISION valor'''
    p[0] = ('expresion', p[2], p[1], p[3])

# Producción para transacciones
def p_transaccion(p):
    '''transaccion : BEGIN PUNTOCOMA
                   | COMMIT PUNTOCOMA
                   | ROLLBACK PUNTOCOMA'''
    p[0] = ('transaccion', p[1])

# Error de sintaxis
def p_error(p):
    global error_sintactico
    if p:
        error_sintactico = f"Error de sintaxis en '{p.value}' en la línea {p.lineno}"
    else:
        error_sintactico = "Error de sintaxis en EOF"

# Construimos el parser
parser = yacc.yacc()

# Función de análisis
def parse(data):
    global error_sintactico
    resultado_sintactico.clear()
    error_sintactico = None  # Reinicia el error antes de analizar
    parser.parse(data)

    if error_sintactico:
        return {"correcto": False, "error": error_sintactico}
    else:
        return {"correcto": True, "resultado": resultado_sintactico}
