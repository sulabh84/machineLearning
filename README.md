
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

Observation for dataset:  
1) Missing data  
  Solution 1: skip the missing data rows  
  Solution 2: put the mean of all other data  


Categorical variables:  
1) Country - France,spain,germany  
2) Purchased - true or false  
Problem: Characters can not be used for calculation  
Solution: We have convert the values to some integer to calculate  

Dummy Encoding:  
Problem: if we convert France,spain,germany in numbers like 1,2,3 respectively the equation understand it
    as france is lesser than spain and spain is lesser than germany  
Solution: We have to create as many column as many gategories and assign 0 and 1   
  France   Germany  Spain  
    1        0        0  
    0        1        0  
    0        0        1 

 