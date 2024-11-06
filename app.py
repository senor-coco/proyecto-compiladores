from flask import Flask, render_template, request, redirect, url_for, jsonify
from lexer import prueba
import psycopg2

app = Flask(__name__)

# Variables globales para almacenar los textos ingresados
db_name = ''
use_db = ''
table_name = ''
insert_data = ''
query_data = ''

# Función de conexión a PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="compiladores",  # Cambia este nombre al de tu base de datos
            user="postgres",
            password="contraseña"
        )
        conn.autocommit = True  # Configura autocommit para permitir comandos como CREATE DATABASE
        # Comando de prueba para verificar conexión
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        print("Conexión exitosa:", cursor.fetchone())  # Muestra la versión de PostgreSQL para confirmar conexión
        cursor.close()
        return conn
    except Exception as e:
        print("Error al conectar a PostgreSQL:", e)
        return None

@app.route('/')
def index():
    # Combinar todos los textos en uno solo
    texto_completo = f"""
{db_name}

{use_db}

{table_name}

{insert_data}

{query_data}
"""
    # No ejecutamos el análisis aquí
    return render_template('index.html', texto_completo=texto_completo, db_name=db_name, use_db=use_db, table_name=table_name, insert_data=insert_data, query_data=query_data)

@app.route('/submit_db_name', methods=['POST'])
def submit_db_name():
    global db_name
    db_name = request.form.get('db_name', '')

    # Crear la base de datos en PostgreSQL
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(f"CREATE DATABASE {db_name};")
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
    use_db = request.form.get('use_db', '')
    return redirect(url_for('index'))

@app.route('/submit_table_name', methods=['POST'])
def submit_table_name():
    global table_name
    table_name = request.form.get('table_name', '')

    # Crear una tabla en PostgreSQL
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(table_name)  # Asumimos que table_name contiene la instrucción completa CREATE TABLE
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

    # Insertar datos en la tabla
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(insert_data)  # Asumimos que insert_data contiene la instrucción completa INSERT INTO
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

    # Ejecutar consulta en la base de datos
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(query_data)  # Asumimos que query_data contiene una instrucción SELECT, UPDATE, o DELETE
            if query_data.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                print("Resultados de la consulta:", results)
            else:
                conn.commit()
                print("Operación realizada exitosamente.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            cursor.close()
            conn.close()
    return redirect(url_for('index'))

# Nueva ruta para el análisis léxico
@app.route('/analizar', methods=['POST'])
def analizar():
    data = request.get_json()
    texto_completo = data.get('texto_completo', '')

    # Realizar el análisis léxico
    tokens = prueba(texto_completo)

    # Imprimir los tokens en la consola para depuración
    print('Tokens generados:', tokens)

    # Devolver los tokens como JSON
    return jsonify({'tokens': tokens})

# Nueva ruta para ejecutar el código completo en PostgreSQL
@app.route('/ejecutar_sql', methods=['POST'])
def ejecutar_sql():
    data = request.get_json()
    codigo_sql = data.get('codigo_sql', '')

    # Conectarse a PostgreSQL
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(codigo_sql)
            conn.commit()
            message = "Código ejecutado exitosamente en PostgreSQL."
        except Exception as e:
            message = f"Error al ejecutar el código: {e}"
        finally:
            cursor.close()
            conn.close()
    else:
        message = "No se pudo conectar a PostgreSQL."

    return jsonify({"message": message})

# Nueva ruta para recibir todos los campos juntos y enviarlos al "Código Completo"
@app.route('/submit_all', methods=['POST'])
def submit_all():
    global db_name, use_db, table_name, insert_data, query_data
    
    data = request.get_json()
    db_name = data.get('db_name', '')
    use_db = data.get('use_db', '')
    table_name = data.get('table_name', '')
    insert_data = data.get('insert_data', '')
    query_data = data.get('query_data', '')

    # Combinar todos los textos en uno solo
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