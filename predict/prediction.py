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
    print("---------1 - cleaned_input--------",
          json_input, len(json_input["data"].keys()))
    # for i in f:
    #     cleaned_input.append(json_input["data"][i])
    # print("---------2 - cleaned_input--------",
    #       cleaned_input, len(cleaned_input))
    # cleaned_input = np.array(cleaned_input).reshape(-1, 1)
    # print("---------3 - cleaned_input--------",
    #       cleaned_input, len(cleaned_input))
    # c = []
    # for k in json_input["data"].keys():
    #     if k != 0:
    #         print(k, len(json_input["data"].keys()))
    #         c.append(json_input["data"][k])
    cleaned_input = np.array([1000, 100, 3, 1, 1, 5, 1, 5, 1, 0, 0, 0, 0, 0, 1, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]).reshape(1, -1)
    return {"prediction": model.predict(cleaned_input)}
