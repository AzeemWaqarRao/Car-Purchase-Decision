# Car Purchase Prediction App
This is a simple Streamlit app that predicts whether a person will buy a car or not based on their gender, age, and salary. The app uses a Random Forest Classifier model that was trained on a dataset of individuals and their car buying behavior.

## Getting Started
### Prerequisites<br>
To run the app, you will need the following installed on your machine:

Python 3.6+<br>
pip<br>
## Installing
To install the required Python libraries, navigate to the root directory of the project and run:

```
pip install -r requirements.txt
```
## Running the app
To run the app, navigate to the root directory of the project and run:

```
streamlit run app.py
```
This will start the Streamlit app in your default web browser.

## Usage
When you open the app, you will see a form where you can input the gender, age, and salary of a person. Once you submit the form, the app will use the trained SVM model to predict whether the person is likely to buy a car or not.

## Model Training
To train the Random Forest Classifier, we used a dataset of individuals and their car buying behavior. The dataset contains the following features:<br>

Gender (Male or Female)<br>
Age (in years)<br>
Salary (in USD)<br>
Car Purchased (Yes or No)<br>
We split the dataset into training and testing sets, with 70% of the data used for training and 30% for testing. We then trained a Random Forest Classifier on the training data and evaluated its performance on the testing data.


