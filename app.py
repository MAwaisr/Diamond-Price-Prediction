# local host address http://127.0.0.1:5000/
from flask import Flask, render_template, request, jsonify
from src.pipelines.prediction_pipeline import PredictPipeline, CustomData

import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form.html')
def show_form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Access the submitted form data
        carat = float(request.form['carat'])
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = 0
        y = 0
        z = 0
        cut = request.form['cut']
        color = request.form['color']
        clarity = request.form['clarity']

        # Create a CustomData object
        custom_data = CustomData(carat, depth, table, x, y, z, cut, color, clarity)

        # Get the data as a DataFrame
        features = custom_data.get_data_as_dataframe()

        # Predict using the PredictPipeline
        predictor = PredictPipeline()
        prediction = predictor.predict(features)

        # Render the result page with the prediction
        return render_template('result.html', prediction=int(prediction[0]))

    except Exception as e:
        # Handle exceptions
        return "An error occurred during prediction."

if __name__ == '__main__':
    app.run(debug=True)
