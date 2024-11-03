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
    // Selecciona todos los inputs de tipo texto dentro del formulario
    const inputs = document.querySelectorAll('form input[type="text"]');
    
    // Itera sobre cada input y borra su valor
    inputs.forEach(input => {
        input.value = '';
    });
}

// Función para enviar todos los formularios
function enviarTodosLosFormularios() {
    // Recopilar datos de todos los formularios
    const db_name = document.querySelector('input[name="db_name"]').value;
    const use_db = document.querySelector('input[name="use_db"]').value;
    const table_name = document.querySelector('input[name="table_name"]').value;
    const insert_data = document.querySelector('input[name="insert_data"]').value;
    const query_data = document.querySelector('input[name="query_data"]').value;

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
                <pre>${data.texto_completo}</pre>
                <!-- Botones dentro del cuadro blanco -->
                <div class="button-container">
                    <button type="button" class="btn analizar" onclick="analizarCodigo()">Analizar</button>
                    <button type="button" class="btn borrar" onclick="borrarScript()">Borrar</button>
                    <button type="button" class="btn generar" onclick="generarScript()">Generar Script</button>
                </div>
            `;
        } else {
            // Si el cuadro blanco no existe, crearlo
            const nuevoCuadroBlanco = document.createElement('div');
            nuevoCuadroBlanco.id = 'cuadro-blanco';
            nuevoCuadroBlanco.className = 'cuadro-blanco';
            nuevoCuadroBlanco.innerHTML = `
                <h2>Código Completo:</h2>
                <pre>${data.texto_completo}</pre>
                <!-- Botones dentro del cuadro blanco -->
                <div class="button-container">
                    <button type="button" class="btn analizar" onclick="analizarCodigo()">Analizar</button>
                    <button type="button" class="btn borrar" onclick="borrarScript()">Borrar</button>
                    <button type="button" class="btn generar" onclick="generarScript()">Generar Script</button>
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

function borrarScript() {
    // Limpiar el contenido del cuadro blanco
    const cuadroBlanco = document.getElementById('cuadro-blanco');
    if (cuadroBlanco) {
        cuadroBlanco.remove();
    }
    // Remover la tabla de tokens si existe
    const tablaExistente = document.querySelector('.tabla-tokens');
    if (tablaExistente) {
        tablaExistente.remove();
    }
}

function generarScript() {
    // Tu lógica para generar el script
}
