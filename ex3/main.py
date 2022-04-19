import csv
import  numpy as np
# from keras import Sequential
# from keras.layers import Danse
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#Todo: używać read_csv
def read_csv_files():
    with open("vector.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader))
    return data[:, 1:], data[:, 0]


if __name__ == '__main__':
    X, Y = read_csv_files()
    label_encoder = LabelEncoder()
    intiger_encoded = label_encoder.fit_transform(Y)

    onehot_encoder = OneHotEncoder(sparse=False)
    intiger_encoded = intiger_encoded.reshape(len(intiger_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(intiger_encoded)

    print(Y)
    #y_int =