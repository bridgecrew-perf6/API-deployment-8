# Definition of Json schema

from zip_codes_belgium import zip_codes

global json_schema
json_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Belgian real estate property",
    "description": "Features of a Belgian real estate property",
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "title": "Input data",
            "type": "object",
            "minProperties": 16,
            "properties": {
                "area": {"title": "Area", "type": "integer", "exclusiveMinimum": 0},
                "property-type": {
                    "title": "Type of property",
                    "type": "string",
                    "enum": ["APARTMENT", "HOUSE", "OTHERS"],
                },
                "rooms-number": {
                    "title": "Number of rooms",
                    "type": "integer",
                    "minimum": 1,
                },
                "zip-code": {
                    "title": "Belgian zip-code",
                    "enum": zip_codes,
                },
                "land-area": {"type": ["integer", "null"], "minimum": 1},
                "garden": {"type": ["boolean", "null"], "default": False},
                "garden-area": {"type": ["integer", "null"], "minimum": 1},
                "equipped-kitchen": {"type": ["boolean", "null"], "default": False},
                "full-address": {"type": ["string", "null"]},
                "swimmingpool": {"type": ["boolean", "null"], "default": False},
                "furnished": {"type": ["boolean", "null"], "default": False},
                "open-fire": {"type": ["boolean", "null"], "default": False},
                "terrace": {"type": ["boolean", "null"], "default": False},
                "terrace-area": {"type": ["integer", "null"], "minimum": 1},
                "facades-number": {"type": ["integer", "null"], "minimum": 1},
                "building-state": {
                    "type": ["string", "null"],
                    "default": "GOOD",
                    "enum": [
                        "NEW",
                        "GOOD",
                        "TO RENOVATE",
                        "JUST RENOVATED",
                        "TO REBUILD",
                        None
                    ],
                },
            },
        }
    },
}

if __name__ == '__main__':
    print(json_schema)