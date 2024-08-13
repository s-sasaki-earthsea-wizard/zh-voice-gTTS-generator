import os
import datetime

def prepare_output_path(output_dir='output', filename=None):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # If no filename is provided, generate one
    if filename is None:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"output_{timestamp}.mp3"
    
    return os.path.join(output_dir, filename)

