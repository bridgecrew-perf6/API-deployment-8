# Preprocessing with json schema

# Import libraries for JSON input management and validation
import json
from jsonschema.validators import Draft7Validator

# Import modules
from json_schema_file import json_schema



#from sklearn.preprocessing import OneHotEncoder
#from sklearn.compose import make_column_transformer

# Json Example 1
#json_input_file = open("json_data.json")  # open json file
#json_input_1 = json.load(json_input_file)  # convert to python dict

# Json Example
json_input_2 = {
    "data": {
        "area": 5,
        "property-type": "APARTMENT",
        "rooms-number": 1,
        "zip-code": 1050,  # only 4 integers, >1000 & <9999
        "land-area": None,  # Optional
        "garden": True,  # Optional
        "garden-area": 34,  # Optional
        "equipped-kitchen": False,  # Optional
        "full-address": "djfg",  # Optional
        "swimmingpool": True,  # Optional
        "furnished": False,  # Optional
        "open-fire": True,  # Optional
        "terrace": False,  # Optional
        "terrace-area": 98,  # Optional
        "facades-number": 4,  # >1 & <10 #Optional
        #  ["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        "building-state": "NEW",
    }
}

def preprocess(json_input):

    """Check whether there are errors related to JSON input format"""

    # 1. Set validator variable to validate the input according to the draft version 7 JSON schema
    validator = Draft7Validator(schema=json_schema)

    # 2. Show input errors in a readable, user-friendly way
    readable_input_errors = []
    for error in validator.iter_errors(instance=json_input):
        if len(error.path) == 0:
                readable_input_errors.append(f"In 'properties': {error.message}")
        else:
                readable_input_errors.append(f"In '{str(error.path[-1])}': {error.message}")

    error_input = '\n'.join(readable_input_errors)


    # 3. Input validation. If no errors are found, preprocess the input data.

    if readable_input_errors:
        error = True
        message = f"\n ERROR: The inputed data is not valid due to the errors below. Please fix them and send your data again.\n{error_input}\n"

    else:
        error = False
        message = "SUCCESS: Your data is valid."

    """Once data is valid, start preprocessing"""
    # 1. Handle with null (None) values: replace by default ones

    all_variables = json_input["data"].keys()

    boolean_variables = ["garden", 'equipped-kitchen', 'swimmingpool', 'furnished', 'open-fire', 'terrace']
    integer_variables = ["terrace-area", "garden-area", "facades-number", "land-area"]

    for variable in all_variables:
        if variable in boolean_variables:
            if json_input["data"][variable] == None:
                json_input["data"][variable] = False
        elif variable in integer_variables:
            if json_input["data"][variable] == None:
                json_input["data"][variable] = 0
        elif variable == "facades-number":
            if json_input["data"][variable] > 4:
                json_input["data"][variable] = 4
        elif variable == "building-state":
            if json_input["data"][variable] == None:
                json_input["data"][variable] = "GOOD"
        ############# WHAT DO WE DO WITH FULL ADDRESS? ###########################

    ########## PREFIX FOR PROPERTY-SUBTYPES AND BUILDING STATES

    ########## TRANSFORM DUMMIES

        #column_trans = make_column_transformer(
        #    (OneHotEncoder(), ['property_subtype', 'swimming_pool_has', 'open_fire', 'building_state_agg']),
        #    remainder='passthrough')"""

    #########################

        return error, message, json_input


if __name__ == "__main__":
    error, message, json_input = preprocess(json_input_2)
    print(f"error: {error}, message: {message}\n Your data: \n {json_input_2}")



    # types = ["APARTMENT", "HOUSE", "OTHERS"]
    # state = ["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]
    # message = ""


#   if error == False: ###########################
# make other cleaning parts


######################################################################################### BOOLEAN (6)
# if bool(json_input["data"]["garden"]) not in [True]:
#    json_input["data"]["garden"] = False  # default value; hence, "default":False
# else:
#    json_input["data"]["garden"] = True

# if bool(json_input["data"]["equipped-kitchen"]) not in [True]:
#    json_input["data"]["equipped-kitchen"] = False
# else:
#    json_input["data"]["equipped-kitchen"] = True

# if bool(json_input["data"]["swimmingpool"]) not in [True]:
#    json_input["data"]["swimmingpool"] = False
# else:
#    json_input["data"]["swimmingpool"] = True

# if bool(json_input["data"]["furnished"]) not in [True]:
#    json_input["data"]["furnished"] = False
# else:
#    json_input["data"]["furnished"] = True

# if bool(json_input["data"]["open-fire"]) not in [True]:
#    json_input["data"]["open-fire"] = False
# else:
#    json_input["data"]["open-fire"] = True

# if bool(json_input["data"]["terrace"]) not in [True]:
#    json_input["data"]["terrace"] = False
# else:
#    json_input["data"]["terrace"] = True

############################################################################### INTEGERS
# Minimum 1

# if int(json_input["data"]["land-area"]) < 1:  # = "minimum": 1
#    json_input["data"]["land-area"] = 0

# if int(json_input["data"]["garden-area"]) < 1:
#    json_input["data"]["garden-area"] = 0 # "minimum":0

# if int(json_input["data"]["terrace-area"]) < 1:
#   json_input["data"]["terrace-area"] = 0

#        if int(json_input["data"]["facades-number"]) < 1: ################################333
#            json_input["data"]["facades-number"] = 0 ########################################

#        if int(json_input["data"]["facades-number"]) > 4: ####################################
#            json_input["data"]["facades-number"] = 4 ########################################3

################################################################################# STRINGS

#        if json_input["data"]["full-address"] != "": #############################33
# call API to get GPS location then ???????????????????
# add latitude and latitude to json_input??????????????
#            json_input["data"]["latitude"] = 0 #############################################
#            json_input["data"]["longitude"] = 0 ###########################################


# if json_input["data"]["building-state"] not in state:
# Selected according to the median value of "Building state"
#    json_input["data"]["building-state"] = "GOOD" # "default":"GOOD"
# return error, message, json_input

# error, message = preprocess(sample_json_input)