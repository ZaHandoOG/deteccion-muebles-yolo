import cv2
from ultralytics import YOLO

if __name__ == '__main__':
    ruta_modelo = 'deteccion-muebles-yolo\DataSet\prueba_muebles_v1-3\weights\best.pt'
    model = YOLO(ruta_modelo)

    #Pon aquí la ruta de una foto de algún mueble para probar
    ruta_imagen_prueba = ''

    resultados = model(ruta_imagen_prueba)

    for resultado in resultados:
        imagen_anotada = resultado.plot() 
        cv2.imshow("Detecciones de YOLO", imagen_anotada)

    cv2.waitKey(0)
    cv2.destroyAllWindows()