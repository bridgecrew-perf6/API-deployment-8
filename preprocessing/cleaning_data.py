from predict.prediction import predict
from preprocessing.listsler import subtype, postcodes


def preprocess(json_input):
    types = ["APARTMENT", "HOUSE", "OTHERS"]
    area = 1
    if int(json_input["data"]["area"]) < 0:
        area = 0
    error = True
    message = ""
    if area == 0:
        message = "area size should be an integer and has to be minimum 1(m2)"
    elif json_input["data"]["property-type"] not in types:
        message = "property-type need to be in this list in capital case = " + \
            str(types)
    elif int(json_input["data"]["rooms-number"]) < 1:
        message = "room number has to be at least 1"
    elif json_input["data"]["zip-code"] not in postcodes:
        message = "zip-code need to be between 1000-9999 and in this list = \n" + \
            str(postcodes)
    else:
        error = False

    if error:   # return without any clean because mandotories are wrong
        return error, message, json_input
    else:        # make other cleaning parts
        jid = json_input["data"]
        try:
            if int(jid["land-area"]) < 1:
                jid["land-area"] = 0
        except:
            jid["land-area"] = 0
            pass
        try:
            if int(jid["garden-area"]) < 1:
                jid["garden-area"] = 0
        except:
            jid["garden-area"] = 0
            pass
        try:
            if int(jid["terrace-area"]) < 1:
                jid["terrace-area"] = 0
        except:
            jid["terrace-area"] = 0
            pass
        try:
            if int(jid["facades-number"]) < 1:
                jid["facades-number"] = 0
            elif int(jid["facades-number"]) > 4:
                jid["facades-number"] = 4
        except:
            jid["facades-number"] = 0
            pass

        if jid["full-address"] != "":
            jid["latitude"] = 0  # call API to get GPS location then ???
            jid["longitude"] = 0  # add latitude and latitude to json_input???
        else:
            jid["latitude"] = 0
            jid["longitude"] = 0

        for bool1 in ["garden", "equipped-kitchen", "swimmingpool",
                      "furnished", "open-fire", "terrace"]:
            if bool(jid[bool1]) in [True]:
                jid[bool1] = 1
            else:
                jid[bool1] = 0

        ps = jid["property_subtype"]
        for col1 in subtype:
            if ps == col1:
                jid["col1_"+col1] = 1
            else:
                jid["col1_"+col1] = 0
        jid.pop("property_subtype")

        bs = jid["building-state"]
        for col2 in ['AS_NEW', 'GOOD', 'JUST_RENOVATED', 'TO_RENOVATE', 'TO_RESTORE']:
            if bs == col2:
                jid["col2_"+col2] = 1
            else:
                jid["col2_"+col2] = 0
        jid.pop("building-state")
        jid.pop("facades-number")
        jid.pop("property-type")
        jid.pop("full-address")  # print('input', json_input)
        return error, message, json_input
