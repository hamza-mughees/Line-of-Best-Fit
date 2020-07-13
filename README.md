# Line of Best Fit

Lately, I have been studying machine learning and specifically looking at linear regression. In linear regression, part of the model-building procedure is to obtain the line of best fit of the correlation between the features and the labels.

I thought I'd build a simple program which reads data from a .csv file and calculates the equation of the line of best fit for the correlation of the data and uses this equation to plot the line.

The data for this program has been obtained from [here](https://zeescorrelationstudy.weebly.com/).

Let X = the independant variable and y = the dependant variable  
The following are the formulas I used to help me calculate the equation of the line of best fit:

<p align="center"><img src="/tex/eb3a5a74038c45aea699e178be46785d.svg?invert_in_darkmode&sanitize=true" align=middle width=124.04194274999999pt height=39.452455349999994pt/></p>

<p align="center"><img src="/tex/cb55d22cab5d700699ea9004e21bd925.svg?invert_in_darkmode&sanitize=true" align=middle width=323.47576964999996pt height=42.024892799999996pt/></p>

Our final equation should be in the form <img src="/tex/b4e68edcfd54c56d10b73a26a2faef8b.svg?invert_in_darkmode&sanitize=true" align=middle width=88.91152214999998pt height=22.831056599999986pt/>

Assuming that we have obtained the standard deviation (sigma) of X as well as y and the correlation coefficient (r), we can calculate the values of b0 and b1 as follows:

<p align="center"><img src="/tex/a8ea54addcf0aac7676ec5bad03c55c5.svg?invert_in_darkmode&sanitize=true" align=middle width=63.861791399999994pt height=31.939908pt/></p>

<p align="center"><img src="/tex/b9cfb5cace9eca4c4da2812e718c4940.svg?invert_in_darkmode&sanitize=true" align=middle width=88.91152215pt height=14.611878599999999pt/></p>

The following is the output of the program when ran against the data from the 'data.csv' file:

<p align="center"><img width=500, src=https://github.com/hamza-mughees/Line-of-Best-Fit/blob/master/output.png></p>
