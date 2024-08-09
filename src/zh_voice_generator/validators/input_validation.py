import re

def is_chinese(text):
    # Check if the text contains Chinese characters
    zn_unicode_range = r'[\u4e00-\u9fff]'
    match = re.search(zn_unicode_range, text)
    if match:
        print(f"Found Chinese character: {match.group()}")
    else:
        print("No Chinese characters found.")
    return bool(match)

def validate_input(text):
    # Check if the input is empty
    if not text.strip():
        raise ValueError("Input cannot be empty.")

    # Check if the input contains invalid characters (e.g., only emojis or symbols)
    if not is_chinese(text):
        raise ValueError("Input must contain Chinese characters.")

    # Add more validation rules as needed...

# Example usage
try:
    #input_text = "你好，欢迎使用这个程序。"
    #input_text = "Hello, welcome to this program."
    #input_text = "😊👍"
    #input_text = ""
    input_text = "歡迎使用這個程序。"
    print(input_text)
    validate_input(input_text)
    print("Input is valid Chinese text.")
except ValueError as e:
    print(f"Invalid input: {e}")
