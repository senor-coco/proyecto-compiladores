const toggleSwitch = document.getElementById('theme-toggle');
const body = document.body;

//Modo oscuro//
toggleSwitch.addEventListener('change', () => {
    if (toggleSwitch.checked) {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
    }
});
//Borrar//
function borrarCampos() {
    // Selecciona todos los inputs de tipo texto dentro del formulario
    const inputs = document.querySelectorAll('form input[type="text"]');
    
    // Itera sobre cada input y borra su valor
    inputs.forEach(input => {
        input.value = '';
    });
}
//Cuadro blanco//
function toggleCuadroBlanco() {
    const cuadroBlanco = document.getElementById('cuadro-blanco');
    const botonMostrar = document.querySelector('.btn.mostrar');

    if (cuadroBlanco && (cuadroBlanco.style.display === 'none' || cuadroBlanco.style.display === '')) {
        cuadroBlanco.style.display = 'block';
        botonMostrar.textContent = 'Ocultar Código Completo';
    } else if (cuadroBlanco) {
        cuadroBlanco.style.display = 'none';
        botonMostrar.textContent = 'Mostrar Código Completo';
    }
}
function analizarCodigo() {
    alert("Análisis en proceso...");
}