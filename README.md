cat_recognition

Este repositorio usa el framework [ImageAI](https://github.com/OlafenwaMoses/ImageAI) para analizar automáticamente las imágenes en el directorio `data/raw` y busca gatos en las imágenes.

Las identificaciones positivas se guardan a la carpeta `data/processed/cat_detected` y en caso de no haber detección crea una copia en el directorio `data/processed/not_cat_detected`.


## Como usar?

- Clona el repositorio: ```git clone https://github.com/IslasGECI/cat_recognition.git```
- Genera el contenedor usando el Dockerfile

- Guarda las imágenes con gatos que quieras analizar en el directorio `data/raw`

- Corre la instrucción `make process_images`

- Listo!


## Futuras tareas

- Utilizar los distintos modelos: yolo, retinaIA y otro.
