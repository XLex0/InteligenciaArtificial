import pickle
import numpy as np
import cv2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import GlobalMaxPooling2D
from sklearn.neighbors import NearestNeighbors

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

# Cargar los datos filtrados
lista_atributos = np.array(pickle.load(open("lista_Caracteristicas_filtrada.pkl", "rb")))
lista_nombres = pickle.load(open("lista_nombre_filtrada.pkl", "rb"))

print(f"Shape de lista_atributos: {lista_atributos.shape}")

# Ruta de la imagen de prueba
ruta_test = r"C:\Users\Xelan\Downloads\archive\test\image\14222_00.jpg"
resultado = True
imagen = cv2.imread(ruta_test)

# Inicializar el modelo ResNet50 preentrenado
modelo_base = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
modelo_base.trainable = False
modelo = Model(inputs=modelo_base.input, outputs=GlobalMaxPooling2D()(modelo_base.output))

if imagen is None:
    resultado = False
else:
    cara_recortada = recortar_cara(imagen)
    if cara_recortada is None:
        resultado = False
    else:
        atributos = caracteristicas_imagen(cara_recortada, modelo)

if resultado:
    print(f"Longitud de los atributos: {len(atributos)}")

    # Inicializar el modelo de vecinos más cercanos
    neighbors = NearestNeighbors(n_neighbors=6, algorithm="brute", metric="euclidean")
    neighbors.fit(lista_atributos)

    # Encontrar los vecinos más cercanos
    distancia, indices = neighbors.kneighbors([atributos])
    cv2.imshow("original",imagen)
    cv2.waitKey(0)

    # Mostrar los nombres de las imágenes más cercanas
    for i in indices[0]:
        imagen_temp =cv2.imread(lista_nombres[i])
        cloth = lista_nombres[i].replace("image","cloth")
        print (cloth)
        ropa = cv2.imread(cloth)
        cv2.imshow("ropa", ropa)
        cv2.imshow("modelo", imagen_temp)
        cv2.waitKey(0)
else:
    print("No se pudo procesar la imagen.")
