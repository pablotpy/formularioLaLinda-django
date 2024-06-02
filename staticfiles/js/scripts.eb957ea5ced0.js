                 // Función para convertir automáticamente el texto a mayúsculas mientras el usuario escribe
                 function convertirAMayusculas(input) {
                    input.value = input.value.toUpperCase();
                    
                }
        
                // Obtener todos los campos de texto del formulario
                var camposTexto = document.querySelectorAll('input[type="text"]');
        
                // Iterar sobre los campos de texto y agregar el evento de entrada
                camposTexto.forEach(function(input) {
                    input.addEventListener('input', function() {
                        convertirAMayusculas(this);
                    });
                });
                       
        // Función para formatear el Nombre
        function formatearNombres(input) {
            let valor = input.value;
            valor = valor.substring(0, 30);
            valor = valor.replace(/[^A-Z\s]/g, '');         
            input.value = valor;
        }

        // Obtener el campo de texto para nombres
        var campoNombres = document.querySelector('input[name="nombres"]');
        // Agregar el evento de entrada al campo de texto para formatear
        campoNombres.addEventListener('input', function() {
            formatearNombres(this);
        });
        
         // Función para formatear el Apellidos
            function formatearApellidos(input) {
            let valor = input.value;
            valor = valor.substring(0, 30);
            valor = valor.replace(/[^A-Z\s]/g, '');         
            input.value = valor;
        }

        // Obtener el campo de texto para nombres
        var campoApellidos = document.querySelector('input[name="apellidos"]');
        // Agregar el evento de entrada al campo de texto para formatear
        campoApellidos.addEventListener('input', function() {
            formatearApellidos(this);
        });
            

           

       // Función para formatear el número de teléfono
        function formatearTelefono(input) {
            // Obtener el valor actual del campo de texto
            let valor = input.value;
            // Eliminar cualquier guión presente en el valor actual
            valor = valor.replace(/\D/g, '');
            // Limitar la cantidad máxima de caracteres a 10
            valor = valor.substring(0, 10);
            // Verificar si el valor tiene al menos 4 caracteres y agregar el primer guión
            if (valor.length >= 4) {
                valor = valor.substring(0, 4) + '-' + valor.substring(4);
            }
            // Verificar si el valor tiene al menos 8 caracteres y agregar el segundo guión
            if (valor.length >= 8) {
                valor = valor.substring(0, 8) + '-' + valor.substring(8);
            }
            // Actualizar el valor del campo de texto
            input.value = valor;
        }

        // Obtener el campo de texto para el número de teléfono
        var campoTelefono = document.querySelector('input[name="telefono"]');

        // Agregar el evento de entrada al campo de texto para formatear y limitar el número de teléfono
        campoTelefono.addEventListener('input', function() {
            formatearTelefono(this);
        });

        // 001-001-0000001
        function formatearComprobante(input) {
            let valor = input.value;
            valor = valor.replace(/\D/g, '');
            valor = valor.substring(0, 13);
            // Verificar si el valor tiene al menos 4 caracteres y agregar el primer guión
            if (valor.length >= 3) {
                valor = valor.substring(0, 3) + '-' + valor.substring(3);
            }
            if (valor.length >= 7) {
                valor = valor.substring(0, 7) + '-' + valor.substring(7);
            }
            // Verificar si el valor tiene al menos 8 caracteres y agregar el segundo guión
            // Actualizar el valor del campo de texto
            input.value = valor;
        }
        var campoNrocomprobante = document.querySelector('input[name="nrocomprobante"]');
        campoNrocomprobante.addEventListener('input', function() {
            formatearComprobante(this);
        });

        function verificarEstadoCheckbox() {
    var checkbox = document.getElementById('id_terminos');
    var botonEnviar = document.getElementById('botonenviar');
    var mensaje = document.getElementById('mensaje');

    if (checkbox.checked) {
        botonEnviar.disabled = false;
        mensaje.innerHTML = ''; // Ocultar el mensaje
        mensaje.style.display='none';
    } else {
        botonEnviar.disabled = true;
        mensaje.innerHTML = 'Debe aceptar los términos y completar el formulario';
        mensaje.style.display = 'block';
    }
}

// Llamar a la función verificarEstadoCheckbox al cargar la página para establecer el estado inicial del botón de enviar y del mensaje
verificarEstadoCheckbox();

// Agregar un evento de cambio al checkbox para actualizar el estado del botón de enviar y del mensaje
document.getElementById('id_terminos').addEventListener('change', verificarEstadoCheckbox);


document.addEventListener('DOMContentLoaded', function() {
    var errorList = document.querySelector('.errorlist');

    if (errorList) {
        // Obtenemos la posición vertical del errorList
        var errorListOffset = errorList.offsetTop;

        // Hacemos que la página se desplace hasta esa posición
        window.scrollTo({
            top: errorListOffset,
            behavior: 'smooth' // Desplazamiento suave
        });
    }
});