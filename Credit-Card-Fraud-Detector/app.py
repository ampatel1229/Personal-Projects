from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import pickle

# ----------------------------------
# Credit Card Fraud Detector Web App
# ----------------------------------

#Creating flash application
#__name__ tells Flash where it should look for templates(HTML)/static(CSS) files
app = Flask(__name__)

#Loads the model and scaler when the app starts
#Happens once when you run the app, not every time someone makes a prediction
print("Loading model and scaler...")

# Open the saved model file in 'read binary' mode
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
    print("Model loaded successfully!")

#Open the scaler file
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file) #load the StandardScaler
    print("Scaler loaded successfully!")

@app.route('/')
#Defining homepage route
def home():
    #renders main page of application; render_template() looks for the html file in the templates folder
    return render_template('index.html')

#Defining prediction route
@app.route('/predict', methods=['POST'])
def predict():
    """
    Funtion Process:
    1. Gets the transaction data from the form
    2. Scales the numeric values of the data
    3. Makes a prediciton based on our trained model
    4. Returns the result to the user
    """

    try:
        #request.form is a directory containing all the input values; must convert to floats as they start out as strings

        #Time and Amount Transactions
        time = float(request.form['time'])
        amount = float(request.form['amount'])

        v_feat = []
        for i in range(1, 29):
            feature_name = f'v{i}'
            v_feat.append(float(request.form[feature_name]))

        #Combining the features into one list (corrected order)
        features = [time] + v_feat + [amount]

        #Convert to numpy array and resize to 2D array
        #reshape(1, -1) means: 1 row and auto-calculate columns
        features_array = np.array(features).reshape(1, -1)

        #Create DataFrame with proper column name
        #Important since our scaler was trained on specific columns
        feature_names = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
        features_df = pd.DataFrame([features], columns=feature_names)

        #Scaling time and amount
        features_scaled = features_df.copy()

        features_scaled.loc[:, ['Time', 'Amount']] = scaler.transform(features_df[['Time', 'Amount']])

        #Make the prediciton of fraud
        prediction = model.predict(features_scaled)[0]

        # Get the probability of fraud
        # predict_proba() returns [prob_of_0, prob_of_1]
        probability = model.predict_proba(features_scaled)[0][1]

        #Determine results
        if prediction == 1:
            result = "FRAUDULENT TRANSACTION 🚨"
            result_class = "fraud"
        else:
            result = "LEGITIMATE TRANSACTION ✅"
            result_class = "legitimate"
        
        confidence = f"{probability * 100:.2f}%"

        return render_template('index.html', 
                               prediction_text=result, 
                               probability_text=f"Fraud Probability: {confidence}", 
                               result_class=result_class,
                               showResult=True)
    except KeyError as e:
        # If a form field is missing
        error_msg = f"Missing form field: {str(e)}"
        return render_template('index.html', error=error_msg)
    except ValueError as e:
        # If a value can't be converted to float
        error_msg = f"Invalid input value: {str(e)}"
        return render_template('index.html', error=error_msg)
    except Exception as e:
        # Catch any other unexpected errors
        error_msg = f"An error occurred: {str(e)}"
        return render_template('index.html', error=error_msg)
    
    # Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000) #Starts the Flask Server

    """
    This block only runs if you execute this file directly (python app.py)
    debug=True enables:
    - Auto-reload when you change code
    - Detailed error messages
    """

    print("\n" + "=" * 50)
    print("Starting Credit Card Fraud Detection App!")
    print("=" * 50)
    print("Open your browser and go to: http://127.0.0.1:5000/")
    print("Press CTRL+C to stop the server")
    print("=" * 50 + "\n")
    

