from flask import Flask, request, redirect, url_for, flash, jsonify
import pickle as p
import numpy as np
import json


app=Flask(__name__)

@app.route('/prediction',methods=['POST'])

def make():
    data=request.get_json()
    prediction= np.array2string(model.predict(data))

    return jsonify(prediction)


if __name__ == '__main__':
    modelfile = 'diabetes_model.pkl'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')
