# Comet for Data Science

<a href="https://www.packtpub.com/product/practical-deep-learning-at-scale-with-mlflow/9781803241333?utm_source=github&utm_medium=repository&utm_campaign=9781803241333"><img src="https://static.packt-cdn.com/products/9781803241333/cover/smaller" alt="Comet for Data Science" height="256px" align="right"></a>

This is the code repository for [Comet for Data Science](https://www.packtpub.com/product/practical-deep-learning-at-scale-with-mlflow/9781803241333?utm_source=github&utm_medium=repository&utm_campaign=9781803241333), published by Packt.

**Enhance your ability to manage and optimize the life cycle of your data science project**

## What is this book about?
This book provides concepts and practical use cases which can be used to quickly build, monitor, and optimize data science projects. 
Using Comet, you will learn how to manage almost every step of the data science process from data collection through to creating, deploying, and monitoring a machine learning model.

This book covers the following exciting features: 
* Prepare for your project with the right data
* Understand the purposes of different machine learning algorithms
* Get up and running with Comet to manage and monitor your pipelines
* Understand how Comet works and how to get the most out of it
* See how you can use Comet for machine learning
* Discover how to integrate Comet with GitLab
* Work with Comet for NLP, deep learning, and time series analysis

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/B09NC5XJ6D) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
Xclient = boto3.client('sagemaker-runtime')
response = client.invoke_endpoint(
EndpointName=app_name,
ContentType=content_type,
Accept=accept,
Body=payload
)
```

**Following is what you need for this book:**
This book is for anyone who has programming experience, and wants to learn how to manage and optimize a complete data science lifecycle using Comet and other DevOps platforms. 
Although an understanding of basic data science concepts and programming concepts is needed, no prior knowledge of Comet and DevOps is required.

With the following software and hardware list you can run all code files present in the book (Chapter 1-10).

### Software and Hardware List


| Software required                    | OS required                        |
| ------------------------------------ | -----------------------------------|
| Python 3.8                          
  Python librares                      | Windows, Mac OS X, and Linux (Any) |
                                                        |
|0.	comet-ml==3.23.0 
|1.	findspark==1.4.2
|2.	gradio==3.2.2
|3.	matplotlib==3.4.3 
|4.	numpy==1.19.5 
|5.	pandas==1.3.4 
|6.	pandas-profiling==3.1.0  
|7.	pyspark==3.2.1
|8.	scikit-learn==1.0
|9.	seaborn==0.11.2   
|10.	shap==0.40.0
|11.	spark-nlp==3.4.4
|12.	sweetviz==2.1.3
|13. tensorflow==2.8.2                 | Windows, macOS, or Linux If you are using macOS, 
                                         please make sure that the chip is not Apple M1.
                                         To overcome this problem, you can use Google Colab|										 
|Java SE Development Kit 17.0.2        | Windows, macOS, or Linux |
|(optional for Chapter 4, Workspaces,
| Projects, Experiments, and Models)    |                                     |
|Java libraries (optional for Chapter 4,
|Workspaces, Projects, Experiments, and Models):
|1.	comet-java-sdk-1.1.10 
|    weka 3.8.6 |
|R software (optional)|Windows, macOS, or Linux|
|R libraries (optional): |Windows, macOS, or Linux|
|1.	caret 
|2.	cometr 
|Docker|Windows, macOS, or Linux|
|Kubernetes|Windows, macOS, or Linux|
|git|Windows, macOS, or Linux|
|Java 8 (required for Chapter 9, Comet for Natural Language Processing)|Windows, macOS, or Linux|
|Apache Spark 3.1.2|Windows, macOS, or Linux|

The majority of the code in this book can be implemented and executed using the open
source MLflow tool, with a few exceptions where a 14-day full Databricks trial is needed
(sign up at https://databricks.com/try-databricks) along with an AWS
Free Tier account (sign up at https://aws.amazon.com/free/). The following lists
some major software packages covered in this book:

* MLflow 1.20.2 and above
* Python 3.8.10
* Lightning-flash 0.5.0
* Transformers 4.9.2
* SHAP 0.40.0
* PySpark 3.2.1
* Ray[tune] 1.9.2
* Optuna 2.10.0

The complete package dependencies are listed in each chapter's requirements.txt
file or the conda.yaml file in this book's GitHub repository. All code has been tested
to run successfully in a macOS or Linux environment. If you are a Microsoft Windows
user, it is recommended to install WSL2 to run the bash scripts provided in this book:
https://www.windowscentral.com/how-install-wsl2-windows-10. 
It is a known issue that the MLflow CLI does not work properly in the Microsoft Windows
command line. 

Starting from Chapter 3, Tracking Models, Parameters, and Metrics of this book, you
will also need to have Docker Desktop (https://www.docker.com/products/
docker-desktop/) installed to set up a fully-fledged local MLflow tracking server for executing the code in this book. AWS SageMaker is needed in Chapter 8, Deploying a
DL Inference Pipeline at Scale, for the cloud deployment example. VS Code version 1.60 or above (https://code.visualstudio.com/updates/v1_60) is used as the
integrated development environment (IDE) in this book. Miniconda version 4.10.3 or above (https://docs.conda.io/en/latest/miniconda.html) is used
throughout this book for creating and activating virtual environments.

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781803241333_ColorImages.pdf).


### Related products <Other books you may enjoy>
* Engineering MLOps [[Packt]](https://www.packtpub.com/product/engineering-mlops/9781800562882?utm_source=github&utm_medium=repository&utm_campaign=9781800562882) [[Amazon]](https://www.amazon.com/dp/B08PFN73CM)

* Machine Learning Engineering with Python [[Packt]](https://www.packtpub.com/product/machine-learning-engineering-with-python/9781801079259?utm_source=github&utm_medium=repository&utm_campaign=9781801079259) [[Amazon]](https://www.amazon.com/dp/B09CHHK2RJ)

## Get to Know the Author
**Angelica Lo Duca**
is a researcher at the Institute of Informatics and Telematics of the National Research
Council, Italy. She is also an external professor of data journalism at the University of Pisa. Her research
includes data science, data journalism, and web applications. She used to work on network security,
semantic web, linked data, and blockchain. She has published more than 40 scientific papers at national
and international conferences and journals and has participated in many international projects and
events, including as a member of the Program Committee. She is also part of the editorial team of
the HighTech And Innovation Journal. She owns a personal blog, where she publishes articles on her
research interests.

## Part 1: Getting Started with Comet
#### [Chapter 1 - An overview of Comet](01/)
* [First Use Case](01/first-use-case)
* [Second Use Case](01/second-use-case)
#### [Chapter 2 - Exploratory Data Analysis in Comet](02/) 
* [EDA Techniques](02/)
#### [Chapter 3 - Model Evaluation in Comet](03/) 
* [Model Evaluation](03/)
## Part 2: A Deep Dive to Comet
#### [Chapter 4 - Workspaces, Projects, Experiments and Models](04/)
* [Example in R](04/r-example/)
* [Example in Java](04/java-example/)
* [First Use Case Advanced](04/first-use-case-advanced/)
* [Second Use Case Advanced](04/second-use-case-advanced/)
#### [Chapter 5 - Building a Narrative in Comet](05/) 
* [Example 1](05/Example%201.ipynb)
* [Example 2](05/Example%202.ipynb)
#### [Chapter 6 - Integrating Comet into DevOps](06/)
* [Comet REST API](06/comet-rest-api/)
* [Docker Example](06/docker-example/)
* [Kubernetes Example](06/kubernetes-example/)
#### [Chapter 7 - Extending the Gitlab DevOps Platform with Comet](07/) 
* [Docker Example](07/docker-example/)
* [Test Models](07/test-models/)
## Part 3: Examples and Use Cases
#### [Chapter 8 - Comet for Machine Learning](08/)
* [Model Selection](08/Model%20Selection.ipynb)
* [SHAP Value](08/SHAP%20Value.ipynb)
#### [Chapter 9 - Comet for Natural Language Processing](09/)
* [Sentiment Analysis](09/)
#### [Chapter 10 - Comet for Deep Learning](10/)
* [Deep Learning](10/Deep_Learning.ipynb)
#### [Chapter 11 - Comet for Time Series Analysis](11/)
* [Basic Concepts](11/Basic%20concepts%20on%20Time%20Series%20.ipynb)
* [Time Series Analysis](11/Time%20Series%20Analysis.ipynb)

