import os
import json
import pickle
import cv2
import pandas as pd

def persist_data(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)

def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' does not exist.")

def overwrite_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

def append_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data)

def write_binary_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

def read_image_file(filename):
    image = cv2.imread(filename)
    if image is not None:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Failed to read the image from '{filename}'.")

def read_csv_file(filename):
    df = pd.read_csv(filename)
    print(df)

def write_csv_file(filename, df):
    df.to_csv(filename, index=False)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    print(data)

def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

def write_pickle_file(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

