from flask import Flask, render_template, request, redirect, url_for, jsonify

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
    return render_template('index.html', texto_completo=texto_completo)

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
    return jsonify({'texto_completo': texto_completo})

if __name__ == '__main__':
    app.run(debug=True)