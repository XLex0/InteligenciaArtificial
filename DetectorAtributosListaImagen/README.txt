Funcionalidad: Recomendar Ropa en base a atributos faciales

Requisitos: 2 Carpetas de imagenes en nuestro caso. La primera 
son las imagenes que serán procesadas y la otra las imágenes que se 
mostrarán de acuerdo a las características obtenidas de la primera.
Se debe tener en ambas carpetas un relacion biyectiva, es decir, a cada 
imagen de la carpeta A le corresponde solo una imagen de la carpeta B.
Estas 2 imagenes tendrán el mismo nombre para facilidad. Solo estarán en
directorios distintos.
Formato jpg o similares

Se tiene 2 programas de python, el primero Detector_Imagen_Atributos.py
se encarga de analizar una cantidad exorbitante de fotos y genera un arreglo
con los 2048 atributos de cada imagen, esto se guarda en un arreglo.
El segundo programa solo procesa una foto y en base a sus atributos compara
los 6 elementos más cercanos, en base a los atributos y devuelve la ruta de estas 
6 imagenes. 
Por ultimo cambiamos la carpeta de la imagen, para que nos muestre la imagen de 
la prenda y no de la modelo.

¿Cómo usar?
Se uso un dataset de Kaggle con las características dadas: VITON_HD
en nuestro caso, usaremos images y cloth de la carpeta train
Pondremos la ruta de images

Nota:
----------------------------------------------------------------------
Ver como conectar con java para usar jade 
----------------------------------------------------------------------
Solo debería retornar la ruta, sin embargo, para las pruebas se incorpora
cv2, para mostrar la imagen
----------------------------------------------------------------------