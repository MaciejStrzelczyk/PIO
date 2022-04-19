import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


# if __name__ == '__main__':
df = pd.read_csv('vector.csv', sep=',')
data = df.to_numpy()
x = data[:, 1:].astype('float')
y = data[:, 0]

label_encoder = LabelEncoder()
y_int = label_encoder.fit_transform(y)
y_onehot = OneHotEncoder(sparse=False)
y_int = y_int.reshape(len(y_int), 1)
y_onehot = y_onehot.fit_transform(y_int)
x_train, x_test, y_train, y_test = train_test_split(x, y_onehot, test_size=0.3)

model = Sequential()
model.add(Dense(10, input_dim=6, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.summary()

model.fit(x_train, y_train, epochs=200, batch_size=10, shuffle=True)

y_pred = model.predict(x_test)
y_pred_int = np.argmax(y_pred, axis=1)
y_test_int = np.argmax(y_test, axis=1)
cm = confusion_matrix(y_test_int, y_pred_int)
print(cm)
