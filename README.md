# ml_stroke_predictor

The final web application: https://bit.ly/ml-stroke-predictor-sahil

A web application that predicts the percentage likeliness of stroke occurrence in patients with special emphasis on the impact of various treatments done on the parent dataset on the accuracy of the ML model.

For choosing the most accurate model, the parent dataset went through various treatments to yield 7 derived datasets. These treatments included label encoding of categorical variables, handling missing values using different techniques, oversampling of data, outlier treatments, etc. All 7 datasets with 5000+ entries were feature-engineered using python and then trained as ML Classification Models using Google Cloud Platform's Vertex AI. Next, the most accurate model was chosen to be used for prediction in the web application.

The final prediction is done by passing the data input by the user as a JSON file with the help of a cloud function using POST API to the chosen ML classification model. The model returns the percentage value of the likeliness of stroke occurrence. The web application then directs the user to useful links regarding the symptoms and causes, diagnosis and treatment, and recovery for stroke patients.
