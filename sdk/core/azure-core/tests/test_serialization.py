# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import json
import isodate
from datetime import date, timedelta, time
from azure.core.serialization import NULL

def test_NULL_is_falsy():
    assert NULL is not False
    assert bool(NULL) is False
    assert NULL is NULL

def test_serialize_dictionary():
    test_obj = {
        "string": "myid",
        "number": 42,
        "boolean": True,
        "list_of_string": [1, 2, 3],
        "dictionary_of_number": {"pi": 3.14},
        "timedelta": timedelta(1),
        "date": date(2021, 5, 12),
        "datetime": isodate.parse_datetime('2012-02-24T00:53:52.780Z'),
        "time": time(11,12,13),
    }
    expected = {
        "string": "myid",
        "number": 42,
        "boolean": True,
        "list_of_string": [1, 2, 3],
        "dictionary_of_number": {"pi": 3.14},
        "timedelta": "P1D",
        "date": "2021-05-12",
        "datetime": '2012-02-24T00:53:52.780Z',
        'time': '11:12:13',
    }

    assert json.dumps(test_obj, cls=ComplexEncoder) == expected
