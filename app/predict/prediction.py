# Create predict() function that will take your preprocessed data as an input and return a price as output.
from cleaning_data import preprocess


def predict(json_input):
    error = False
    error, message, cleaned_input = preprocess(json_input)
    if error == True:
        json_output = {
            "prediction": None,
            "error": message,
            "other message": None  # mandatory features are ....
        }
        return json_output
    else:
        json_output = {
            "prediction": model(cleaned_input),
            "error": None,
            "other message": message
        }
        return json_output
