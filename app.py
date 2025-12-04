from flask import Flask,request,render_template
import numpy as np
import pickle
from mangum import Mangum
model=pickle.load(open("model.pkl","rb"))
app=Flask(__name__)
handler=Mangum(app)
@app.route("/")
def wine():  
    return render_template('index1.html')
   
@app.route("/predict",methods=["POST"])
def wine1():
    Fixed_Acidity=eval(request.form.get("Fixed_Acidity"))
    volatile_Acidity=eval(request.form.get("volatile_Acidity"))
    citric_acid=eval(request.form.get("citric_acid"))
    residual_sugar=eval(request.form.get("residual_sugar"))
    chlorides=eval(request.form.get("chlorides"))
    free_sulfur_dioxide=eval(request.form.get("free_sulfur_dioxide"))
    total_sulfur_dioxide=eval(request.form.get("total_sulfur_dioxide"))
    density=eval(request.form.get("density"))
    PH=eval(request.form.get("PH"))
    Sulphates=eval(request.form.get("Sulphates"))
    alcohol=eval(request.form.get("alcohol"))
    result=model.predict(np.array([Fixed_Acidity,volatile_Acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,PH,Sulphates,alcohol]).reshape(1,11))
    if result[0]<=6:
        return "<h1 style='color:green'>Good,Yes Plz Drink</h1>"
    else:
        return "<h1 style='color:red'>Not Good,So Sorry</h1>"
app.run(debug=True)
