import os
import cv2
import numpy as np
import threading
from tqdm import tqdm
from queue import Queue
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalMaxPooling2D
import pickle

# Definir las funciones de procesamiento de imágenes
def recortar_cara(imagen):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cara_recortada = imagen[y:y+h, x:x+w]
        return cara_recortada
    return None

def caracteristicas_imagen(cara_recorte, modelo):
    imagen = cv2.resize(cara_recorte, (224, 224))
    imagen_array = image.img_to_array(imagen)
    imagen_extendida = np.expand_dims(imagen_array, axis=0)
    imagen_procesada = preprocess_input(imagen_extendida)
    resultado = modelo.predict(imagen_procesada).flatten()
    normalizado = resultado / np.linalg.norm(resultado)
    return normalizado

def cargar_imagen(file, queue):
    imagen = cv2.imread(file)
    queue.put((file, imagen))

ruta_carpeta_imagenes =r"C:\Users\ponerCarpetadondeEstanImagenes\train\image"

# Cargar el modelo ResNet50 preentrenado
modelo_base = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
modelo_base.trainable = False
modelo = Model(inputs=modelo_base.input, outputs=GlobalMaxPooling2D()(modelo_base.output))

# Listar los archivos en el directorio de imágenes
filesname = []
for file in os.listdir(ruta_carpeta_imagenes):
    #para windows (modificar si es necesario)
    filesname.append(ruta_carpeta_imagenes+"\\" + file)

print(f"Número de archivos: {len(filesname)}")

# Procesar cada imagen y extraer características
listas_caracteristicas = []

# Usar tqdm para mostrar una barra de progreso
for file in tqdm(filesname, desc="Procesando imágenes"):
    # Crear una cola para el subproceso
    queue = Queue()

    # Iniciar el subproceso para cargar la imagen
    t = threading.Thread(target=cargar_imagen, args=(file, queue))
    t.start()

    # Esperar hasta que el subproceso termine o se agote el tiempo (10 segundos)
    t.join(timeout=10)

    # Obtener la imagen del subproceso (si se ha cargado)
    if not queue.empty():
        filename, imagen = queue.get()
        if imagen is None:
            print(f"No se pudo cargar la imagen: {filename}")
            listas_caracteristicas.append(None)
            continue
    else:
        print(f"El tiempo de espera ha expirado para la imagen: {file}")
        listas_caracteristicas.append(None)
        continue

    cara_recorte = recortar_cara(imagen)
    if cara_recorte is not None:
        # Extraer características de la cara recortada
        caracteristicas = caracteristicas_imagen(cara_recorte, modelo)
        listas_caracteristicas.append(caracteristicas)
    else:
        print(f"No se encontró ninguna cara en la imagen: {file}")
        listas_caracteristicas.append(None)

pickle.dump(listas_caracteristicas,open("lista_Caracteristicas.pkl","wb"))
pickle.dump(filesname,open("lista_nombre.pkl","wb"))