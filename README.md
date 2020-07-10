# Line of Best Fit

Lately, I have been studying machine learning and specifically looking at linear regression. In linear regression, part of the model-building procedure is to obtain the line of best fit of the correlation between the features and the labels.

I thought I'd build a simple program which reads data from a .csv file and calculates the equation of the line of best fit of the correlation of the data.

The data for this program has been obtained from [here](https://zeescorrelationstudy.weebly.com/).

Let x = the independant variable and y = the dependant variable  
The following are the formulas I used to calculate the equation of the line of best fit:

<img height=50, src="https://render.githubusercontent.com/render/math?math=\sigma=\sqrt{\frac{\sum{(x-\bar{x})}}{n-1}}">

<img height=50, src="https://render.githubusercontent.com/render/math?math=r=\frac{n(\sum{xy})-(\sum{x})(\sum{y})}{\sqrt{[n(\sum{x^{2}})-(\sum{x})^{2}][n(\sum{y^{2}})-(\sum{y})^{2}]}}">

Our final equation should be in the form: 

<img height=25, src="https://render.githubusercontent.com/render/math?math=%5Chat%7By%7D=b_%7B0%7D%2bb_%7B1%7Dx">

Assuming that we have obtained the standard deviation (sigma) and the correlation coefficient (r), we can calculate the values of b0 and b1 as follows:

<img height=35, src="https://render.githubusercontent.com/render/math?math=b_{1}=r\frac{\sigma _{y}}{\sigma _{x}}">

<img height=25, src="https://render.githubusercontent.com/render/math?math=b_{0}=\hat{y}-b_{1}x">
