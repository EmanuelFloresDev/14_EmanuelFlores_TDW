let slideActual = 0;

const slides = document.querySelectorAll(".slide");


function mostrarSlide(numero) {

    if (numero >= slides.length) {
        slideActual = 0;
    }

    if (numero < 0) {
        slideActual = slides.length - 1;
    }

    slides.forEach(function(slide) {
        slide.classList.remove("active");
    });

    slides[slideActual].classList.add("active");
}

function cambiarSlide(direccion) {
    slideActual = slideActual + direccion;

    mostrarSlide(slideActual);
}

mostrarSlide(slideActual);
