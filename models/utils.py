import json
import numpy as np
import pickle
import config

class DiabetesTest():
    def __init__(self,Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    def load_model(self):        
        
        with open(config.Model_Path,"rb") as f:
            self.model=pickle.load(f)

        with open(config.Json_Data, "r") as f:
            self.json_data = json.load(f)
    
    def disease_pred(self):
        
        self.load_model()

        arr = np.zeros(len(self.json_data["columns"]))
        arr[0] = self.Glucose
        arr[1] = self.BloodPressure
        arr[2] = self.SkinThickness
        arr[3] = self.Insulin
        arr[4] = self.BMI
        arr[5] = self.DiabetesPedigreeFunction
        arr[6] = self.Age
    
        result = self.model.predict([arr])[0]
        print(result)

        if result == 1:

            return "Diabetes Not Detected."
        else:
            return "Diabetes Dectected"

if __name__=="__main__":
    
    Glucose = 150
    BloodPressure = 0
    SkinThickness = 0
    Insulin = 0
    BMI = 35.5
    DiabetesPedigreeFunction = 0.134
    Age = 29

    obj = DiabetesTest(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    obj.disease_pred()


