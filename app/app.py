from flask import Flask, request, jsonify, make_response
import json
import sys
sys.path.insert(1, '/app')
#from preprocessing.cleaning_data import preprocess
#from predict.prediction import predict


app = Flask(__name__)


@app.route('/', methods=['GET'])
def alive():
    return """<h1>Alive!</h1> 
    <a href= '/predict'>Let's use this API!</a>"""


@app.route('/predict', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        if request.is_json:
            #json_input = request.get_json(force=True)
            #json_input_cleaned = preprocess(json_input)
            #prediction, error = predict(json_input_cleaned) # ADD ACCURACY

            if error:
                response = {
                    #"prediction": f"{prediction}"
                    # accuracy_based_on_ADD ACCURACY
                    "error": f"{error}"
                }
            else:
                response = {
                    "prediction": f"{prediction}"
                    # ADD ACCURACY
                    # "error": # ?
                }

            json_output = make_response(jsonify(response), 200) # 200

            return json_output

        else:
            response = make_response(jsonify({"message":"Sorry, no JSON data was received"}), 400)
            return response

    else: # Json schema especially used to validate instances
        json_schema = '''{}'''
        json_schema = json.loads(json_schema)
        return json_schema

if __name__ == '__main__':
    app.run(debug=True)
