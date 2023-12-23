import datetime

def generate_timestamp_filename(filename_prefix):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y_%m_%d_%H_%M")
    return f"{filename_prefix}_{timestamp}"
