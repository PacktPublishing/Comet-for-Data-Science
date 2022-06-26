# Comet for Natural Language Processing

The following example performs sentiment analysis of Disneyland Reviews Dataset, available on Kaggle at [this link](https://www.kaggle.com/datasets/arushchillar/disneyland-reviews)  and released under the  CC0: Public Domain license. 

The dataset contains  42,656 reviews of 3 Disneyland branches (- Paris, California and Hong Kong), posted by visitors on Trip Advisor. For each review, it also provides the rating, which ranges from 1 (totally unsatisfied) to 5 (satisfied). We group ratings into two categories: positive, if the rating is greater than 2, and negative, otherwise. The example compares a pretrained model and a custom model, and shows the results in Comet.

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