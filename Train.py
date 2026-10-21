from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('yolo11n.pt')

    results = model.train(
        data='deteccion-muebles-yolo\DataSet\data.yaml', 
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        project='Resultados_Entrenamiento', 
        name='prueba_muebles_v1'             
    )