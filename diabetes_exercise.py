''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets


diabetes = datasets.load_diabetes()

#how many samples and How many features?
print(diabetes.data.shape)
#returns (442, 10)

#gives us info about each feature
print(diabetes.DESCR)


# What does feature s6 represent?
print(diabetes.data[6])



#print out the coefficient
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(diabetes.data,diabetes.target, random_state = 11)


# There are three steps to model somehting w sklearn
# 1. Set up the model
mymodel = LinearRegression()

# 2. Use fit to train our model
    #x_train is the data and y_train is the target
mymodel.fit(X_train, y_train)

# print out the coefficient
print(mymodel.coef_)

# print out the intercept
print(mymodel.intercept_)

# 3. Use predict to test your model
predicted = mymodel.predict(X_test) #only give it the data, not the target
                                    #we want it to predict the target
expected = y_test


# create a scatterplot with regression line
plt.plot(expected, predicted, ".")  #the "." is indicating a point on the graph



# create a line of best fit
x = np.linspace(0, 330, 100) #bcs our endpoint is 330
                            #it will create 100 points btwn 0 and 330
print(x)
y = x
plt.plot(x,y)
plt.show()

# this model is not accurate according to the graph