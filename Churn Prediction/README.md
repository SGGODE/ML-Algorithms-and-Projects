# Customer Churn Prediction

This repository contains a machine learning model for predicting customer churn in a telecommunications company. Customer churn prediction is a crucial task for businesses, as it helps them identify customers who are likely to leave and take proactive steps to retain them.
### Live : https://predictor-w6mq.onrender.com/
## Dependencies
To run this project, you'll need the following Python libraries installed:

- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask

You can install these dependencies using pip with the following command:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn flask
```

## Dataset
The dataset used in this model can be found in the data folder. It contains historical customer data, including various features such as account information, usage patterns, and customer demographics. Make sure to explore and preprocess the data as necessary before training the model.

## Model Architecture
The Customer Churn Prediction model is built using a logistic regression algorithm from scikit-learn. Logistic regression is a popular choice for binary classification problems like churn prediction because it provides a probability of a customer churning.

## Usage
Follow these steps to use this project:

Install Dependencies: Ensure that you have installed all the required dependencies mentioned above.

Explore and Preprocess Data: Explore the dataset in the data folder and preprocess it if required. Data preprocessing might involve handling missing values, encoding categorical variables, and splitting the data into training and testing sets.

Train the Model: Train the customer churn prediction model using the Customer Churn Prediction.py script. You can do this by running the following command:

```bash
python "Customer Churn Prediction.py"
```
### Evaluation: 
Once the model is trained, you can evaluate its performance using various metrics such as accuracy, precision, recall, and F1-score. You may customize the evaluation metrics according to your specific business needs.

### Deployment: 
This model is deployed using Flask, HTML, and CSS. You can find the deployment files and instructions in the deployment folder. Deploy the model to make real-time predictions or integrate it with your application.

## Deployment
The deployment of this model involves using Flask to create a web application for making predictions. The Flask app serves HTML and CSS files for the user interface and utilizes the trained model to predict churn. 

Feel free to customize and adapt this project to suit your specific needs and requirements. Happy predicting!
