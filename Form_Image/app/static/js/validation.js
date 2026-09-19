// Obtiene el formulario y los datos ingresados por el usuario para realizar las validaciones
document.getElementById('uploadForm').addEventListener('submit', function(e) {
    const nombre = document.getElementById('nombreInput').value.trim();
    const paisaje = document.getElementById('paisajeInput').value.trim();
    const fileInput = document.getElementById('imageInput');
    const errorMsg = document.getElementById('errorMsg');

    // Limpia y oculta cualquier mensaje de error anterior
    errorMsg.classList.add('hidden');
    errorMsg.textContent = '';

    // Verifica que los campos de nombre y paisaje estén completos antes de enviar el formulario
    if (!nombre || !paisaje) {
        e.preventDefault();
        errorMsg.textContent = 'Por favor, verifica que los campos "nombres" o "paisaje favorito" esten completos';
        errorMsg.classList.remove('hidden');
        return;
    }

    // Verifica que el usuario haya seleccionado una imagen antes de enviar el formulario
    if (fileInput.files.length === 0) {
        e.preventDefault();
        errorMsg.textContent = 'Por favor, selecciona una imagen obligatoriamente.';
        errorMsg.classList.remove('hidden');
        return;
    }

    // Obtiene la imagen seleccionada y verifica que tenga un formato permitido
    const file = fileInput.files[0];
    const validTypes = ['image/jpeg', 'image/png', 'image/jpg'];

    if (!validTypes.includes(file.type)) {
        e.preventDefault();
        errorMsg.textContent = 'Formato inválido. Solo se permiten archivos JPG, JPEG o PNG.';
        errorMsg.classList.remove('hidden');
        return;
    }

    // Define un límite de 50 MB y verifica que la imagen no lo supere
    const maxSize = 50 * 1024 * 1024; // Límite de 50MB
    if (file.size > maxSize) {
        e.preventDefault();
        errorMsg.textContent = 'El archivo es muy pesado. El límite máximo es 50MB.';
        errorMsg.classList.remove('hidden');
        return;
    }
});