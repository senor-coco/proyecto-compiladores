from flask import Flask, render_template, request, redirect, url_for, jsonify
from lexer import prueba

app = Flask(__name__)

# Variables globales para almacenar los textos ingresados
db_name = ''
use_db = ''
table_name = ''
insert_data = ''
query_data = ''

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
    return redirect(url_for('index'))

@app.route('/submit_insert_data', methods=['POST'])
def submit_insert_data():
    global insert_data
    insert_data = request.form.get('insert_data', '')
    return redirect(url_for('index'))

@app.route('/submit_query_data', methods=['POST'])
def submit_query_data():
    global query_data
    query_data = request.form.get('query_data', '')
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


if __name__ == '__main__':
    app.run(debug=True)
