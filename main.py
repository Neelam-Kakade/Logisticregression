from flask import Flask, render_template ,request ,jsonify
from models import utils
import config


app= Flask(__name__)

@app.route("/")
def homeapi():
    return render_template("index.html")
    return "hello"

@app.route("/pred_disease")
def result_api():     #check name if error occurs
    
    request.method="GET"
    Glucose = request.args.get("Glucose")
    BloodPressure = request.args.get("BloodPressure")
    SkinThickness = request.args.get("SkinThickness")
    Insulin = request.args.get("Insulin")
    BMI = request.args.get("BMI")
    DiabetesPedigreeFunction = request.args.get("DiabetesPedigreeFunction")
    Age = request.args.get("Age")

    obj = utils.DiabetesTest(Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    result = obj.disease_pred()
    return render_template("index.html", result = result)


if __name__=="__main__":

     app.run(host = "0.0.0.0",port = config.PORT_NUMBER,debug=True)



    
    