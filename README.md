# Diamond Price Prediction Machine Learning Project

This machine learning project focuses on predicting the price of diamonds based on features like carat, depth, and table. The project utilizes a machine learning model and integrates it into a web application using Flask, providing a user-friendly interface to predict diamond prices.

## Dataset

## Dataset

The dataset used for this project contains the following columns:
- `carat`: The weight of the diamond (in carats)
- `depth`: Total depth percentage (as a percentage of diameter)
- `table`: Width of the top of the diamond relative to the widest point (in percentage)
- `color`: Color of the diamond (ranging from D to J, with D being the most colorless and J having noticeable color)
- `clarity`: A measurement of how clear the diamond is (ranging from I1 to IF.
- `cut`: Quality of the cut of the diamond (options: Fair, Good, Very Good, Premium, Ideal)
- `price`: Price in USD (the target variable to be predicted)

The goal of the project is to predict the price of a diamond based on these features.

...


## Running the Application

1. Ensure you have Python installed on your system.

2. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
3. To Run the app.py file from terminal, write:
    ```bash
    python app.py


## Model Performance

Multiple models like linear, ridge, lasso and Elastic Net are used. Linear regression shows best results with R2 score of around 92.48% on given dataset.