Name: Jiecao Chen
ID: 4746311

# Instruction for the code

## Problem 3

### diagFisher

Example:

	$ python diagFisher.py Iris.csv 10
	Data:  Iris.csv
	Error rate for cross_validation: 0.0333333333333	

### Fisher

Example:
	
	$ Fisher.py Iris.csv 10
	Data:  Iris.csv
	Error rate for cross_validation: 0.02

### SqClass

Example:
	$ python Sqclass.py Iris.csv 10
	Data:  Iris.csv
	Error rate for cross_validation: 0.186666666667

## Problem 4
The code for this problem was written in matlab, please open
the matlab command window, then for each of the code

### logisticRegression

Example:
	
	> logisticRegression('Pima.csv', 100, [5 10 15 20 25 30])

	train_percent =

	     5    10    15    20    25    30


	meanErrors =

	    0.3823    0.3647    0.3609    0.3456    0.3458    0.3438


	stdVarErrors =

	    0.1146    0.0938    0.0747    0.0723    0.0682    0.0644

### naiveBayesGaussian

Example:

	> naiveBayesGaussian('Pima.csv', 100, [5 10 15 20 25 30])

	train_percent =

	     5    10    15    20    25    30


	meanErrors =

	    0.3001    0.2553    0.2445    0.2362    0.2283    0.2215


	stdVarErrors =

	    0.1792    0.1135    0.1229    0.1144    0.0956    0.0973

Note: for data Ionosphere.csv, my implementation for logisticRegression may
      take 30 secs to give the result. 
