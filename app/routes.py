from flask import render_template,request
from app import app
from .model import get_recommendation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping',methods=['GET'])
def ping():
    return "Hello", 200
@app.route('/recommend',methods=['POST'])
def recommend():
    user_input=request.form['user_input']
    recommendations=get_recommendation(user_input)
    return render_template('results.html',recommendations=recommendations.to_dict(orient='records'))