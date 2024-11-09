from flask import Flask, render_template, request, redirect, url_for, jsonify
from lexer import prueba  # Importamos la función `prueba` del lexer para analizar el código
from parser import parse  # Importamos la función `parse` para el análisis sintáctico
import psycopg2
import os

app = Flask(__name__)

# Variables globales para almacenar los textos ingresados
db_name = ''
use_db = ''
table_name = ''
insert_data = ''
query_data = ''

# Función de conexión a PostgreSQL
def get_db_connection(database="compiladores"):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="ange",  # Nombre de la base de datos a conectar
            user="postgres",
            password="HolaShepi"  # Cambiar por la contraseña real
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        print("Conexión exitosa:", cursor.fetchone())
        cursor.close()
        return conn
    except Exception as e:
        print("Error al conectar a PostgreSQL:", e)
        return None


@app.route('/')
def index():
    texto_completo = f"""
{db_name}

{use_db}

{table_name}

{insert_data}

{query_data}
"""
    return render_template('index.html', texto_completo=texto_completo, db_name=db_name, use_db=use_db, table_name=table_name, insert_data=insert_data, query_data=query_data)

@app.route('/analizar_sintaxis', methods=['POST'])
def analizar_sintaxis():
    code = request.form.get('code', '')
    resultado_sintactico = parse(code)  # Usamos la función `parse` del parser
    return jsonify({
        "sintaxis": resultado_sintactico
    })

@app.route('/analizar', methods=['POST'])
def analizar():
    code = request.form.get('code', '')
    tokens = prueba(code)  # Usamos la función `prueba` del lexer para obtener los tokens
    return jsonify(tokens=tokens)

# Validación de comandos SQL correctos para cada paso
def validar_comando(comando, tipo):
    if tipo == "CREATE DATABASE" and not comando.strip().upper().startswith("CREATE DATABASE"):
        return False
    elif tipo == "USE" and not comando.strip().upper().startswith("USE"):
        return False
    elif tipo == "CREATE TABLE" and not comando.strip().upper().startswith("CREATE TABLE"):
        return False
    elif tipo == "INSERT INTO" and not comando.strip().upper().startswith("INSERT INTO"):
        return False
    elif tipo in ["SELECT", "UPDATE", "DELETE"] and not any(comando.strip().upper().startswith(cmd) for cmd in ["SELECT", "UPDATE", "DELETE"]):
        return False
    return True

@app.route('/ejecutar_sql', methods=['POST'])
def ejecutar_sql():
    data = request.get_json()
    codigo_sql = data.get('codigo_sql', '')

    # Verificar que el código SQL no esté vacío
    if not codigo_sql.strip():
        return jsonify({"message": "El código SQL está vacío."}), 400

    # Ejecutar el SQL en PostgreSQL
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(codigo_sql)
            if codigo_sql.strip().upper().startswith("SELECT"):
                # Si es una consulta SELECT, devolver los resultados
                results = cursor.fetchall()
                message = f"Consulta ejecutada exitosamente. Resultados: {results}"
            else:
                # Para otros comandos, simplemente confirmar la ejecución
                conn.commit()
                message = "Código SQL ejecutado exitosamente."
        except Exception as e:
            print(f"Error al ejecutar el código SQL: {e}")
            message = f"Error al ejecutar el código SQL: {e}"
        finally:
            cursor.close()
            conn.close()
    else:
        message = "No se pudo establecer la conexión con la base de datos."

    return jsonify({"message": message})


@app.route('/submit_db_name', methods=['POST'])
def submit_db_name():
    global db_name
    db_name = request.form.get('db_name', '')

    if not validar_comando(db_name, "CREATE DATABASE"):
        return jsonify({"error": "El código debe comenzar con 'CREATE DATABASE'"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(db_name)
            print("Base de datos creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la base de datos: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

@app.route('/submit_use_db', methods=['POST'])
def submit_use_db():
    global use_db
    use_db = request.form.get('use_db', '').strip()

    if not validar_comando(use_db, "USE"):
        return jsonify({"error": "El código debe comenzar con 'USE'"}), 400

    # Cambiamos la base de datos al nombre especificado en lugar de ejecutar un comando `USE`
    db_name = use_db.split()[1]  # Extraer el nombre de la base de datos
    conn = get_db_connection(database=db_name)
    if conn:
        print(f"Cambiado a la base de datos: {db_name}")
        conn.close()
    else:
        return jsonify({"error": f"No se pudo conectar a la base de datos {db_name}"}), 500
    return redirect(url_for('index'))

@app.route('/submit_table_name', methods=['POST'])
def submit_table_name():
    global table_name
    table_name = request.form.get('table_name', '')

    if not validar_comando(table_name, "CREATE TABLE"):
        return jsonify({"error": "El código debe comenzar con 'CREATE TABLE'"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(table_name)
            conn.commit()
            print("Tabla creada exitosamente.")
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

@app.route('/submit_insert_data', methods=['POST'])
def submit_insert_data():
    global insert_data
    insert_data = request.form.get('insert_data', '')

    if not validar_comando(insert_data, "INSERT INTO"):
        return jsonify({"error": "El código debe comenzar con 'INSERT INTO'"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(insert_data)
            conn.commit()
            print("Datos insertados exitosamente.")
        except Exception as e:
            print(f"Error al insertar datos: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

@app.route('/submit_query_data', methods=['POST'])
def submit_query_data():
    global query_data
    query_data = request.form.get('query_data', '')

    if not validar_comando(query_data, "SELECT"):
        return jsonify({"error": "El código debe comenzar con 'SELECT', 'UPDATE', o 'DELETE'"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            if query_data.strip().upper().startswith("SELECT"):
                cursor.execute(query_data)
                results = cursor.fetchall()
                print("Resultados de la consulta:", results)
            else:
                cursor.execute(query_data)
                conn.commit()
                print("Operación realizada exitosamente.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

@app.route('/submit_all', methods=['POST'])
def submit_all():
    global db_name, use_db, table_name, insert_data, query_data
    
    data = request.get_json()
    db_name = data.get('db_name', '')
    use_db = data.get('use_db', '')
    table_name = data.get('table_name', '')
    insert_data = data.get('insert_data', '')
    query_data = data.get('query_data', '')

    if not validar_comando(db_name, "CREATE DATABASE"):
        return jsonify({"error": "El código para crear la base de datos es incorrecto"}), 400
    if not validar_comando(use_db, "USE"):
        return jsonify({"error": "El código para usar la base de datos es incorrecto"}), 400
    if not validar_comando(table_name, "CREATE TABLE"):
        return jsonify({"error": "El código para crear la tabla es incorrecto"}), 400
    if not validar_comando(insert_data, "INSERT INTO"):
        return jsonify({"error": "El código para insertar datos es incorrecto"}), 400
    if not validar_comando(query_data, "SELECT"):
        return jsonify({"error": "El código para consultar los datos es incorrecto"}), 400

    texto_completo = f"""
{db_name}

{use_db}

{table_name}

{insert_data}

{query_data}
"""
    return jsonify({"texto_completo": texto_completo})

if __name__ == '__main__':
    app.run(debug=True)