from flask import Flask, render_template, request
import joblib

loaded_model=joblib.load('dib_75.pkl')

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/predict',methods=['POST'])
def predict():
    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')
    print( preg,plas,pres,skin,test,mass,pedi,age,'are the values of the variables')
    print(type(preg))
    prediction = loaded_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    print(prediction)
    if prediction[0]==1:
	    result='Diabetic'
        #print('The result of the prediction is :')
    else:
        result='Not Diabetic'
        #print('The result of the prediction is :')
    #return( result, 'is the result')
    return render_template('results.html', value = result)

if __name__=='__main__':
    app.run(debug=True)