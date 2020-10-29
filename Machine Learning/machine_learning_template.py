import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScalar #Feature Scaling
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures #This is for polynomial linear regression
from sklearn.svm import SVR # this is for Support Vector Regression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


#capital X for matrices and lowercase y for vector

#dataporcessing in Data.csv file
dataset = pd.read_csv('Data.csv')

#takes in features [rows, columns]
X = dataset.iloc[:, :-1].values

#takes in the dependent variable usually just he last column [rows,columns]
y = dataset.iloc[:, -1].values

# Optional this will replace any missing data with the average value of the data in that column
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[X[:, 1:3] = imputer.transform(X[:, 1:3])

#These next lines of code is for Encoding categorical data
#Encoding the Independent Variable
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

#Encoding the Dependent Variable 
le = LabelEncoder()
y = le.fit_transform(y)

#splitting dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#standardization (Xstand = X-mean(x))/standard deviation (X)

#Feature Scaling (Don't use dummy variables), NOT needed in simple or multiple linear regression due to coefficients for each variable. Need Feature Scaling in Support Vector Regression.
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.fit_transform(X_test[:, 3:])

#in Support Vector Regression have to do feature scaling for both x and y like so.
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#reshaping an array for example reshaping dependent variable y if you need to make it a 2D array
y = y.reshape(len(y), 1) #this is basically len(y) rows, and 1 column

#Simple Linear Regression 
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Polynomial regression X is a random variable not from above.
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#Support Vector Regression: from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,y)



#Predicting the Test set results
y_pred = regressor.predict(X_test)

#Predicitng the test results for polynomial
y_pred = lin_reg_2.predict(poly_reg.fit_transform(X))

#Predicting test results for Support Vector Regression....not sure.
y_pred = sc_y.inreverse_transform(regressor.predict(sc_X.fit_transform(X)))

#Visualizing the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualizing the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#Support Vector Regression Visualization 
plt.scatter(sc_X.inreverse_transform, sc_y.inverse_transform(y), color = 'red')
plt.plot(sc_X.inverse_transform(X), sc_y.inverse_transform(regressor.predict(X)), color = 'blue')
plt.title('Salary vs Experience (Support Vector Regression)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#Decision Tree Regression (splits and finding mean of each area)
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,y)

#Predict Decision Tree
y_pred = regressor.predict(regressor([[X_test]])) #array so double []

#Visualization of Decision Tree you can use the Xgrid code for higher resolution curved graph. 
X_grid = np.arrnage(min(X), max(X), 0.1)
X_grid = X_grid_reshape ((len(X_grid), 1))
plt.scatter (X,y, color = 'red')
plt.plot (X_grid, regressor.predict(X_grid), color ='blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Random Forest Regression (marble jar asking different groups of people the estimates)
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)

#Predict Random Forest Regression
regressor.predict([[X_test]])



