# Prediction with jsonschema

from preprocess_jsonschema import preprocess # CHANGE AFTER!
import json
import pickle
import numpy as np
from model_jsonschema import gradient_boosting_reg

#model = pickle.load(open('app/model/model.pkl', 'rb'))
model = pickle.load(open('./model.pkl', 'rb'))

json_data = {
    "data": {
        "area": 10,
        "rooms-number": 1,
        "zip-code": 1050,
        "property-type": "HOUSE" # only 4 integers, >1000 & <9999
    }
}

def predict(json_input):
    #error = False
    error, message, cleaned_input = preprocess(json_input)
    if error == True:
        json_output = {
            "prediction": None,
            "error": message,
            "other message": None
        }

        return json.dumps(json_output, indent=4)

    else:
        cleaned_input = np.array(list(cleaned_input['data'].values()))
        json_output = {
            "prediction": model.predict(cleaned_input),
            "error": None,
            "other message": message
        }
        return json.dumps(json_output, indent=4)

if __name__ == "__main__":
    output_prediction = predict(json_data)
    print(output_prediction)