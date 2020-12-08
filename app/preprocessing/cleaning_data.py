# Preprocessing with json schema

# Import libraries for JSON input management and validation
import json
from jsonschema.validators import Draft7Validator

# Import modules
from json_schema_file import json_schema
from listler import subtype, postcodes

# Json Example 1
# json_input_file = open("json_data.json")  # open json file
# json_input_1 = json.load(json_input_file)  # convert to python dict

# Json Example
json_input_2 = {
    "data": {
        "area": 5,
        "property-type": "APARTMENT",
        "rooms-number": 2,
        "zip-code": 1050,  # only 4 integers, >1000 & <9999
        "land-area": None,  # Optional
        "garden": True,  # Optional
        "garden-area": 34,  # Optional
        "equipped-kitchen": False,  # Optional
        "full-address": "djfg",  # Optional
        "swimmingpool": True,  # Optional
        "furnished": False,  # Optional
        "open-fire": 9,  # Optional
        "terrace": False,  # Optional
        "terrace-area": 98,  # Optional
        "facades-number": 16,  # >1 & <10 #Optional
        #  ["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        "building-state": "NEW"
    }
}

def preprocess(json_input):

    """Check whether there are errors related to JSON input format"""

    # 1. Set validator variable to validate the input according to the draft version 7 JSON schema
    validator = Draft7Validator(schema=json_schema)

    # 2. Show input errors in a readable, user-friendly way
    readable_input_errors = []
    global error
    for error in validator.iter_errors(instance=json_input):
        if len(error.path) == 0:
            readable_input_errors.append(f"In 'properties': {error.message}")
        else:
            readable_input_errors.append(f"In '{str(error.path[-1])}': {error.message}")

    error_input = "\n".join(readable_input_errors)

    # 3. Input validation. If no errors are found, preprocess the input data.
    global message
    message = ""

    if readable_input_errors:
        error = True
        message = error_input

    else:
        error = False
        message = "SUCCESS: Your data is valid."

        """Once data is valid, start preprocessing"""
        # 1. Handle with null (None) values: replace by default ones

        jid = json_input["data"]

        all_variables = jid.keys()

        boolean_variables = [
            "garden",
            "equipped-kitchen",
            "swimmingpool",
            "furnished",
            "open-fire",
            "terrace",
        ]
        integer_variables = [
            "terrace-area",
            "garden-area",
            "facades-number",
            "land-area",
        ]

        for variable in all_variables:
            if variable in boolean_variables:
                if jid[variable] == None or False:
                    jid[variable] = 0
                else:
                    jid[variable] = 1
            elif variable in integer_variables:
                if jid[variable] == None or 0:
                    jid[variable] = 0
            elif variable == "facades-number":
                if jid[variable] > 4:
                    jid[variable] = 4

        # Property-type
        jid_pt = jid["property-type"]
        for col1 in subtype:
            if jid_pt == col1:
                jid["col1_" + col1] = 1
            else:
                jid["col1" + col1] = 0

        # Building-state
        jid_bs = jid["building-state"]

        for col2 in ["AS_NEW", "GOOD", "JUST_RENOVATED", "TO_RENOVATE", "TO_RESTORE"]:
            if jid_bs == col2:
                jid["col_2" + col2] = 1
            else:
                jid["col_2" + col2] = 0

        # Full-address
        if jid["full-address"] != "" or None:
            jid["latitude"] = 0  # call API to get GPS location then ???
            jid["longitude"] = 0  # add latitude and latitude to json_input???
        else:
            jid["latitude"] = 0
            jid["longitude"] = 0

        jid.pop("building-state")
        jid.pop("facades-number")
        jid.pop("property-type")
        jid.pop("full-address")

        ########## TRANSFORM DUMMIES

        # column_trans = make_column_transformer(
        #    (OneHotEncoder(), ['property_subtype', 'swimming_pool_has', 'open_fire', 'building_state_agg']),
        #    remainder='passthrough')"""

        #########################

    return error, message, json_input


if __name__ == "__main__":
    error, message, json_input_cleaned = preprocess(json_input_2)
    print({"error": error, "message": message})
