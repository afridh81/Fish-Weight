import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Fish_weight1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Species = request.form['Species']
    if (Species == 'Bream'):
        Bream = 1
        Roach = 0
        Whitefish = 0
        Parkki = 0
        Perch = 0
        Pike = 0
        Smelt = 0
    elif (Species == 'Roach'):
        Bream =0
        Roach = 1
        Whitefish = 0
        Parkki = 0
        Perch = 0
        Pike = 0
        Smelt = 0
    elif (Species == 'Whitefish'):
        Bream =0
        Roach = 0
        Whitefish = 1
        Parkki = 0
        Perch = 0
        Pike = 0
        Smelt = 0
    elif (Species == 'Parkki'):
        Bream =0
        Roach = 0
        Whitefish = 0
        Parkki = 1
        Perch = 0
        Pike = 0
        Smelt = 0
    elif (Species == 'Perch'):
        Bream =0
        Roach = 0
        Whitefish = 0
        Parkki = 0
        Perch = 1
        Pike = 0
        Smelt = 0
    elif (Species == 'Pike'):
        Bream =0
        Roach = 0
        Whitefish = 0
        Parkki = 0
        Perch = 0
        Pike = 1
        Smelt = 0
    elif (Species == 'Smelt'):
        Bream = 0
        Roach = 0
        Whitefish = 0
        Parkki = 0
        Perch = 0
        Pike = 0
        Smelt = 1
    length1=float(request.form["Length1"])
    length2 = float(request.form["Length2"])
    length3 = float(request.form["Length3"])
    height = float(request.form["Height"])
    width = float(request.form["Width"])
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    prediction = model.predict([[height,width,length3,length2,length1,Bream,Roach,Whitefish,Parkki,Perch,Pike,Smelt]])

    output = abs(round(prediction[0], 2))

    return render_template('index.html', prediction_text='Weight of fish$ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)