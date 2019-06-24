
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

