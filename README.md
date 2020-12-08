# API-deployment

# 1. The Project

Following a succesful Data Scraping project of Real Estate websites of Belgium, Data Cleaning and Visualization project to clean, study and understand the data, and Machine Learning Project to apply Regression models to predict house prices, the team was challenged to create an API through which data can be received and predicted home prices can be outputted.

The API is to be used by the web developers to create a website around. This repository contains all the information and resources that went into achieving this.

## 1.1. The Team

This project was a collaborative effort between four members of the _Bouwman2_ promotion at [BeCode](https://github.com/becodeorg), Brussels, in December 2020. The team comprised of [Orhan Nurkan](https://github.com/orhannurkan), [Christophe Giets](https://github.com/gietsc), [Sara Silvente](https://github.com/silventesa), and [Naomi Thiru](https://github.com/naomithiru)

# 2. Contents

For quick reference, the repository is divided into the relevant sections, each with it's own resources and outline.  
2.1. [The model](#model)  
2.2. [Preprocessing](#prep)  
2.3. [Fitting the Data](#pred)  
2.4. [The API](#api)  
2.5. [Docker](#doc)

<a name="model"></a>

## 2.1. The model

| **Problem**            | **Data**             | **Methods** | **Libs**                                                        | **Link** |
| ---------------------- | -------------------- | ----------- | --------------------------------------------------------------- | -------- |
| Machine Learning model | House attribute data | Regression  | `pandas`, `numpy`, `sklearn`, `seaborn`, `matplotlib`, `pickle` |          |

The model used was selected out of several models based on it's accuracy score. The `model.py` file contains all the code that was used to train the models. The dataset is available as well in this repository.

The dataset used the sklearn's OneHotEncoder to convert categorial columns to a format which would be useful for a machin learning model.

<a name="prep"></a>

### 2.2. Preprocessing

| **Problem**        | **Data**   | **Methods** | **Libs** | **Link** |
| ------------------ | ---------- | ----------- | -------- | -------- |
| Data preprocessing | json input |             | `python` |          |

The required input from the user is either mandatory or optional. The mandatory fields must have the required inputs in the stipumated formats. All optional features, will have a default null value, which is translated as False or 0 by the prediction model.

The steps of preprocessing the data include:  
-Normalizing the category names to match the feature names of the training dataset to avoid conflicts.  
-Ensuring all features have a value in the correct data types.

<a name="pred"></a>

### 2.3. Fitting the Data

| **Problem** | **Data**      | **Methods** | **Libs**            | **Link** |
| ----------- | ------------- | ----------- | ------------------- | -------- |
| Prediction  | json from API |             | `predict`, `pickle` |          |

The prediction file `prediction.py` takes input data from the user, sends it through the required preprocessing steps and passes this data to the model.
The input data is in json format, and returns a json output, consisting of the house price prediction, and either an error message, or a success message.

<a name="api"></a>

### 2.4. NAME_OF_THE_API API

The NAME_OF_THE_API API receives data on features of real estate properties in Belgium (input data) and returns a prediction of properties' price (output).

This API has been built by [Christophe Giets](https://github.com/gietsc), [Naomi Thiru](https://github.com/naomithiru), [Orhan Nurkan](https://github.com/orhannurkan) and [Sara Silvente](https://github.com/silventesa).

## How does NAME_OF_THE_API work?

NAME_OF_THE_API has been developed with [Flask](https://flask.palletsprojects.com/en/1.1.x/), one of the most popular Python web application frameworks.

NAME_OF_THE_API gets data on JSON format. After having assessed the appropriateness of the input ([see "Input requirements" section below](#input-requirements)), data is first [preprocessed](https://github.com/orhannurkan/API-deployment/blob/main/app/preprocessing/cleaning_data.py) according to the model requirements. The prediction is then made based on a [machine learning model](https://github.com/orhannurkan/API-deployment/blob/main/app/model/model.py) that has been [previously trained](https://github.com/orhannurkan/API-deployment/blob/Naomi/app/model/def_dataset.csv) upon/with NUMBER_OF_PROPERTIES properties for sale across Belgium.

## Instructions

_write instructions: Source code = app.py, etc._

## Input requirements

NAME_OF_THE_API gets data in **[JSON format](https://www.json.org/json-en.html)** and returns a prediction in the same format.

_16 keys you can use to send your data in the appropriate format / mandatory and optional instances / each feature accepts a specific data type (<code>int</code>, <code>bool</code> and <code>str</code> stand for <i>integer</i>, <i>boolean</i> and <i>string</i>, respectively). The features <code>property-type</code> and <code>building-state</code> accept only one of the values that are indicated (in capitals) / etc._
