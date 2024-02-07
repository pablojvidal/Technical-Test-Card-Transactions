# Credit Card Clustering and Forecasting Analysis

![Header](imgs/header_cc.png)


**Description of technical test:** Birmingham City Council has publish details of all their relevant expenditure of more than £500 within Payments to Suppliers page, and will continue to do so. 

However, the Council started publishing all purchase card transactions, regardless of value, from the April 2014 card statement. 


Where does this data comes from?: Under the Code of Recommended Practice for Local Authorities on Data Transparency, councils are encouraged to publish all corporate purchase card transactions. 

This is a historical dataset, I'm able to perform any of the following
tasks:

**Problem tasks:** 
* (Clustering) Discovering profiles (whether the case) or unusual transactions (anomalies detection)
* (Forecasting) Try to guess future transactional behaviors. 


# Objective

The main objective is to be able to have a merged file of data that allows an analysis of card transactions and to be able to perform clustering and forecasting analysis of the data.

# Hypothesis

Since there is no objective defined by the client or the company we work for, different hypotheses can be defined.

Hypothesis: If a customer always makes large purchases with a card, the model should not identify this as anomalous data if we delete the outliers.
If a customer normally makes relatively low purchases and at some point a very high value purchase is made, then it should be detected as anomalous data. I should not discriminate anomalous data only by value, I should consider the client's behavior to evaluate.


# Notebook files

1- 1.card-transactions-load-and-cleaning.ipynb - Data loading, cleaning and storing the result in one file.

2- 2.card-transactions-analysis.ipynb  - Data explore and modeling.

3- 3.card-transactions-cluster-and-forecasting.ipynb - Clustering, modeling and forecasting using unsupervised approach.



#  Work Pipeline

A pipeline is a series of interconnected data processing and modeling steps designed to streamline the process of working with algorithmic models. For this test i create 3 notebooks in order to perform different activities and solve the problem tasks:

1. Input Data Validation: The pipeline begins by loading and validating the input data. This step ensures that the data is in the expected format, contains relevant features that are common in all the files, and adheres to any necessary constraints. (notebook number 1)
2. Feature Engineering: Next, the pipeline performs feature engineering. This involves transforming raw data into meaningful features that can be used by the model. Feature selection, extraction, and transformation techniques are applied here. (notebook number 1)
3. EDA Analysis: Analyze and investigate the resulting dataset and summarize their main characteristics using data visualization methods. It helps determine the best way to manipulate data sources to get the answers that we need, allowing us to discover patterns, detect anomalies, test a hypothesis, or test assumptions. (notebook number 2)
4. Model Training: The heart of the pipeline! The models used for clustering and forecasting are trained using the processed data. (notebook number 3)
5. Model Evaluation: After training, the model’s performance is evaluated using appropriate metrics (MSE in my case).


Finally, concluding the project by giving marketing strategy based on what we learn from the data. (notebook number 3)

NOTE:There are other steps within a pipeline to work on, such as hyperparameter adjustment, model deployment and monitoring that were not applied in this work.

# Data Description

Link to the dataset: 

Data: https://www.cityobservatory.birmingham.gov.uk/@birmingham-city-council/purchase-card-transactions


There are a lot of features (up to 18 behavioral features). 



# Selected Measure

The selected evaluation metric is the 

*Time Series: MSE*



# Project Organization
------------
    │
    ├── README.md          <- The top-level README for developers using this project.
    ├── dataset            <- Data from third party sources.
    │   ├── unified      <- The final, canonical data sets for modeling.
    │
    ├── imgs               <- Images used in the project.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         dot, and a short `-` delimited description, e.g.
    │                         `1-card-transactions-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                              generated with `pip freeze > requirements.txt`
    
    
# Considerations

For testing purpose, I selected the period between July and December of 2018

The entire execution process takes approximately 30-35 minutes for the selected dataset.

### Equipment and software version

* Intel(R) Core(TM) i5-3570K CPU @ 3.40GHz   3.40 GHz
* 16 GB RAM
* OS Windows 10
* Python version 3.11

There is a requirements.txt file with the necessary libraries if it is necessary to run the project in a local environment.

To install all the packages with requirements.txt is necessary to run the following command

```
pip install -r requirements.txt
```


# Summary and Possible Marketing Strategy

I have learned a lot from this dataset by segmenting the customers into smaller groups: the Average consumer, the Active Users in some categories, the big Spenders, the period of time where exists more number of transactiones. 


To conclude the cluster analysis, let's sum up what we have learned and some possible marketing strategies:

* There are some categories that do not use credit card very much in their daily life. They have healthy finances and low debts (I suppose). While encouraging these people to use credit cards will be more is necessary for the company's profit. Obviously, we must take into account business ethics and social responsibility should also be considered.

* Identify active customers in order to apply proper marketing strategy towards them. These customers are the main group that we should focus on.

# General conclusions about the process:

* The preprocessing exercise in heterogeneous data sources always is  is required to unify the data structure for future analysis and understanding.

* Clustering process gives disagreeing information for the customers ' variables and the "spend" target variable. For example, the cluster model classifies transactions of the same category in different time points in distinct buckets. 

*  The proposed fraud identification model requires a very good regressor to obtain a reliable expenditure estimate, in another hand, the results obtained with the test data suggest that the regression models constructed are not tooreliable. It implies that the classification model would not be reliable either. 

* The time-series analysis of the monthly expenditure on the "directorate" and "trans cac desc 1" fields, allows exploiting the data employing evolutionary graphs, histograms, and business reports, which can be used to audit the expenditure and perform a cost reduction process according to the business sense.

* It is important to be able to establish an adequate communication channel with the client, to understand the business sense of the data involved in the analysis. The expert information could help develop a better model and find hidden relationships more easily. Additionally, this allows being in tune with the business point of view, with the customer's requirements, capabilities, and infrastructure.


# Conclusion

In this project, we have performed data preprocessing, feature extraction, experimented with  Clustering algorithm (KMeans Clustering), data visualizations, and business analytics (a little) at the end.

# Ideas or other approaches for the future

By having so many categorical, text-type variables, natural language processing could be performed and these results used as input for grouping or predictions.

Visualize the clusters created with 3-dimensional graphs to analyze how distinguishable they were from each other. For this, it would be a good idea to have more historical information about clients: age, years of membership, type of card, number of installments, etc.

