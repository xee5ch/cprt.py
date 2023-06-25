#!/usr/bin/env python

import pytest
import pydantic
from cpyrt import CPRT

def test_model_invalid_empty():
    with pytest.raises(TypeError):
        bad_input = {}
        CPRT(bad_input)

def test_model_invalid_malformed():
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        bad_input = {
            'a': [1, 2, 3],
            'b': 'value',
            'c': False
        }
        CPRT(**bad_input)

def test_model_valid():
    good_input = {
            "documents": [],
            "relationship_types": [],
            "elements": [],
            "relationships": []
        }
    CPRT(**good_input)
