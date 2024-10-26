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
function borrarCampos() {
    // Selecciona todos los inputs de tipo texto dentro del formulario
    const inputs = document.querySelectorAll('form input[type="text"]');
    
    // Itera sobre cada input y borra su valor
    inputs.forEach(input => {
        input.value = '';
    });
}

// Función para el botón "Analizar" (opcional)
function analizarCodigo() {
    // Aquí puedes agregar la lógica para analizar el código ingresado
    alert("Análisis en proceso...");
}
