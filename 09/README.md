# Comet for Natural Language Processing - Example

The following example performs sentiment analysis of some text extracted from Twitter. The example compares a pretrained model and a custom model, and shows the results in Comet.

As a use case, you will use the Twitter Sentiment Dataset, available on [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/twitter-sentiment-dataset?resource=download) and released under the Attribution 4.0 International (CC BY 4.0) license.

The dataset contains 162,980 tweets, and for each tweet, it also provides the sentiment, which can be either negative (-1), neutral (0), and positive (+1). In our scenario, we will focus only on positive and negative sentiments, thus we will discard all the neutral tweets.

## Requirements
* You need to create a `.comet.config` file and place it in this directory:
```
[comet]
api_key=YOUR_COMET_API_KEY
workspace=YOUR_WORKSPACE
project_name=YOUR_PROJECT_NAME
```
* You need to install the packages contained in the `requirements.txt` file. To install them, you can runn the following command:

```
pip install -r requirements.txt
```

## Results in Comet
You can see the results in Comet at the following links:
* the [dashboard](https://www.comet.ml/packt/spark-nlp/)
* the [report](https://www.comet.ml/packt/spark-nlp/reports/analysis-of-twitter-sentiment-using-two-models)