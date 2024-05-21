import cv2
import numpy as np


def main():
    
    # creamos un objeto tipo CascadaClassifier, como argumento metemos las ruta de las haarcascades
    # y el archivo específico donde se guarda los datos para reconocer caras (XML)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # luego  debemos capturar el video  para ello seleccionamos nuestra camara, por defecto 0
    cap = cv2.VideoCapture(0)
  
    
    while True:
        
        # cap read guarda un frame(frame) y si esta operación fue exitosa (success)
        sucess, frame = cap.read()
        #si no, no ejecuta lo de abajo
        if not sucess:
            break
        
        # para la deteccion de rostros es necesario tener la imagen en grises por lo que creamos una imagen en grises
        gris_imag = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # faces almacena un arreglo de 4 valores, una posición en x y y, y w y h que es ancho y altura
        # en este caso se usa los valores para crear un poligono de 4 lados alrededor de la cara
        # es necesario pasar la imagen en gris, scale factor es el escalado que se hace para reconocer caras de diferente tamaño
        # se necesita 5 detecciones para confirmar el rostro y minSize descarta las caras menores a este tamaño
        cara = face_cascade.detectMultiScale(gris_imag, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # dibujamos un rectangulo en el frame y donde se reconoce la cara
        for (x,y,w,h) in cara:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Seleccionamos solo el area donde hay una cara
            cara_area = frame[y:y+h, x:x+w]
        
        # cambiamos la cara_area(RGB) a (hsv)
            hsv_cara = cv2.cvtColor(cara_area, cv2.COLOR_BGR2HSV)
            
            #definimos los rango de color que detectara, probar para cada caso y ajustar valores 
            lower_skin = np.array([0, 10, 40], dtype=np.uint8)
            upper_skin = np.array([50, 150, 255], dtype=np.uint8)
            
            mask = cv2.inRange(hsv_cara, lower_skin, upper_skin)
            
            skin = cv2.bitwise_and(cara_area, cara_area, mask=mask)
            
            average_color = cv2.mean(cara_area, mask=mask)[:3]
            
            average_color_rgb = tuple(map(int, (average_color[2], average_color[1], average_color[0])))
            
            
            print(f"El color en RGB es: {average_color}")
            
            color_patch_size = 50  # Tamaño del rectángulo
            cv2.rectangle(frame, (10, 10), (10 + color_patch_size, 10 + color_patch_size), average_color_rgb, -1)
        
            
    
            cv2.imshow('Skin', skin)
            
        cv2.imshow('Video', frame)
        
        
        
        
        
        # Salir del bucle presionando q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
        
    
if __name__ == "__main__":
    main()