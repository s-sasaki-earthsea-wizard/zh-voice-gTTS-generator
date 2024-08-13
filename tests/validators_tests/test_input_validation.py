import sys
import os
import pytest

# Add the project root directory to the system path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import the function to test
from validators.input_validation import validate_input, is_chinese

def test_validate_input_valid_chinese():
    input_text = "你好，欢迎使用这个程序。"
    assert validate_input(input_text) is None

def test_validate_input_invalid_english():
    input_text = "Hello, welcome to this program."
    with pytest.raises(ValueError, match="Input must contain Chinese characters."):
        validate_input(input_text)

def test_validate_input_emoji():
    input_text = "😊👍"
    with pytest.raises(ValueError, match="Input must contain Chinese characters."):
        validate_input(input_text)

def test_validate_input_empty():
    input_text = ""
    with pytest.raises(ValueError, match="Input cannot be empty."):
        validate_input(input_text)

def test_validate_input_valid_traditional_chinese():
    input_text = "歡迎使用這個程序。"
    assert validate_input(input_text) is None