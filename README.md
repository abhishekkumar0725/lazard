# Lazard Data Science Challenge

## Requirements
- Python 3
- Pandas
- H5Py
- Numpy
- SKLearn

## Deliverables
- data_cleaning.ipynb - Main data cleaning python notebook
- feature_engineering.py - Supplementary python file for working with features and data
- h5_file.py - Sandbox file for working with h5 files
- model_building.py - Main model building notebook, where I tested and tuned various models
- model/ - contains the pickled models that I found to be best in model_building

## Approach
### Loading Data
I began by cleaning and loading the data. I never worked with H5 files, so learning more about how to use these and operate with them was my biggest difficulty. I had isssues with just using pd.read_hdf5 so I tried various other methods. I converted it into an excel file, an .asci file, and used h5py to try to interpret it. After working through some computer issues, I was able to load up the h5 files using pandas. From there, I began actual cleaning and playing with the given data.

### Cleaning Data
My first thought was clean the news data. The given file gave me a lot of information and wasn't sure if I needed it all. I also had categorical data I wanted to encode into numbers that I could plug into a model. I started by removing any column that had a majority of NaN values, so I could filter out data I thought would not be significant or may be overfit on. I then seperated the text information from the numerical values extracted from the text. I grouped and merged it with the given financial data, to form a single DataFrame full of features. I standardized the all the x data to make sure

### Model Building
In terms of model building, I tested various state of the art regressison models, including Linear Regression, Support Vector Regressions, Stochastic Gradient Descent, and Decision Trees. I ended up finding that Linear Regresssion and SVRs performed the best of the 4 and tuned the hyperparameters of both until I found the best model I could.

## Results

### Monthly Returns
For the montly returns, I found that a Ridge Regression with Alpha = .001 to be the best model for predicting returns. It had an average mean square error of 0.009627294573522913 during cross validation. I also saw the Support Vector Regression with Linear kernel to be another well suited model.

### F1 Monthly Returns
For the F1 monthly returns, I found that a LASSO Regression with Alpha = .05 to be the best model for predicting returns. It had an average mean square error of 0.00821228645879302 during cross validation. I, once again, also saw the Support Vector Regression with Linear kernel to be another well suited model.

## Next Steps

### Text Engineering
If I had more time to work on this, I would have started implementing more text feautres. Sentiment and relevance are great starting steps, but maybe the addition of TF IDF vectorization or entity extraction may have helped in creating a better model.

### Further Feature Engineering
Another change I would implement is incorporating more ways on evaluating the existing features. Whether that was PCA for dimensionality reduction since there were so many different input values or using polynomial features to extract more information. 

### Alternative Data
I would have also implemented more robust machine learning models. I tried some basic regressions and decision trees and hypertuned parameters accordingly; however, I would love to work with some deep learning architecture and see if there was some neural network architecture that would be a better fit than an ordinary linear regression.