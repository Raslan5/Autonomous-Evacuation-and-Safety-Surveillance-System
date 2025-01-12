# Autonomous Evacuation and Safety Surveillance System

This project develops the features of a multimodal autonomous system that integrates data from
sound sensors, cameras, and electricity usage to assess the safety of neighborhoods and houses,
specifically Lebanese evacuated houses due to the war.

## Module 1 - Threatening Sound Detection and Classification 
The first module focuses on detecting potential airstrikes by analyzing sound patterns captured from a microphone using machine learning. 
The system is trained to classify audio inputs in real-time as either "casual" or "uncasual", distinguishing sounds like explosions or gunshot. 
This functionality is critical for emergency response and evacuation planning in conflict zones.
By leveraging a diverse dataset of audio samples, the model is designed to be robust and reliable, ensuring accurate detection relevant to situation of Lebanon. 

 - `gru.pth`: A pre-trained model using a GRU (Gated Recurrent Unit) architecture for classifying whether a sound is casual or uncasual. This serves as the first step in identifying potentially suspicious sounds.
 - `RNN_Module.ipynb`: A Jupyter Notebook for implementing and training the GRU-based RNN model (gru.pth) to classify sounds as casual or uncasual. It focuses on processing time-series audio data.
 - `resnet.pth`: A pre-trained ResNet model used to classify uncasual sounds into specific types such as gunshots, explosions, or airstrikes.
 - `ResNet_Module.ipynb`: A Jupyter Notebook for implementing and training the ResNet model (resnet.pth) to classify specific types of uncasual sounds. This is executed after the RNN model detects an uncasual sound and handles audio features.
 - `Overall_Model_1_Architecture.ipynb`: A Jupyter Notebook that combines the GRU-based RNN model and ResNet-based classification model into a unified framework. This file integrates the functionality of both RNN_Module and ResNet_Module to streamline the sound classification pipeline.

## Module 2 - Suspicious Activity Feedbacks
The second module uses YOLOv11 for object detection. The pre-trained by 25 epochs model file, mod2.pt, is designed to detect suspicious objects and activities, 
such as weapons and masked individuals. The predict_mod2.py script allows users to perform predictions on images, videos, or webcam feeds, with results displayed and saved automatically. 
For those looking to train the model further, train_mod2.ipynb provides a customizable framework to train YOLOv11 using a custom dataset, 
enabling adjustments to hyperparameters like confidence thresholds and epochs.

 - `mod2.pt`: A pre-trained by only 25 epochs YOLOv11 model for detecting suspicious objects and activities such as weapons, masked individuals, and more.
 - `predict_mod2.py`: A Python script for performing predictions using the YOLO model (mod2.pt).
 - `train_mod2.ipynb`: A Jupyter Notebook used for training the YOLO model after manipulating and unifying the datasets.

## Module 3 - Electricity Safety 
The third module focuses on detecting potential electricity theft in households by analyzing electricity usage patterns using machine learning.  
The module includes steps for preprocessing the data, engineering features such as usage trends and anomalies, and training a machine learning model to detect irregularities.

 - `Electricity_Usage_Levels_Model_3.ipynb`: This notebook is designed to process historical power consumption data to classify whether the electricity usage is legitimate or indicates possible theft.
 - `power_theft_model`: A pre-trained model for the electricity possible theft detection.
