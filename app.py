from flask import Flask, request
from flask import render_template
import pickle
import numpy as np
app=Flask(__name__)



"""@app.route('/', methods=['GET','POST'])

def index():
    if request.method =='POST' :
        model=pickle.load(open('model.pkl', 'rb'))
        inp=request.form.get('V1')
        inp=float(inp)
        inp=np.array(inp)
        inp=inp.reshape(-1,1)
        predic=model.predict(inp)

    if request.method=='GET':
        return "Hello World"
    if request.method=='POST':
        data=request.form
        return render_template('base.html', form_data=form_data)"""

@app.route('/')
def my_form():
    return render_template('base.html')

@app.route('/', methods=['GET','POST'])
def my_form_post():
    if request.method=='POST':
        text = request.form['text']
        processed_text = text.upper()
        return processed_text

@app.route('/onlyget/users/<string:name>/posts/<int:id>')
def get(name,id):
    return "Hellow " +name+"your id is" +str(id)


if __name__=="__main__":
    app.run(debug=True)

    