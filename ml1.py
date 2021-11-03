from sklearn.datasets import load_digits

#digits is our dataset; digits = bunch object
digits = load_digits()

# #gives us info about our data set
# print(digits.DESCR)

# #look at one of the rows of our dataset; the 5th sample
# #this is a 1D array w/ 64 columns
# print(digits.data[5])
# #tells us what each of the samples represents (gives us a # btwn 0-9)
# print(digits.target[5])


# #returns (1797,64); rows - the number of samples; columns - the number of features
# print(digits.data.shape)
# #returns only (1797, ) rows; they represent the goal for each of those samples
# print(digits.target.shape)

import matplotlib.pyplot as plt

#we are creating a chart with 24 pictures; we want the target value of each of these images
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))

# plt.show()

#ravel makes 2D into 1D
for item in zip(axes.ravel(), digits.images, digits.target):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)

plt.tight_layout()
# plt.show()


from sklearn.model_selection import train_test_split

#will randomly split data; train 75% and test 25%
data_train, data_test, target_train, target_test = train_test_split(
    digits.data, digits.target, random_state = 11)

print(data_train.shape) #will be 2D
print(data_test.shape)
print(target_train.shape)   #will be 1D
print(target_test.shape)


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

#fit is the method that does all the machine learning****
#needs 2 things: the data and the target (to know what data represents)
    #here, we do need the target so the machine can Learn
knn.fit(X=data_train, y=target_train)

#this is where we give unlabeled data and see if it can correctly guess the #
    #we don't need the target here bcs it will output the correct answer

predicted = knn.predict(X=data_test)
    #target_test will be the correct answer; we'll see if the machine outputs this
expected = target_test
print(predicted[:20])
print(expected[:20])

#score to see how well the machine predicted
print(format(knn.score(data_test, target_test), ".2%"))

#see which ones the machine got wrong
wrong = [(p,e) for (p,e) in zip(predicted, expected) if p != e]
print(wrong)


#confusion matrix
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)

print(confusion)


#create a heatmap to visualize where machine went wrong
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df = pd.DataFrame(confusion, index=range(10), columns=range(10))

figure = plt2.figure(figsize=(7,6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.show()
