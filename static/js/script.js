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
// Objeto para almacenar el estado del reconocimiento por textarea
const reconocimientoVoz = {};

// Función para iniciar o detener el dictado de voz en un textarea específico
function iniciarDictado(textareaName) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        alert('Tu navegador no soporta el reconocimiento de voz. Por favor, utiliza un navegador compatible como Google Chrome.');
        return;
    }

    const textarea = document.querySelector(`textarea[name="${textareaName}"]`);
    const dictarButton = textarea.parentElement.querySelector('.btn.dictar');

    // Verificar si ya hay un reconocimiento en curso para este textarea
    if (reconocimientoVoz[textareaName] && reconocimientoVoz[textareaName].activo) {
        // Detener el reconocimiento
        reconocimientoVoz[textareaName].recognition.stop();
        reconocimientoVoz[textareaName].activo = false;
        dictarButton.classList.remove('activo'); // Actualizar apariencia del botón
        dictarButton.disabled = false;
        return;
    }

    // Configurar el reconocimiento de voz
    const recognition = new SpeechRecognition();
    recognition.lang = 'en-US'; // Idioma inglés
    recognition.interimResults = true; // Habilitar resultados intermedios
    recognition.continuous = true; // Continuar reconociendo hasta que el usuario detenga
    recognition.maxAlternatives = 1;

    reconocimientoVoz[textareaName] = {
        recognition: recognition,
        activo: true
    };

    dictarButton.classList.add('activo'); // Cambiar apariencia del botón
    dictarButton.disabled = false;

    let textoTemporal = '';
    let textoFinal = textarea.value;

    recognition.onresult = function(event) {
        textoTemporal = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            const transcript = event.results[i][0].transcript;
            if (event.results[i].isFinal) {
                textoFinal += transcript + ' ';
            } else {
                textoTemporal += transcript;
            }
        }
        textarea.value = textoFinal + textoTemporal;
    };

    recognition.onerror = function(event) {
        console.error('Error en el reconocimiento de voz:', event.error);
        alert('Ocurrió un error durante el reconocimiento de voz: ' + event.error);
        dictarButton.classList.remove('activo');
        reconocimientoVoz[textareaName].activo = false;
    };

    recognition.onend = function() {
        if (reconocimientoVoz[textareaName].activo) {
            // Reiniciar el reconocimiento si aún está activo
            recognition.start();
        } else {
            dictarButton.classList.remove('activo');
            dictarButton.disabled = false;
        }
    };

    // Iniciar el reconocimiento
    recognition.start();
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

// Función para actualizar la conexión a la base de datos desde la interfaz
function actualizarConexion() {
    const db_host = document.querySelector('input[name="db_host"]').value;
    const db_name = document.querySelector('input[name="db_name"]').value;
    const db_user = document.querySelector('input[name="db_user"]').value;
    const db_password = document.querySelector('input[name="db_password"]').value;

    const datosConexion = { db_host, db_name, db_user, db_password };

    fetch('/actualizar_conexion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datosConexion)
    })
    .then(response => {
        if (response.ok) {
            alert("Conexión a la base de datos actualizada exitosamente.");
        } else {
            throw new Error("Error al actualizar la conexión.");
        }
    })
    .catch(error => {
        console.error('Error al actualizar la conexión:', error);
        alert("Error al actualizar la conexión a la base de datos.");
    });
}

// Función para enviar y crear la tabla desde el formulario
function crearTabla() {
    const tableSql = document.querySelector('textarea[name="table_name"]').value;

    fetch('/crear_tabla', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({ crear_tabla: tableSql })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error al crear la tabla:', error);
        alert("Error al crear la tabla en PostgreSQL.");
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
    // Agregado para limpiar los resultados de la tabla
    document.getElementById('tabla-resultados').innerHTML = '';
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
            return response.json().then(errorData => { throw new Error(errorData.message); });
        }
        return response.json();
    })
    .then(data => {
        console.log(data.message);
        alert(data.message);

        // Mostrar los resultados de SELECT en tabla HTML si es una consulta SELECT
        if (data.data && data.columns) {
            mostrarResultados(data.data, data.columns);
        }
    })
    .catch(error => {
        console.error('Error al ejecutar en PostgreSQL:', error);
        alert('Error al ejecutar el código en PostgreSQL: ' + error.message);
    });
}

// Función para mostrar los resultados de SELECT en tabla HTML
function mostrarResultados(data, columns) {
    const resultadoDiv = document.getElementById('tabla-resultados');
    resultadoDiv.innerHTML = '';

    if (data.length > 0) {
        let tableHTML = '<table class="tabla-resultados"><tr>';

        // Encabezados de la tabla
        columns.forEach(col => {
            tableHTML += `<th>${col}</th>`;
        });
        tableHTML += '</tr>';

        // Filas de resultados
        data.forEach(row => {
            tableHTML += '<tr>';
            columns.forEach(col => {
                tableHTML += `<td>${row[col]}</td>`;
            });
            tableHTML += '</tr>';
        });

        tableHTML += '</table>';
        resultadoDiv.innerHTML = tableHTML;
    } else {
        resultadoDiv.innerHTML = "<p>No se encontraron resultados.</p>";
    }
}

// Código original (no eliminado)
// function ejecutarEnPostgreSQL() {
//     const textoCompleto = document.getElementById('texto-completo').innerText.trim();

//     if (!textoCompleto) {
//         alert("No hay código SQL para ejecutar.");
//         return;
//     }

//     fetch('/ejecutar_sql', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ 'codigo_sql': textoCompleto })
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error("Error en la solicitud: " + response.statusText);
//         }
//         return response.json();
//     })
//     .then(data => {
//         console.log(data.message);
//         alert(data.message);

//         // Mostrar los resultados de SELECT en tabla HTML si es una consulta SELECT
//         if (textoCompleto.toUpperCase().startsWith("SELECT")) {
//             mostrarResultados(data);
//         }
//     })
//     .catch(error => {
//         console.error('Error al ejecutar en PostgreSQL:', error);
//         alert('Error al ejecutar el código en PostgreSQL');
//     });
// }

// function mostrarResultados(data) {
//     const resultadoDiv = document.getElementById('resultado-analisis');
//     resultadoDiv.innerHTML = '';

//     if (data.result && data.result.length > 0) {
//         let tableHTML = '<table class="tabla-resultados"><tr>';

//         // Encabezados de la tabla
//         Object.keys(data.result[0]).forEach(key => {
//             tableHTML += `<th>${key}</th>`;
//         });
//         tableHTML += '</tr>';

//         // Filas de resultados
//         data.result.forEach(row => {
//             tableHTML += '<tr>';
//             Object.values(row).forEach(value => {
//                 tableHTML += `<td>${value}</td>`;
//             });
//             tableHTML += '</tr>';
//         });

//         tableHTML += '</table>';
//         resultadoDiv.innerHTML = tableHTML;
//     } else {
//         resultadoDiv.innerHTML = "<p>No se encontraron resultados.</p>";
//     }
// }