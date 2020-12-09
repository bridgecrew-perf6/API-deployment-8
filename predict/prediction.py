import pandas as pd

f = ['zip-code', 'area', 'rooms-number', 'equipped-kitchen', 'garden', 'garden-area', 'terrace', 'terrace-area', 'furnished',
     'swimmingpool', 'land-area', 'open-fire', 'longitude', 'latitude', 'col1_APARTMENT', 'col1_APARTMENT_BLOCK',
     'col1_BUNGALOW', 'col1_COUNTRY_COTTAGE', 'col1_DUPLEX', 'col1_EXCEPTIONAL_PROPERTY', 'col1_FARMHOUSE', 'col1_FLAT_STUDIO',
     'col1_GROUND_FLOOR', 'col1_HOUSE', 'col1_KOT', 'col1_LOFT', 'col1_MANOR_HOUSE', 'col1_MANSION', 'col1_MIXED_USE_BUILDING',
     'col1_OTHER_PROPERTY', 'col1_PENTHOUSE', 'col1_SERVICE_FLAT', 'col1_TOWN_HOUSE', 'col1_TRIPLEX', 'col1_VILLA', 'col2_AS_NEW',
     'col2_GOOD', 'col2_JUST_RENOVATED', 'col2_TO_RENOVATE',
     'col2_TO_RESTORE']
f2 = ['postcode', 'area', 'rooms_number', 'equipped_kitchen_has', 'garden',
      'garden_area', 'terrace', 'terrace_area', 'furnished',
      'swimming_pool_has', 'land_surface', 'open_fire', 'longitude',
      'latitude', 'col1_APARTMENT', 'col1_APARTMENT_BLOCK', 'col1_BUNGALOW',
      'col1_COUNTRY_COTTAGE', 'col1_DUPLEX', 'col1_EXCEPTIONAL_PROPERTY',
      'col1_FARMHOUSE', 'col1_FLAT_STUDIO', 'col1_GROUND_FLOOR', 'col1_HOUSE',
      'col1_KOT', 'col1_LOFT', 'col1_MANOR_HOUSE', 'col1_MANSION',
      'col1_MIXED_USE_BUILDING', 'col1_OTHER_PROPERTY', 'col1_PENTHOUSE',
      'col1_SERVICE_FLAT', 'col1_TOWN_HOUSE', 'col1_TRIPLEX', 'col1_VILLA',
      'col2_AS_NEW', 'col2_GOOD', 'col2_JUST_RENOVATED', 'col2_TO_RENOVATE',
      'col2_TO_RESTORE']
#'rooms-number', 'zip-code','land-area','garden-area','terrace-area','equipped-kitchen','open-fire',
# 'rooms_number','postcode', 'land_surface','garden_area','terrace_area','equipped_kitchen_has', 'open_fire',
fkendi = ['postcode', 'area', 'rooms_number', 'equipped_kitchen_has', 'garden',
          'garden_area', 'terrace', 'terrace_area', 'furnished',
          'swimming_pool_has', 'land_surface', 'open_fire', 'longitude',
          'latitude', 'col1_APARTMENT', 'col1_APARTMENT_BLOCK', 'col1_BUNGALOW',
          'col1_COUNTRY_COTTAGE', 'col1_DUPLEX', 'col1_EXCEPTIONAL_PROPERTY',
          'col1_FARMHOUSE', 'col1_FLAT_STUDIO', 'col1_GROUND_FLOOR', 'col1_HOUSE',
          'col1_KOT', 'col1_LOFT', 'col1_MANOR_HOUSE', 'col1_MANSION',
          'col1_MIXED_USE_BUILDING', 'col1_OTHER_PROPERTY', 'col1_PENTHOUSE',
          'col1_SERVICE_FLAT', 'col1_TOWN_HOUSE', 'col1_TRIPLEX', 'col1_VILLA',
          'col2_AS_NEW', 'col2_GOOD', 'col2_JUST_RENOVATED', 'col2_TO_RENOVATE',
          'col2_TO_RESTORE']


def predict(model, json_input):    # print(json_input)
    #     cleaned_input = []
    # json that filled by default 0, =>np.array DataFrame
    # print("---------1 - cleaned_input--------",
    #   json_input, len(json_input["data"].keys()))
    #     for i in f:
    #         cleaned_input.append(json_input["data"][i])
    # print("---------2 - cleaned_input--------",
    #       cleaned_input, len(cleaned_input))
    # print("demo++++++++++", json_input["data"])
    demo1 = pd.json_normalize(json_input["data"])
    # print("##############################################", demo1.columns)
    demo = {}  # this line gets only feautures we need from input json
    for column in f:
        demo[column] = demo1[column]
    demo = pd.json_normalize(demo)
    demo['rooms_number'] = demo['rooms-number']
    demo['postcode'] = demo['zip-code']
    demo['land_surface'] = demo['land-area']
    demo['garden_area'] = demo['garden-area']
    demo['terrace_area'] = demo['terrace-area']
    demo['equipped_kitchen_has'] = demo['equipped-kitchen']
    demo['open_fire'] = demo['open-fire']
    demo['swimming_pool_has'] = demo['swimmingpool']

    demo = demo.drop(['rooms-number', 'zip-code', 'land-area', 'garden-area',
                      'terrace-area', 'equipped-kitchen', 'open-fire', 'swimmingpool'], axis=1)
    #'rooms-number', 'zip-code','land-area','garden-area','terrace-area','equipped-kitchen','open-fire','swimmingpool',
    # 'rooms_number','postcode', 'land_surface','garden_area','terrace_area','equipped_kitchen_has', 'open_fire','swimming_pool_has',
    # print("-------------once------------------", demo.columns)
    demo = demo[f2]
#     demo = pd.DataFrame(json_input["data"])
    # print("-------------sonra++++++++++", demo.columns)

#     cleaned_input = np.array(cleaned_input).reshape(-1, 1)
    # print("---------3 - cleaned_input--------",
    #       cleaned_input, len(cleaned_input))
#     c = []
#     for k in json_input["data"].keys():
#         if k != 0:
#         print(k, len(json_input["data"].keys()))
#         c.append(json_input["data"][k])
    cleaned_input = demo
    a = {"prediction": model.predict(cleaned_input)}
    # print(a)
#     np.array([1000, 100, 3, 1, 1, 5, 1, 5, 1, 0, 0, 0, 0, 0, 1, 0, 0,
#                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]).reshape(1, -1)

    return a
