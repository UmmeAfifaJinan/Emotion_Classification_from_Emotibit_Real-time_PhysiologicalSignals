
# Emotion Classification with Emotibit Physiological Data in Real-Time

This project implements a real-time system to classify emotions based on physiological signals collected from the EmotiBit device. The system establishes a UDP connection to receive ECG (Electrocardiography) and GSR (Galvanic Skin Response) data, processes the data using various machine learning classifiers, and predicts emotions based on these inputs.

## Overview

The project is composed of multiple Python scripts, each serving a specific function in the data collection, processing, and emotion classification pipeline.

1. client.py

Purpose: 
Initiates a UDP connection to the server to send and receive physiological data.

Functionality:
Connects to the server, which receives real-time physiological signals from the EmotiBit device.
Sends a predefined message to verify the connection. 

2. server.py

Purpose: Acts as a server to receive physiological data from the EmotiBit device via UDP.
Functionality:
Receives ECG and GSR signals from the EmotiBit device.
Logs data into CSV files for further analysis.
The script is a base version, which can be extended to include more complex data processing tasks or forwarding data to machine learning models for real-time analysis. 

3. ML_models.py

Purpose: Implements machine learning models for emotion classification based on the physiological data.
Functionality:
The script includes six classic machine learning classifiers:

   Support Vector Machine (SVM)

   Random Forest

   Stochastic Gradient Descent (SGD) Classifier

   K-Nearest Neighbors (KNN)

   Gradient Boosting Classifier

   Logistic Regression

Models are trained, tested, and validated on the data, providing performance metrics such as F1 score, precision, recall, and others.

The models are then used for real-time emotion classification based on incoming physiological signals.


4. server_real_time_prediction.py

Purpose: An enhanced version of server.py, integrating machine learning for real-time emotion prediction.

Functionality:
Establishes a UDP connection to receive real-time data from the EmotiBit device.

Applies preprocessing to the incoming data and predicts emotions using the machine learning models defined in ML_models.py.

Outputs predictions along with various performance metrics for real-time feedback.

5. examplecode_fixedDataset.py

Purpose: Demonstrates how to classify emotions using machine learning models with a predefined dataset.

Functionality:
Loads a predefined dataset that simulates the kind of data received from the EmotiBit device.
Trains, tests, and validates emotion classification models using the dataset.

Provides a reference for understanding how the system works with real-time data in a more controlled environment.

## Instructions 

### Steps

1. **Start the Server**:
   
   Run server_real_time_prediction.py to start the server and begin receiving physiological data from the EmotiBit device.
   
2. **Connect the Client**:
   
   Run client.py to establish a connection with the server and start sending data.

3. **Machine Learning Prediction**:
   
   The server will process the incoming data, apply machine learning models, and output the predicted emotions.

4. **Example with Predefined Dataset**:
   
   Run examplecode_fixedDataset.py to see how the system performs emotion classification using a fixed dataset.

## Project Structure

- client.py: Client script to send data to the server.
- server.py: Server script to receive and log physiological data.
- ML_models.py: Machine learning models and pipeline for emotion classification. 
- server_real_time_prediction.py: Server script with real-time emotion prediction capabilities. 
- examplecode_fixedDataset.py: Example script for emotion classification using a predefined dataset. 

## Contributing 
- Contributions are welcome! Please feel free to submit issues or pull requests. 

---

For more information or inquiries, contact [Umme Afifa Jinan](mailto:ujinan@students.kennesaw.edu).


