#data preprocessing
#no need to import libraries as they are 
#already imported by default and can be seen
#in the PACKAGES section

#we need to set the working directory

#importing dataset
dataset=read.csv('Data.csv')

#no need to classify dependent and independent 
#variables

#taking care of missing data

dataset$Age=ifelse(is.na(dataset$Age),
                   ave(dataset$Age, FUN= function(x)mean(x, na.rm=TRUE)),
                   dataset$Age)
dataset$Salary=ifelse(is.na(dataset$Salary),
                      ave(dataset$Salary, FUN= function(x)mean(x, na.rm=TRUE)),
                      dataset$Salary)

