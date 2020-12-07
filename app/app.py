# Import the necessary libraries

from flask import Flask, request, jsonify, make_response
import json

import sys
sys.path.insert(1, '/app')



# Create instance of the Flask class
app = Flask(__name__)


# Define API routes

# 1. Home route. "Alive" message printed to make sure the server is running.
@app.route('/', methods=['GET'])
def alive():
    return """<h1>Alive!</h1> 
    <a href= '/predict'>Let's use this API!</a>"""

# 2. Route (/predict). Get method shows the JSON schema that the user should follow to send the data.
@app.route('/predict', methods = ['GET','POST'])
def predict():
    # 2.1. Request method: POST (retrieve data inputed by user)
    if request.method == 'POST':
        if request.is_json:
            json_input = request.get_json(force=True)

            # Import the necessary modules
            # from preprocessing.cleaning_data import preprocess
            # from predict.prediction import predict

            #json_input_cleaned = preprocess(json_input)
            #prediction, error = predict(json_input_cleaned) # ADD ACCURACY

            #if error:
            #    response = {
                    #"prediction": f"{prediction}"
                    # accuracy_based_on_ADD ACCURACY
            #        "error": f"{error}"
            #    }
            #else:
            #    response = {
            #        "prediction": f"{prediction}"
                    # ADD ACCURACY
                    # "error": # ?
            #    }

            json_output = make_response(jsonify(response), 200) # 200


            return json_output

        else:
            response = make_response(jsonify({"message":"Sorry, no JSON data was received"}), 400)
            return response

    # 2.2. Request method: GET. JSON schema used to send data (user) and validate instances (HOW TO SAY "US")??
    else:
        from json_schema_dir.json_schema_file import json_schema

        json_schema_user = json.dumps(json_schema)
        return json_schema_user


if __name__ == '__main__':
    app.run(debug=True)
