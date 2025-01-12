<<<<<<< HEAD:module_2/predict_mod2.py
from ultralytics import YOLO
model = YOLO("best.pt") # use the trained model

# source to 0 for local webcam 
model.predict(source= "sample", show=True,
            save = True, conf=0.2, line_thickness=2,
            line_width=2,   
            show_labels= True,
            show_conf = False, 
            ) 
=======
from ultralytics import YOLO
model = YOLO("mod2.pt") # use the trained model

# source to 0 for local webcam 
model.predict(source= "sample", show=True,
            save = True, conf=0.2, line_thickness=2,
            line_width=2,   
            show_labels= True,
            show_conf = False, 
            ) 
>>>>>>> 50a6eb3b45d4d6c2493053a2c09d0ff6a2c28cdb:predict_mod2.py
