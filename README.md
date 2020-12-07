# API-deployment
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
2.3. [Predict](#pred)  
2.4. [The API](#api)  
2.5. [Docker](#doc)  

<a name="model"></a>
## 2.1. The model
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Machine Learning model|House attribute data|Regression|`pandas`, `numpy`, `sklearn`, `seaborn`, `matplotlib`, `pickle`| |

The model used was selected out of several models based on it's accuracy score. The `model.py` file contains all the code that was used to train the models. The dataset is available as well in this repository.

The dataset used the sklearn's OneHotEncoder to convert categorial columns to a format which would be useful for a machin learning model.

The selected prediction model is the `GradientBoosting` ensemble regression model built using sklearn packages.
Using pickle, the model is packaged to be able to be used externally.

<a name="prep"></a>
### Preprocessing
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|Data preprocessing |json input| |`pandas`, `numpy`,| |

The required input from the user is either mandatory or optional. The mandatory fields must have the required inputs in the stipumated formats. All optional features, will have a default null value, which is translated as False or 0 by the prediction model.

The steps of preprocessing the data include:
Normalizing the category names to match the feature names of the training dataset.
Ensuring all features have a value in the correct data types.
The required input from the user is either mandatory or optional. The mandatory fields must have the required inputs in the stipumated formats.

<a name="pred"></a>
### Fitting the Data
|__Problem__|__Data__|__Methods__|__Libs__|__Link__|
|-|-|-|-|-|
|`Prediction`|json from API|`predict`|`pickle`||

The prediction file takes input data from the user, sends it through the required preprocessing steps and passes this data to the model.
The input data is in json format, and returns a json output, consisting of the house price prediction, and either an error message, or a success message.

