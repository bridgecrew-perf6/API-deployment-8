import pandas as pd
# import json_data_example
import json

json_input = {
    "data": {
        "area": 5,
        "property-type": "APARTMENT",
        "rooms-number": 1,
        "zip-code": 1050,  # only 4 integers, >1000 & <9999
        "land-area": None,  # Optional
        "garden": None,  # Optional
        "garden-area": None,  # Optional
        "equipped-kitchen": None,  # Optional
        "full-address": "djfg",  # Optional
        "swimmingpool": None,  # Optional
        "furnished": None,  # Optional
        "open-fire": None,  # Optional
        "terrace": None,  # Optional
        "terrace-area": None,  # Optional
        "facades-number": None,  # >1 & <10 #Optional
        #  ["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
        "building-state": None,
    }
}
# Load JSON
# = json.load(open('json_data_example.json', 'r'))
# df = pd.json_normalize(json_data_2)
# print(df)
# df.replace("null", np.nan, inplace=True)
# df = df.dropna(axis=1)

print(type(json_input["data"]["garden"]))

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

print(json_input)