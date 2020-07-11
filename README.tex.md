# Line of Best Fit

Lately, I have been studying machine learning and specifically looking at linear regression. In linear regression, part of the model-building procedure is to obtain the line of best fit of the correlation between the features and the labels.

I thought I'd build a simple program which reads data from a .csv file and calculates the equation of the line of best fit of the correlation of the data.

The data for this program has been obtained from [here](https://zeescorrelationstudy.weebly.com/).

Let x = the independant variable and y = the dependant variable  
The following are the formulas I used to help me calculate the equation of the line of best fit:

$$\sigma=\sqrt{\frac{\sum{(x-\bar{x})}}{n-1}}$$

$$r=\frac{n(\sum{xy})-(\sum{x})(\sum{y})}{\sqrt{[n(\sum{x^{2}})-(\sum{x})^{2}][n(\sum{y^{2}})-(\sum{y})^{2}]}}$$

Our final equation should be in the form $\hat{y}=b_{0}+b_{1}x$

Assuming that we have obtained the standard deviation (sigma) of x as well as y and the correlation coefficient (r), we can calculate the values of b0 and b1 as follows:

$$b_{1}=r\frac{\sigma _{y}}{\sigma _{x}}$$

$$b_{0}=\bar{y}-b_{1}\bar{x}$$