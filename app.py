from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Recuperar los datos del formulario
    db_name = request.form['db_name']
    use_db = request.form['use_db']
    table_name = request.form['table_name']
    insert_data = request.form['insert_data']
    query_data = request.form['query_data']
    
    # Lógica para procesar los datos
    # ...

    return render_template('index.html', mensaje="Datos enviados correctamente")

if __name__ == '__main__':
    app.run(debug=True)
