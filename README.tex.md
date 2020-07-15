# Line of Best Fit

Lately, I have been studying machine learning and specifically looking at linear regression. In linear regression, part of the model-building procedure is to obtain the line of best fit for the correlation between the features and the labels.

I thought I'd build a simple program which reads data from a .csv file and calculates the equation of the line of best fit for the correlation of the data and uses this equation to plot the line.

The data for this program has been obtained from [here](https://zeescorrelationstudy.weebly.com/).

Let X = the independant variable and y = the dependant variable  
The following are the formulas I used to help me calculate the equation of the line of best fit and the value of R-squared:

**Standard Deviation**

$$\sigma=\sqrt{\frac{\sum{(x-\bar{x})}}{n-1}}$$

**Correlation Coefficient**

$$r=\frac{n(\sum{xy})-(\sum{x})(\sum{y})}{\sqrt{[n(\sum{x^{2}})-(\sum{x})^{2}][n(\sum{y^{2}})-(\sum{y})^{2}]}}$$

After obtaining the line of best fit, the "closeness" of this line to the actual data can be determined with the *coefficient of determination*. The following is the formula of this value:

**Coefficient of Determination (R-Squared)**

$$R^2=1-\frac{\sum{(y_i-\hat{y_i})^2}}{\sum{(y_i-\bar y)^2}}$$

Our final equation should be in the form $\hat{y}=b_{0}+b_{1}x$ where $b_0=\hat{\beta_0}$ and $b_1=\hat{\beta_1}$

Assuming that we have obtained the standard deviation (sigma) of X as well as y and the correlation coefficient (r), we can calculate the values of b0 and b1 as follows:

$$b_{1}=r\frac{\sigma _{y}}{\sigma _{x}}$$

$$b_{0}=\bar{y}-b_{1}\bar{x}$$

The following is the output of the program when ran against the data from the 'data.csv' file:

<p align="center"><img width=500, src=https://github.com/hamza-mughees/Line-of-Best-Fit/blob/master/output_plot.png></p>

The title of the plot is the obtained equation of the line of best fit, as well as the obtained value of R-squared.
