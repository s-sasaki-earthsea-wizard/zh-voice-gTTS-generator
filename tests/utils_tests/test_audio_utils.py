import os
import pytest
from src.zh_voice_generator.utils.audio_utils import prepare_output_path

def test_prepare_output_path_default():
    output_path = prepare_output_path()
    assert output_path.startswith('output/output_')
    assert output_path.endswith('.mp3')
    assert os.path.dirname(output_path) == 'output'

def test_prepare_output_path_custom_filename():
    output_path = prepare_output_path(filename='custom_name.mp3')
    assert output_path == 'output/custom_name.mp3'

def test_prepare_output_path_custom_output_dir():
    output_path = prepare_output_path(output_dir='custom_output_dir')
    assert output_path.startswith('custom_output_dir/output_')
    assert output_path.endswith('.mp3')
    assert os.path.dirname(output_path) == 'custom_output_dir'

def test_prepare_output_path_custom_dir_and_filename():
    output_path = prepare_output_path(output_dir='custom_output_dir', filename='custom_name.mp3')
    assert output_path == 'custom_output_dir/custom_name.mp3'
