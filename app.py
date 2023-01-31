from flask import Flask
import pickle

app = Flask(__name__)
model = pickle.load(open('savedmodel.sav','rb'))

@app.route('/')
def home():
    result=''
    return render_template('home.html',**local)