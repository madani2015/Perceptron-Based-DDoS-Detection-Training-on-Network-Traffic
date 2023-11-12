import creation_dataset as cd
import knn
from sklearn.model_selection import train_test_split
import numpy as np


# creation of the dataset
ddos = cd.read_document("dataset/ddos_dataset.csv") + cd.read_document("dataset/ddos_att_dataset.csv") + cd.read_document("dataset/ddos_full_dataset.csv")
normal = cd.read_document("dataset/norm_dataset.csv") + cd.read_document("dataset/normal_full_dataset.csv")

y= []
for k in range(len(ddos)):
    if k < 10:
        y.append(-1)
    else:
        y.append(1)

for k in range(len(normal)):
    y.append(-1)

dataset = ddos+normal
X = np.array(dataset)
y = np.array(y)

X_train, X_res, y_train, y_res = train_test_split(X, y, train_size= 0.7)
X_test, X_val, y_test, y_val =  train_test_split(X_res, y_res, train_size= 0.5)

model =  knn.KNN(3)
model.train(X_train, y_train)

y_pred = model.predict(X_test, 2)
nb_true = 0
for k in range(y_pred.size):
    if y_pred[k] == y_test[k]:
        nb_true += 1
print((nb_true/y_pred.size)*100)


y_valid = model.predict(X_val, 2)
nb_true_val = 0
for k in range(y_valid.size):
    if y_valid[k] == y_val[k]:
        nb_true_val += 1
print((nb_true_val/y_valid.size)*100)

liste = [[7, 9000000]]
array = np.array(liste)
print(model.predict(array, 2))

