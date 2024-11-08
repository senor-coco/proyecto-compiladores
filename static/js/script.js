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
    const inputs = document.querySelectorAll('form textarea');
    inputs.forEach(input => {
        input.value = '';
    });
}

// Función para enviar todos los formularios
function enviarTodosLosFormularios() {
    const db_name = document.querySelector('textarea[name="db_name"]').value;
    const use_db = document.querySelector('textarea[name="use_db"]').value;
    const table_name = document.querySelector('textarea[name="table_name"]').value;
    const insert_data = document.querySelector('textarea[name="insert_data"]').value;
    const query_data = document.querySelector('textarea[name="query_data"]').value;

    const datos = { db_name, use_db, table_name, insert_data, query_data };

    fetch('/submit_all', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        const cuadroBlanco = document.getElementById('cuadro-blanco');
        if (cuadroBlanco) {
            cuadroBlanco.innerHTML = `
                <h2>Código Completo:</h2>
                <pre id="texto-completo">${data.texto_completo}</pre>
                <div class="button-container">
                    <button type="button" class="btn analizar" onclick="analizarCodigo()">Analizar</button>
                    <button type="button" class="btn borrar" onclick="borrarScript()">Borrar</button>
                    <button type="button" class="btn generar" onclick="generarScript()">Generar Script</button>
                    <button type="button" class="btn ejecutar" onclick="ejecutarEnPostgreSQL()">Ejecutar en PostgreSQL</button>
                </div>
            `;
        } else {
            const nuevoCuadroBlanco = document.createElement('div');
            nuevoCuadroBlanco.id = 'cuadro-blanco';
            nuevoCuadroBlanco.className = 'cuadro-blanco';
            nuevoCuadroBlanco.innerHTML = `
                <h2>Código Completo:</h2>
                <pre id="texto-completo">${data.texto_completo}</pre>
                <div class="button-container">
                    <button type="button" class="btn analizar" onclick="analizarCodigo()">Analizar</button>
                    <button type="button" class="btn borrar" onclick="borrarScript()">Borrar</button>
                    <button type="button" class="btn generar" onclick="generarScript()">Generar Script</button>
                    <button type="button" class="btn ejecutar" onclick="ejecutarEnPostgreSQL()">Ejecutar en PostgreSQL</button>
                </div>
            `;
            const stepsContainer = document.querySelector('.steps-container');
            stepsContainer.appendChild(nuevoCuadroBlanco);
        }
    })
    .catch(error => {
        console.error('Error al enviar los datos:', error);
    });
}

// Función para analizar y enviar el contenido de cada textarea
function analizarParte(parte) {
    const textarea = document.querySelector(`textarea[name="${parte}"]`);
    const contenido = textarea.value;
    const notificacion = document.getElementById(`notificacion-${parte}`);

    // Enviar el contenido al backend para su análisis
    fetch('/analizar_sintaxis', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({ code: contenido })
    })
    .then(response => response.json())
    .then(data => {
        notificacion.innerHTML = "";
        notificacion.style.display = "block";

        if (data.sintaxis.correcto) {
            // Mostrar mensaje de éxito
            notificacion.className = 'notificacion verde';
            notificacion.textContent = 'Código correcto';

            // Agregar el contenido al cuadro de "Código Completo"
            const cuadroBlanco = document.getElementById("cuadro-blanco");
            const textoCompleto = document.getElementById("texto-completo");

            // Añadir el contenido al cuadro de texto completo
            textoCompleto.innerText += contenido + "\n";

            // Mostrar el cuadro de "Código Completo" si no está visible
            cuadroBlanco.style.display = "block";
        } else {
            // Mostrar mensaje de error
            notificacion.className = 'notificacion rojo';
            notificacion.textContent = `Error: ${data.sintaxis.error}`;
        }
    })
    .catch(error => {
        console.error('Error en la validación:', error);
        notificacion.className = 'notificacion rojo';
        notificacion.textContent = 'Error al validar el código';
        notificacion.style.display = "block";
    });
}

document.querySelectorAll('.step-input').forEach((element, index, array) => {
    element.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            const nextElement = array[index + 1];
            if (nextElement) {
                nextElement.focus();
            }
        }
    });
});

document.querySelectorAll('.step-input').forEach((element) => {
    const name = element.getAttribute('name');
    if (localStorage.getItem(name)) {
        element.value = localStorage.getItem(name);
    }
    element.addEventListener('input', function() {
        localStorage.setItem(name, element.value);
    });
});

function borrarScript() {
    document.getElementById('texto-completo').innerText = '';
    $('#resultado-analisis').empty();
}

function generarScript() {
    var textoCompleto = document.getElementById('texto-completo').innerText;
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
        alert('Tu navegador no soporta la descarga de archivos.');
    }
}

function ejecutarEnPostgreSQL() {
    const textoCompleto = document.getElementById('texto-completo').innerText.trim();

    if (!textoCompleto) {
        alert("No hay código SQL para ejecutar.");
        return;
    }

    fetch('/ejecutar_sql', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'codigo_sql': textoCompleto })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Error en la solicitud: " + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        alert(data.message);
    })
    .catch(error => {
        console.error('Error al ejecutar en PostgreSQL:', error);
        alert('Error al ejecutar el código en PostgreSQL');
    });
}