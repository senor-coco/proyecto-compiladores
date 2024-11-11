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

# Variables para la configuración dinámica de la base de datos
db_config = {
    "host": "localhost",
    "database": "ange",  # Nombre predeterminado de la base de datos
    "user": "postgres",
    "password": "HolaShepi"  # Contraseña predeterminada
}

# Función de conexión a PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=db_config["host"],
            database=db_config["database"],
            user=db_config["user"],
            password=db_config["password"]
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

@app.route('/actualizar_conexion', methods=['POST'])
def actualizar_conexion():
    # Actualizar los datos de conexión con los valores enviados desde el formulario
    datos_conexion = request.json
    db_config["host"] = datos_conexion.get("db_host", "localhost")
    db_config["database"] = datos_conexion.get("db_name", "ange")
    db_config["user"] = datos_conexion.get("db_user", "postgres")
    db_config["password"] = datos_conexion.get("db_password", "HolaShepi")
    
    # Verificar la conexión con la nueva configuración
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"message": "Conexión actualizada exitosamente"}), 200
    else:
        return jsonify({"message": "Error al conectar con la nueva configuración"}), 500

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

@app.route('/crear_tabla', methods=['POST'])
def crear_tabla():
    # Obtener el código SQL para crear la tabla desde el formulario
    sql_crear_tabla = request.form.get('crear_tabla', '')
    if not sql_crear_tabla.strip().upper().startswith("CREATE TABLE"):
        return jsonify({"error": "El código debe comenzar con 'CREATE TABLE'"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql_crear_tabla)
            conn.commit()
            print("Tabla creada exitosamente en pgAdmin.")
            message = "Tabla creada exitosamente."
        except Exception as e:
            print(f"Error al crear la tabla: {e}")
            message = f"Error al crear la tabla: {e}"
        finally:
            cursor.close()
            conn.close()
    else:
        message = "No se pudo establecer la conexión para crear la tabla."

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
    conn = get_db_connection()
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

# Nueva ruta para manejar SELECT * FROM <tabla> y devolver resultados en HTML
@app.route('/select_data', methods=['POST'])
def select_data():
    table_name = request.json.get('table_name')
    
    if not table_name:
        return jsonify({"error": "No se especificó el nombre de la tabla"}), 400

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

            # Crear la tabla HTML con los resultados
            results_html = "<table border='1'><tr>" + "".join(f"<th>{col}</th>" for col in columns) + "</tr>"
            for row in rows:
                results_html += "<tr>" + "".join(f"<td>{data}</td>" for data in row) + "</tr>"
            results_html += "</table>"

            return jsonify({"result": results_html})
        except Exception as e:
            print(f"Error al ejecutar SELECT: {e}")
            return jsonify({"error": f"Error al ejecutar SELECT: {e}"}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

if __name__ == '__main__':
    app.run(debug=True)