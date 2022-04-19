import csv

import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split


def read_csv_files():
    with open("vector.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader))
    return data[:, 1:], data[:, 0]


if __name__ == '__main__':
    X, Y = read_csv_files()
    classifier = svm.SVC(gamma='auto')
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=2)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred, normalize='true')
    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=['Desk', 'floor', 'Wall'], cmap=plt.cm.Blues)
    plt.show()
    print("Accuracy:\n")
    print(acc)
