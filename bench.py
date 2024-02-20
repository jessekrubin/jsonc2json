from os import path
from pathlib import Path
from time import perf_counter
import re
import json
from jsonc2json import jsonc2json
import commentjson
import orjson

import rapidjson
jsonc_string_1 = """
{ // This is a comment
    "id": 1,
    "guid": "046447ee-da78-478c-b518-b612111942a5",
    "picture": "http://placehold.it/32x32",//Voluptate commodo quis enim cupidatat ea ea nisi.
    "age": 37,
    "name": "Payton Murphy",
    "company": "Robotomic",
    "phone": "806-587-2379",
    "email": "payton@robotomic.com"
}
"""
jsonc_string_2 = """{
    "name": "Vaidik Kapoor",
    "location": "Delhi, India", // Person's location

    // person's appearance
    "appearance": {
        "hair_color": "black",
        "eyes_color": "black",
        "height": "6"
    }
}"""

jsonc_string_3 = """{
    "name": "Vaidik Kapoor", # Person's name
    "location": "Delhi, India", // Person's location

    # Section contains info about
    // person's appearance
    "appearance": {
        "hair_color": "black",
        "eyes_color": "black",
        "height": "6"
    }
}"""

jsonc_strings = [jsonc_string_1, jsonc_string_2]

def rapidjson_strip_and_loads(json_str):
    return rapidjson.loads(json_str, parse_mode=rapidjson.PM_COMMENTS)
# def loads
def strip_and_loads(json_str):
    return commentjson.loads(json_str)
    # # Define the regular expression to match comments
    # pattern = r"(\"(?:\\.|[^\\\"])*\"|\#.*|\/\/.*$)"
    # # Replace any matches with an empty string
    # stripped = re.sub(pattern, "", json_str, flags=re.MULTILINE)
    # # Return the stripped JSON string
    # return stripped

def rs_strip_and_loads(json_str):
    # return json.loads( jsonc2json(json_str))
    return orjson.loads( jsonc2json(json_str.encode()))
def main()->None:
    # jsonc_string = Path('_data').joinpath('sample.json').read_text()

    for jsonc_string in jsonc_strings:
        py_data= strip_and_loads(jsonc_string)
        rs_data= rs_strip_and_loads(jsonc_string)
        rj_data = rapidjson_strip_and_loads(jsonc_string)

        # py_data = json.loads(stripped_json_str)
        # rs_data = json.loads(jsonc2json_str)
        assert json.dumps(py_data) == json.dumps(rs_data)
        assert json.dumps(py_data) == json.dumps(rj_data)

        iterations = 1000

        ti  = perf_counter()
        for i in range(iterations):
            strip_and_loads(jsonc_string)
        tf  = perf_counter()

        print(f"Python: {tf-ti}")

        ti = perf_counter()
        for i in range(iterations):
            rapidjson_strip_and_loads(jsonc_string)
        tf = perf_counter()
        print(f"RapidJSON: {tf-ti}")

        ti = perf_counter()
        for i in range(iterations):
            rs_strip_and_loads(jsonc_string)
        tf = perf_counter()
        print(f"Rust: {tf-ti}")











if __name__ == "__main__":
    main()
