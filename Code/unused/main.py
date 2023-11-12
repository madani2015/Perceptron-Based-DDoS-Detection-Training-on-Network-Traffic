import creation_dataset as cd
import perceptron as prtn
from sklearn.model_selection import train_test_split
import numpy as np

ddos = cd.read_document("ddos_dataset.csv")
normal = cd.read_document("norm_dataset.csv")

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

perceptron =  prtn.Perceptron()
perceptron.perceptron_algorithm(X_train, y_train)

y_pred = perceptron.predict(X_test)
nb_true = 0
for k in range(y_pred.size):
    if y_pred[k] == y_test[k]:
        nb_true += 1
print((nb_true/y_pred.size)*100)


y_valid = perceptron.predict(X_val)
nb_true_val = 0
for k in range(y_valid.size):
    if y_valid[k] == y_val[k]:
        nb_true_val += 1
print((nb_true_val/y_valid.size)*100)
