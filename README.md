##Algerian Forest Fire Prediction Model

This project is a machine learning model that predicts the likelihood of forest fires occurring in Algeria based on various environmental and climatic factors. The model is trained using historical data on weather conditions and fire occurrences, helping to provide early warnings for fire-prone areas.

#Description

This machine learning model uses the Algerian Forest Fire dataset to predict the likelihood of forest fires in Algeria. The dataset includes features such as temperature, humidity, wind speed, and month of the year, which are important factors in forest fire occurrences.

The model was built using Random Forest or Logistic Regression, or another suitable algorithm. It is intended to aid in predicting when and where forest fires are most likely to occur based on weather conditions.

##Installation

To run the Algerian Forest Fire Prediction model on your local machine, follow these steps:

1. Clone the repository:
    git clone https://github.com/yourusername/AlgerianForestFireModel.git
    cd AlgerianForestFireModel

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required libraries:
    pip install -r requirements.txt

This will install the necessary dependencies for running the project.

Dependencies in `requirements.txt`:
numpy~=1.26.4
flask~=3.0.3
matplotlib
pandas
scikit-learn
seaborn

#Usage

To run the forest fire prediction model, follow these steps:

1. Ensure that you have installed all dependencies by running the `pip install -r requirements.txt` command.

2. Run the model using a script (for example, `predict_fire.py`). Here is how you can use the model:

    python predict_fire.py --temperature 30 --humidity 45 --wind_speed 12 --month 7

    The model will predict whether a fire is likely to occur based on the provided features (temperature, humidity, wind speed, and month).

    Example output:
    Predicted result: High risk of fire


#Model

The forest fire prediction model uses a machine learning algorithm (such as Random Forest, Decision Trees, or Logistic Regression) to classify or predict the likelihood of a fire. Here are the key details:

- Algorithm Used: Random Forest / Logistic Regression
- Training Data: The model was trained on historical fire data (as provided by the Algerian Forest Fire dataset).
- Features Used: Temperature, Humidity, Wind Speed, and Month (among others).

Hyperparameters:
- Random Forest:
    - Number of Trees: 100
    - Maximum Depth: 5
    - Criterion: Gini impurity
- Logistic Regression:
    - Regularization: L2
    - Solver: liblinear


#Contributing

We welcome contributions! If you'd like to improve the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

