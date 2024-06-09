import cv2
import numpy as np

def moda(datos):
    valores, conteos = np.unique(datos, return_counts=True)
    indice_moda = np.argmax(conteos)
    return valores[indice_moda]

def main():
    # Ruta de la imagen que deseas procesar
    ruta_imagen = r"fotosPiel\piel2x1.png"
    
    # Cargar la imagen desde la ruta especificada
    imagen = cv2.imread(ruta_imagen)
    
    if imagen is None:
        print("Error al cargar la imagen.")
        return
    
    # Crear un objeto tipo CascadeClassifier para la detección de rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Convertir la imagen a escala de grises
    gris_imag = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Detectar caras en la imagen
    caras = face_cascade.detectMultiScale(gris_imag, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in caras:
        # Dibujar un rectángulo alrededor de la cara detectada
        cv2.rectangle(imagen, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Seleccionar solo el área donde hay una cara
        cara_area = imagen[y:y+h, x:x+w]
        hsv_cara = cv2.cvtColor(cara_area, cv2.COLOR_BGR2HSV)
        
        # Definimos los rangos de color de piel (ajusta según sea necesario)
        lower_skin = np.array([0, 10, 40], dtype=np.uint8)
        upper_skin = np.array([50, 150, 255], dtype=np.uint8)

        # Creamos una máscara para los tonos de piel
        mask = cv2.inRange(hsv_cara, lower_skin, upper_skin)
        skin = cv2.bitwise_and(cara_area, cara_area, mask=mask)

        # Extraer los canales H, S y V
        H, S, V = cv2.split(hsv_cara)

        # Calcular la moda de cada canal usando solo los píxeles enmascarados
        H_mascara = H[mask > 0]
        S_mascara = S[mask > 0]
        V_mascara = V[mask > 0]
        
        if H_mascara.size > 0 and S_mascara.size > 0 and V_mascara.size > 0:
            moda_H = moda(H_mascara)
            moda_S = moda(S_mascara)
            moda_V = moda(V_mascara)
            
            resultado_moda_hsv = (moda_H, moda_S, moda_V)

            # Convertimos la moda del color a RGB
            moda_rgb = cv2.cvtColor(np.uint8([[[moda_H, moda_S, moda_V]]]), cv2.COLOR_HSV2BGR)[0][0]
            moda_rgb = tuple(map(int, moda_rgb))
            
            print(f"El color en Moda RGB es: {moda_rgb}")
            
            # Dibujamos un parche de color en la imagen original
            color_patch_size = 50  # Tamaño del rectángulo
            cv2.rectangle(imagen, (10, 10), (10 + color_patch_size, 10 + color_patch_size), moda_rgb, -1)
        
            # Mostramos la imagen de la piel detectada
            cv2.imshow('Skin', skin)
    
    # Mostramos la imagen original con el rectángulo alrededor de la cara y el parche de color
    cv2.imshow('Imagen', imagen)
    
    # Esperamos a que se presione una tecla y luego cerramos las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

       


