# API-deployment

# 1. The Project
Following a succesful Data Scraping project of Real Estate websites of Belgium, Data Cleaning and Visualization project to clean, study and understand the data, and Machine Learning Project to apply Regression models to predict house prices, the team was challenged to create an API through which data can be received and predicted home prices can be outputted.

The API is to be used by the web developers to create a website around. This repository contains all the information and resources that went into achieving this.


## 1.1. The Team
This project was a collaborative effort between four members of the *Bouwman2* promotion at [BeCode](https://github.com/becodeorg), Brussels, in December 2020. The team comprised of [Orhan Nurkan](https://github.com/orhannurkan), [Christophe Giets](https://github.com/gietsc), [Sara Silvente](https://github.com/silventesa), and [Naomi Thiru](https://github.com/naomithiru)

# 2. Contents
For quick reference, the repository is divided into the relevant sections, each with it's own resources and outline.  
2.1. [The model](#model)  
2.2. [Preprocessing](#prep)  
2.3. [Fitting the Data](#pred)  
2.4. [The API](#api)  
2.5. [Docker](#doc)  

<a name="model"></a>
## 2.1. The model
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Machine Learning model|Belgium Real Estate Dataset |Regression|`pandas`, `numpy`, `sklearn`, `pickle`|https://github.com/orhannurkan/API-deployment/blob/main/app/model/model.py|

The features used in this prediction model are: `'house_is','property_subtype', 'price', 'postcode', 'area','rooms_number', 'equipped_kitchen_has', 'garden', 'garden_area','terrace', 'terrace_area', 'furnished', 'swimming_pool_has','land_surface', 'building_state_agg', 'open_fire', 'longitude','latitude'`

Dummy values: All categorical variables and boolean values are given dummy(numerical) values, to convert them into correct formats for the machine learning model using pandas `pd.get dummies`. This results in 40 variables passed to a model, which defines the number of variables expected from the preprocessing stage.

The `model.py` file contains all the code that was used to train the models. The dataset is available as well in [assets](https://github.com/orhannurkan/API-deployment/tree/main/assets)

The model is then [pickled](https://docs.python.org/3/library/pickle.html) to be used for prediction using the function `pickle.dump()`


<a name="prep"></a>
## 2.2. Preprocessing
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Data preprocessing |[JSON input](#input)| |`python`, `JSON Schema Validator`|https://github.com/orhannurkan/API-deployment/tree/main/preprocessing |

The input data is preprocessed according to the model requirements(formats, number of variables).

Below are the 16 keys use to define [JSON input](#input), and the appropriate formats: </br>
`**mandatory data:** {"area":[int],"property-type": ["APARTMENT" | "HOUSE" | "OTHERS"],"rooms-number":[int],"zip-code":[int]}`

`**optional data:** {"land-area":[int],"garden":[bool],"garden-area": *Optional* [int],"equipped-kitchen": [bool],"full-address": [str],"swimmingpool": [bool],"furnished":[bool],"open-fire":[bool],"terrace":[bool],"terrace-area":[int],"facades-number": [int],"building-state":["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"] }`


- The input fields are either mandatory or if not, described as *Optional*. Each feature accepts a specific data type `int, bool and str` (for integer, boolean and string respectively).  
- The features property-type and building-state accept one value out of a list of options, in uppercase.  

The preprocessing function employs the use of [JSON Schema Validator](https://github.com/Julian/jsonschema) to define the variables and expected values.


**Important points to note:**  
* All optional features, will have a default null value, which is coverted to False or 0, for the prediction model.  
* The category names are converted to match the feature names of the training dataset to avoid conflicts.  
* Location data; Using Google APIs, the feature `full-address` is parsed and `longitude` & `latitude` fatures extracted, which are very important for better prediction accuracy.  
* Dummy values are created using `pd.get_dummies`, to convert catgorical and boolean values, and create 40 features as expcted by the prediction model.

The preprocessing step returns a `json_input_cleaned` output.

<a name="pred"></a>
## 2.3. Fitting the Data
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Prediction|json from API||`predict`, `pickle`| (https://github.com/orhannurkan/API-deployment/tree/main/predict)|

The prediction file `prediction.py` takes a cleaned json input and returns a [JSON output](#output), consisting of the house price prediction, and either an error message, or a success message.


<a name="api"></a>
## 2.4. The API
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Deployment|[JSON output](#output)||`Flask`, `pickle`, |(https://github.com/orhannurkan/API-deployment/blob/main/app.py)|

The API has been developed with [Flask](https://flask.palletsprojects.com/en/1.1.x/), one of the most popular Python web application frameworks. The API gets [JSON input](#input), which is [preprocessed](#prep) according to the model requirements. The prediction is then made based on a [machine learning model](#model) and returns a prediction of properties' price (output).

The 16 keys to be used to send user data in the appropriate format are outlined [here](#input).  
To get the prediction, one must at minimum enter a value for the features `area`, `property-type`, `rooms-number` and `zip-code` (they are mandatory features).
The remaining features are optional and will use default values if none are provided.

### Instructions



<a name="doc"></a>
## 2.5. Docker
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Share environment|`Dockerfile`, `requirements.txt`||`python`,`pip`|| |

The `Dockerfile` allows you to start an environment from the latest version of Ubuntu. Once your environment is running on the latest Ubuntu version, it installs the latest version of Python (`python3.8`) and `pip`. Then using `pip`, it will install all the necessary packages located in the `requirements.txt` file.

Using `gunicorn`
