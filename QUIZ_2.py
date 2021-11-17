import pandas as pd

# Using methods covered in class:

# 1) load the dataset and use the KNeighborsClassifier to train and test your model

#load dataset
train = pd.read_csv("gameratings.csv")
test = pd.read_csv("test_esrb.csv")

data_train, data_test, target_train, target_test = train, test, train.Target, test.Target

print(data_train.shape)
print(target_train.shape)
print(data_test.shape)
print(target_test.shape)

#use KNeighborsClassifier to train and test model
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X=data_train, y=target_train)

predicted = knn.predict(X=data_test)
expected = target_test
print(predicted[:20])
print(expected[:20])


# 2) Display all wrong predicted and expected pairs

#see which ones the machine got wrong
wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]
print(wrong)


# 3) produce a csv file of the name of the game and the predicted rating
mypredictions = pd.write_csv("my_predictons.csv")