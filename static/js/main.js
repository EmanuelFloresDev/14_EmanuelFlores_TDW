// MOSTRAR MENSAJE
const btnMensaje = document.getElementById("btnMensaje");

btnMensaje.addEventListener("click", function () {
    alert("¡Bienvenido a TechZone!");
});


// CAMBIAR CONTENIDO
const btnContenido = document.getElementById("btnContenido");
const descripcion = document.getElementById("descripcion");

let contenidoOriginal = true;

btnContenido.addEventListener("click", function () {

    if (contenidoOriginal) {

        descripcion.textContent =
            "TechZone ofrece soluciones tecnológicas para estudiantes, profesionales y amantes de la tecnología.";
        btnContenido.textContent = "Restaurar contenido";
        contenidoOriginal = false;

    } else {

        descripcion.textContent =
            "En TechZone encontrarás productos tecnológicos pensados para mejorar tu día a día.";
        btnContenido.textContent = "Cambiar contenido";
        contenidoOriginal = true;
    }
});

// MODIFICAR ESTILO
const btnEstilo = document.getElementById("btnEstilo");
let estiloOriginal = true;

btnEstilo.addEventListener("click", function () {

    if (estiloOriginal) {

        descripcion.style.color = "#22d3ee";
        descripcion.style.fontWeight = "bold";
        descripcion.style.fontSize = "20px";
        btnEstilo.textContent = "Restaurar estilo";
        estiloOriginal = false;

    } else {

        descripcion.style.color = "";
        descripcion.style.fontWeight = "";
        descripcion.style.fontSize = "";
        btnEstilo.textContent = "Cambiar estilo";

        estiloOriginal = true;
    }
});