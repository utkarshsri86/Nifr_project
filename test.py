## Descriptive  - it consists of organising and summarizing of data 
##.Measure of central tendency - mean , median , mode 
## measure of dispersion- varience 2- standard deviation
##inferencial data - colect data- assumtion or conclusion using some experient 
##Variance is a statistical measure that quantifies the spread or dispersion of a set of data points around their mean (average). It tells us how much the individual data points differ from the average value.

##Covariance is a statistical measure that quantifies the extent to which two random variables change together. It indicates the direction of the linear relationship between the variables.

##  Correlation measures the strength and direction of the linear relationship between two variables, normalized between -1 and 1. Unlike covariance, it is scale-independent, making it easier to interpret.
import pandas as pd

# Read Excel file
file_path = 'c:\Users\utkar\Downloads\2025Project\Book1.xlsx'  # Update this path
data = pd.read_excel(file_path)

# Display first few rows
print(data.head())

# Now you can work with the data