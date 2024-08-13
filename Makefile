# Remove all mp3 files in the current directory and its subdirectories
remove_mp3:
	find . -type f -name "*.mp3" -exec rm {} +

# unit tests for validators
validator_unit_tests:
	PYTHONPATH=src/zh_voice_generator pytest tests/validators_tests/test_input_validation.py

# unit tests for utils
utils_unit_tests:
	PYTHONPATH=src/zh_voice_generator pytest tests/utils_tests/test_utils.py

# run all unit tests
all_unit_tests:
	make validator_unit_tests
	make utils_unit_tests
