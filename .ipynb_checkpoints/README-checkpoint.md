Assignment 2: Part 1 Build Linear Regression Models In Jupyter Notebooks
R-Linear Regression Model Notebook Generation:
    - Used R to perform a simple linear regression analysis using R to model salary based on years of experience.
    - Utilized ggplot2 to perform graphical analaysis
1)
    First step required downloading the data as .csv file and reading the data file into R
        Performed this by read.CSV() function and labelled the file "dataset"

2) Then performed plot(), which utilized a standard function of R and did not require installation or loading to library. The plot was a scatter plot of salary on the y-axis and years of experience on the x-axis.
3) With the plotted data we could then create a linear model of the data- to evaluate the relationship between years of experience and salary. lm() was used to create the linear model of the dataset data. The model was named "Model".
4) "libray(ggplot2) incorporated ggplot2 into our working library. NOTE: had issues at this point as ggplot2 was not installed, went to the main terminal and entered "conda install -c conda-forge r-ggplot2" to perform conda install of the program.
5) Once ggplot2 was downloaded and performed detailed plot with lablled x and y axis with title
6) After generating the plot performed summary of the model to find the p-value and R squared value. (tried to add screen shots but was unsuccessful, reminder to ask how to do this during class**).

Python-Linear Regression Model Notebook Generation
- Used python to perform a simple linear regression analysis using R to model salary based on years of experience.
- Utilized sklearn linear regression and matplotlib plotting functions to generate the plot
  1) Began by downloading the data as a .csv file and importing the data set using import pandas "pd.read_CSV()"
  2) Then utilized the scatter plot function of matplotlib to plot the dataset with years experience being x-axis and salary being y axis
  3) Then used the linear regression funtion from sklearn.linear_model and performed linearregression() and did model.fit() to get a line of best fit.
  4) Then overlayed the regression line and further labelled the graph to generate a clean ploted regression line.
  5) Peformed an evaluation of the model with model.score() to generate a R-squared value.

Saved each notebook and generated HTML files. 