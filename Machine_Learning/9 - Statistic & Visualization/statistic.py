# Make statistic
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix

cm = confusion_matrix(y_val, y_pred)
pre = precision_score(y_val, y_pred, average="macro")
rec = recall_score(y_val, y_pred, average="macro")
acc = accuracy_score(y_val, y_pred)
f1 = f1_score(y_val, y_pred, average="macro")

print("confusion matrix: \n",cm)
print("precision_score: \t{0:.5f}".format(pre))
print("recall_score:    \t{0:.5f}".format(rec))
print("accuracy score:  \t{0:.5f}".format(acc))
print("f1_csore:        \t{0:.5f}".format(f1))