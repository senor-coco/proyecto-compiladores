// Modo oscuro
const toggleSwitch = document.getElementById('theme-toggle');
const body = document.body;

toggleSwitch.addEventListener('change', () => {
    if (toggleSwitch.checked) {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
    }
});

// Borrar campos de los formularios
function borrarCampos() {
    // Selecciona todos los textareas dentro de los formularios
    const inputs = document.querySelectorAll('form textarea');
    
    // Itera sobre cada textarea y borra su valor
    inputs.forEach(input => {
        input.value = '';
    });
}

// Función para enviar todos los formularios
function enviarTodosLosFormularios() {
    // Recopilar datos de todos los formularios
    const db_name = document.querySelector('textarea[name="db_name"]').value;
    const use_db = document.querySelector('textarea[name="use_db"]').value;
    const table_name = document.querySelector('textarea[name="table_name"]').value;
    const insert_data = document.querySelector('textarea[name="insert_data"]').value;
    const query_data = document.querySelector('textarea[name="query_data"]').value;

    // Crear un objeto con todos los datos
    const datos = {
        db_name,
        use_db,
        table_name,
        insert_data,
        query_data
    };

    // Enviar los datos al servidor mediante fetch
    fetch('/submit_all', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        // Actualizar el contenido del cuadro blanco
        const cuadroBlanco = document.getElementById('cuadro-blanco');
        if (cuadroBlanco) {
            cuadroBlanco.innerHTML = `
                <h2>Código Completo:</h2>
                <pre id="texto-completo">${data.texto_completo}</pre>
                <!-- Botones dentro del cuadro blanco -->
                <div class="button-container">
                    <button type="button" class="btn analizar" onclick="analizarCodigo()">Analizar</button>
                    <button type="button" class="btn borrar" onclick="borrarScript()">Borrar</button>
                    <button type="button" class="btn generar" onclick="generarScript()">Generar Script</button>
                    <button type="button" class="btn ejecutar" onclick="ejecutarEnPostgreSQL()">Ejecutar en PostgreSQL</button>
                </div>
            `;
        } else {
            // Si el cuadro blanco no existe, crearlo
            const nuevoCuadroBlanco = document.createElement('div');
            nuevoCuadroBlanco.id = 'cuadro-blanco';
            nuevoCuadroBlanco.className = 'cuadro-blanco';
            nuevoCuadroBlanco.innerHTML = `
                <h2>Código Completo:</h2>
                <pre id="texto-completo">${data.texto_completo}</pre>
                <!-- Botones dentro del cuadro blanco -->
                <div class="button-container">
                    <button type="button" class="btn analizar" onclick="analizarCodigo()">Analizar</button>
                    <button type="button" class="btn borrar" onclick="borrarScript()">Borrar</button>
                    <button type="button" class="btn generar" onclick="generarScript()">Generar Script</button>
                    <button type="button" class="btn ejecutar" onclick="ejecutarEnPostgreSQL()">Ejecutar en PostgreSQL</button>
                </div>
            `;
            // Insertar el cuadro blanco en el DOM
            const stepsContainer = document.querySelector('.steps-container');
            stepsContainer.appendChild(nuevoCuadroBlanco);
        }
    })
    .catch(error => {
        console.error('Error al enviar los datos:', error);
    });
}

// Añadir evento para mover al siguiente campo al presionar Enter
document.querySelectorAll('.step-input').forEach((element, index, array) => {
    element.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Prevenir el salto de línea
            const nextElement = array[index + 1];
            if (nextElement) {
                nextElement.focus();
            }
        }
    });
});

// Función para almacenar y cargar datos previos de los formularios
document.querySelectorAll('.step-input').forEach((element) => {
    const name = element.getAttribute('name');
    
    // Cargar datos previos
    if (localStorage.getItem(name)) {
        element.value = localStorage.getItem(name);
    }

    // Guardar cambios en localStorage al escribir en el campo
    element.addEventListener('input', function() {
        localStorage.setItem(name, element.value);
    });
});


// Función para borrar el contenido del script y el análisis
function borrarScript() {
    // Limpiar el contenido del código y el resultado
    document.getElementById('texto-completo').innerText = '';
    $('#resultado-analisis').empty();
}

// Función para generar el script y descargarlo como archivo .sql
function generarScript() {
    console.log("La función generarScript() se ha llamado.");
    var textoCompleto = document.getElementById('texto-completo').innerText;
    console.log("Contenido de textoCompleto:", textoCompleto);

    var blob = new Blob([textoCompleto], { type: 'text/sql;charset=utf-8;' });
    var link = document.createElement('a');
    if (link.download !== undefined) {
        var nombreArchivo = 'script.sql';
        var url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', nombreArchivo);
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    } else {
        alert('Tu navegador no soporta la descarga de archivos. Por favor, copia y pega el contenido manualmente.');
    }
}

// Nueva función para ejecutar el código completo en PostgreSQL
function ejecutarEnPostgreSQL() {
    const textoCompleto = document.getElementById('texto-completo').innerText;

    fetch('/ejecutar_sql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'codigo_sql': textoCompleto })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        alert(data.message); // Muestra un mensaje con el resultado de la ejecución
    })
    .catch(error => {
        console.error('Error al ejecutar en PostgreSQL:', error);
        alert('Error al ejecutar el código en PostgreSQL');
    });
}