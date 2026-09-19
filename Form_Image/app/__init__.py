# Importa las herramientas necesarias para crear la aplicación, manejar archivos y procesar imágenes
import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from PIL import Image

# Crea y configura la aplicación Flask
def create_app():
    app = Flask(__name__)
    
    # Define las carpetas donde se guardarán las imágenes originales y procesadas
    UPLOAD_FOLDER = 'app/static/uploads'
    PROCESSED_FOLDER = 'app/static/processed'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    # Guarda las rutas de las carpetas en la configuración de Flask
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

    # Crea las carpetas automáticamente si todavía no existen
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    # Verifica que el archivo tenga una extensión de imagen permitida
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    # Define la ruta principal y permite recibir formularios mediante GET y POST
    @app.route('/', methods=['GET', 'POST'])
    def index():

        # Comprueba si el formulario fue enviado mediante POST
        if request.method == 'POST':

            # Obtiene los datos de nombre y paisaje enviados desde el formulario
            nombre = request.form.get('nombre', '').strip()
            paisaje = request.form.get('paisaje', '').strip()
            
            # Verifica que el formulario haya enviado una imagen
            if 'image' not in request.files:
                return redirect(request.url)
            
            # Obtiene el archivo de imagen enviado por el usuario
            file = request.files['image']
            
            # Verifica que el usuario haya seleccionado un archivo
            if file.filename == '':
                return redirect(request.url)
            
            # Verifica que la imagen tenga una extensión permitida
            if file and allowed_file(file.filename):

                # Limpia el nombre del archivo para hacerlo seguro
                filename = secure_filename(file.filename)

                # Define la ubicación donde se guardará la imagen original
                input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Guarda la imagen original en la carpeta de cargas
                file.save(input_path)
                
                # Obtiene el tamaño original de la imagen en bytes
                orig_size_bytes = os.path.getsize(input_path)
                
                # Define el nombre y ubicación de la imagen optimizada
                output_filename = 'opt_' + filename
                output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
                
                # Abre la imagen y realiza el proceso de optimización con Pillow
                with Image.open(input_path) as img:
                    orig_format = img.format
                    width, height = img.size
                    img.thumbnail((800, 800))
                    img.save(output_path, optimize=True, quality=80)
                    
                # Obtiene el tamaño de la imagen después de la optimización
                opt_size_bytes = os.path.getsize(output_path)
                
                # Convierte el tamaño de bytes a KB o MB para mostrarlo al usuario
                def format_size(size_in_bytes):
                    if size_in_bytes >= 1024 * 1024:
                        return f"{round(size_in_bytes / (1024 * 1024), 2)} MB"
                    else:
                        return f"{round(size_in_bytes / 1024, 2)} KB"

                # Calcula qué porcentaje del tamaño original se redujo
                reduction_pct = round((1 - (opt_size_bytes / orig_size_bytes)) * 100, 1) if orig_size_bytes > 0 else 0

                # Prepara los datos obtenidos para mostrarlos en la página HTML
                metrics = {
                    'nombre': nombre,
                    'paisaje': paisaje,
                    'filename': filename,
                    'format': orig_format,
                    'dimensions': f"{width} x {height} px",
                    'orig_size': format_size(orig_size_bytes),
                    'opt_size': format_size(opt_size_bytes),
                    'reduction': f"{reduction_pct}%"
                }
                
                # Envía los resultados del procesamiento al archivo HTML
                return render_template('index.html', metrics=metrics)
                
        return render_template('index.html')

    return app