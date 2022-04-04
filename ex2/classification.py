import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix, plot_confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split


def read_csv_files():
    with open("vector.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        headers = next(reader)
        data = np.array(list(reader))
    Y = data[:, 0]
    X = data[:, 1:]
    return X, Y


if __name__ == '__main__':
    X, Y = read_csv_files()
    clasifier = svm.SVC(gamma='auto')
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=5)
    clasifier.fit(x_train, y_train)
    y_pred = clasifier.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    print(acc)

    cm = confusion_matrix(y_test,y_pred, normalize = 'true')

    print(cm)

    ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=['Desk', 'floor', 'Wall'], cmap=plt.cm.Blues)
    plt.show()

    #disp = plot_confusion_matrix(clasifier, x_test, y_test, display_labels=['Desk', 'floor', 'Wall'], cmap=plt.cm.Blues)
