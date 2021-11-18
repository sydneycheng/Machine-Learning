import pandas as pd
import csv

# Using methods covered in class:

# 1) load the dataset and use the KNeighborsClassifier to train and test your model

#load dataset
train = pd.read_csv("gameratings.csv")
test = pd.read_csv("test_esrb.csv")
target_names = pd.read_csv("target_names.csv")


x_train = train.loc[:,"console":"violence"]
y_train = train.loc[:,"Target"]

x_test = test.loc[:,"console":"violence"]
y_test = test.loc[:,"Target"]


#use KNeighborsClassifier to train and test model
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X=x_train, y=y_train)

predicted = knn.predict(X=x_test)
expected = y_test

# 2) Display all wrong predicted and expected pairs
knn01 = {}

y = 0

for t in target_names.T:
    target_class = target_names.target_class.values[y]
    target_name = target_names.target_name.values[y]
    y += 1
    knn01[target_class] = target_name

predicted = [knn01[t] for t in predicted]
expected = [knn01[t] for t in expected]

# print(predicted[:20])
# print(expected[:20])

#see which pairs the machine predicted incorrectly
wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]
print(wrong)


# 3) produce a csv file of the name of the game and the predicted rating
outfile = open("my_predictions.csv", 'w')
outfile.write('title, prediction\n')

y = 0
for t in test.T:
    outfile.write(test.values[y][0] + ',' + predicted[y] + '\n')
    y += 1
outfile.close()