
## Download and install:
anaconda for python editor  
https://www.anaconda.com/distribution/#download-section  

## Download R and install:
https://cran.r-project.org/bin/windows/base/  
https://www.rstudio.com/products/rstudio/download/  

## Download data sets from  
https://www.superdatascience.com/pages/machine-learning  

-------------------------------------------------------------------------

### Data sets:
independent variable  
dependent variable  

## Observation for dataset:  
### Missing data  
  Solution 1: skip the missing data rows  
  Solution 2: put the mean of all other data  


### Categorical variables:  
1) Country - France,spain,germany  
2) Purchased - true or false  
Problem: Characters can not be used for calculation  
Solution: We have convert the values to some integer to calculate  

### Dummy Encoding:  
Problem: if we convert France,spain,germany in numbers like 1,2,3 respectively the equation understand it
    as france is lesser than spain and spain is lesser than germany  
Solution: We have to create as many column as many gategories and assign 0 and 1   
  France   Germany  Spain  
    1        0        0  
    0        1        0  
    0        0        1 

### Feature Scalling  
Problem: values of different column will vary from range  
   lets say age is between 27 to 50  
   but salary is between 48000 to 83000  
  this will create issue because of the Eucliden Distance between P1 to P2 = sqrt((x2-x1)^2 + (y2-y1)^2)  
  Y cordinate will dominate the x cordinate  
Solution - We need to do feature scalling where we transform the value between -1 to 1  

# Machine Learning Algorithms

## Regression

### Simple Linear Regression
     y = a + bx  
     Ordinary Least Squares  
        Diff between actual point and the line  
          Sum (y - y^)^2 --> min  
### Multiple Linear Regression
     y = a + b1x1 + b2x2 + b3x3 .... + bnxn
     Caveat -- Assumptions  
        1) Linearity
        2) Homoscedasticity
        3) Multivariate normality
        4) Independence of errors
        5) Lack of multicollinearity
      Dummy Variables (Categorical Column):
	It is not a number
	State - New york / California
	Always add one less dummy variable in equation
	y = z + b1x1 + b2x2 + d1x1
	
### Polynomial Regression
### Support Vector Regression (SVR)
### Decision Tree Regression
### Random Forest Regression

## Classification

### Logistic Regression
### K-Nearest Neighbors (K-NN)
### Support Vector Machine (SVM)
### Naive Bayes
### Decision Tree Classification
### Random Forest Classification

## Clustering

### K-Mean Clustering
### Hierarchical Clustering

