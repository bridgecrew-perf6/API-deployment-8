from predict.prediction import predict
from predict.messages import explain_expectations, api_is_alive
from preprocessing.cleaning_data import preprocess
from flask import Flask, request, jsonify, make_response
import pickle
model = pickle.load(open('./model/model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/', methods=['GET'])
def alive():
    return api_is_alive


@app.route('/predict', methods=['GET', 'POST'])
def predictive():  # The parsed JSON data (application/json, see is_json()).
    if request.method == 'POST':
        json_input = request.get_json(force=True)
        if len(json_input["data"].keys()) > 4:
            json_input = request.get_json(force=True)
            error, message, json_input_cleaned = preprocess(json_input)
            if error:
                response = {"error": f"{message}"}
            else:
                response = {"prediction": f"{predict(model,json_input_cleaned)}",
                            "extra info": message}
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify({"message": "Sorry, you should send minimum 4 mandatory features. You can GET more info by GET method to /predict link"}), 406)
    else:
        return explain_expectations


if __name__ == '__main__':
    app.run(debug=True)
