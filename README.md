# NAME_OF_THE_API API

The NAME_OF_THE_API API receives data on features of real estate properties in Belgium (input data) and returns a prediction of properties' price (output).

This API has been built by [Orhan Nurkan](https://github.com/orhannurkan), [Naomi Thiru](https://github.com/naomithiru), [Christophe Giets](https://github.com/gietsc) and [Sara Silvente](https://github.com/silventesa).


## How does NAME_OF_THE_API work?

NAME_OF_THE_API has been developed with [Flask](https://flask.palletsprojects.com/en/1.1.x/), one of the most popular Python web application frameworks. 

NAME_OF_THE_API gets data on JSON format. After having assessed the appropriateness of the input ([see "Input requirements" section below](#input-requirements)), data is first [preprocessed](https://github.com/orhannurkan/API-deployment/blob/main/app/preprocessing/cleaning_data.py) according to the model requirements. The prediction is then made based on a [machine learning model](https://github.com/orhannurkan/API-deployment/blob/main/app/model/model.py) that has been [previously trained](https://github.com/orhannurkan/API-deployment/blob/Naomi/app/model/def_dataset.csv) upon/with NUMBER_OF_PROPERTIES properties for sale across Belgium.


## Instructions

*write instructions: Source code = app.py, etc.*

## Input requirements

NAME_OF_THE_API gets data in **[JSON format](https://www.json.org/json-en.html)** and returns a prediction in the same format.

*16 keys you can use to send your data in the appropriate format / mandatory and optional instances / each feature accepts a specific data type (<code>int</code>, <code>bool</code> and <code>str</code> stand for <i>integer</i>, <i>boolean</i> and <i>string</i>, respectively). The features <code>property-type</code> and <code>building-state</code> accept only one of the values that are indicated (in capitals) / etc.*
