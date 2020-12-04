# Create predict() function that will take your preprocessed data as an input and return a price as output.
from preprocessing.cleaning_data import preprocess
from model.model import model


def predict(json_input_cleaned):
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
            "prediction": model(json_input_cleaned),
            "error": None,
            "other message": message
        }
        return json_output


if __name__ == '__main__':
    predict(json_input)