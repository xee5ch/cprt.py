#!/usr/bin/env python3

import cpyrt
import json
from pathlib import Path
import pytest
from unittest.mock import mock_open, patch, MagicMock

good_input = {
    "response": {
        "requestType": 4,
        "elements": {
            "documents": [],
            "relationship_types": [],
            "elements": [],
            "relationships": []
        }
    }
}

good_output = {
    "documents": [],
    "relationship_types": [],
    "elements": [],
    "relationships": []
}

def test_unwrap_invalid_source():
    with pytest.raises(ValueError):
        cpyrt.unwrap(None)
        cpyrt.unwrap(list())
        cpyrt.unwrap(tuple())
        cpyrt.unwrap('')

@patch('builtins.open', mock_open(read_data=json.dumps(good_input)))
def test_unwrap_source_file():
    assert cpyrt.unwrap('./example.json') == good_output

@patch('urllib.request.urlopen')
def test_unwrap_source_url(mock_urlopen):
    read_response = MagicMock()
    read_response.decode = MagicMock(return_value=json.dumps(good_input))
    sample_response = MagicMock()
    sample_response.read = MagicMock(return_value=read_response)
    mock_urlopen.return_value = sample_response
    cpyrt.unwrap('https://example.com/cprt_document.json') == good_output

def test_unwrap_source_obj():
    assert cpyrt.unwrap(good_input) == good_output
