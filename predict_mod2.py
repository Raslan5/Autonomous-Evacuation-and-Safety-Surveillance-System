from ultralytics import YOLO
model = YOLO("mod2.pt") # use the trained model

# source to 0 for local webcam 
model.predict(source= "sample", show=True,
            save = True, conf=0.2, line_thickness=2,
            line_width=2,   
            show_labels= True,
            show_conf = False, 
            ) 
