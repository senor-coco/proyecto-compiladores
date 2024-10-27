from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Recuperar los datos del formulario
    db_name = request.form.get('db_name', '')
    use_db = request.form.get('use_db', '')
    table_name = request.form.get('table_name', '')
    insert_data = request.form.get('insert_data', '')
    query_data = request.form.get('query_data', '')
    texto_adicional = request.form.get('texto_adicional', '')
    
    # Combinar todos los textos en uno solo
    texto_completo = f"""
{db_name}

{use_db}

{table_name}

{insert_data}

{query_data}

{texto_adicional}
"""

    # Aquí puedes agregar la lógica para guardar en la base de datos si es necesario
    # ...


    # Renderizar el template con el texto completo
    return render_template('index.html', texto_completo=texto_completo)

if __name__ == '__main__':
    app.run(debug=True)
