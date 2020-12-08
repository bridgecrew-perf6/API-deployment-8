# Prediction with jsonschema

from preprocessing import preprocess # CHANGE AFTER!
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

# ---- ORHAN

import numpy as np

f = ['zip-code', 'area', 'rooms-number', 'equipped-kitchen', 'garden', 'garden-area', 'terrace', 'terrace-area', 'furnished',
     'swimmingpool', 'land-area', 'open-fire', 'longitude', 'latitude', 'col1_APARTMENT', 'col1_APARTMENT_BLOCK',
     'col1_BUNGALOW', 'col1_COUNTRY_COTTAGE', 'col1_DUPLEX', 'col1_EXCEPTIONAL_PROPERTY', 'col1_FARMHOUSE', 'col1_FLAT_STUDIO',
     'col1_GROUND_FLOOR', 'col1_HOUSE', 'col1_KOT', 'col1_LOFT', 'col1_MANOR_HOUSE', 'col1_MANSION', 'col1_MIXED_USE_BUILDING',
     'col1_OTHER_PROPERTY', 'col1_PENTHOUSE', 'col1_SERVICE_FLAT', 'col1_TOWN_HOUSE', 'col1_TRIPLEX', 'col1_VILLA', 'col2_AS_NEW',
     'col2_GOOD', 'col2_JUST_RENOVATED', 'col2_TO_RENOVATE',
     'col2_TO_RESTORE']


def predict(model, json_input):    # print(json_input)
    cleaned_input = []
    print("---------1 - cleaned_input--------", json_input, len(json_input["data"].keys()))

    for i in f:
        cleaned_input.append(json_input["data"][i])
    print("---------2 - cleaned_input--------", cleaned_input, len(cleaned_input))

    cleaned_input = np.array(cleaned_input).reshape(-1, 1)
    print("---------3 - cleaned_input--------",cleaned_input, len(cleaned_input))

    c = []
    for k in json_input["data"].keys():
        if k != 0:
            print(k, len(json_input["data"].keys()))
            c.append(json_input["data"][k])

    cleaned_input = np.array([1000, 100, 3, 1, 1, 5, 1, 5, 1, 0, 0, 0, 0, 0, 1, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]).reshape(1, -1)

    return json.dumps({"prediction": model.predict(cleaned_input)}, indent=4)

if __name__ == "__main__":
    output_prediction = predict(model,json_data)
    print(output_prediction)