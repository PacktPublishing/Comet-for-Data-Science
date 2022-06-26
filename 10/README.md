# Comet for Deep Learning

The following example performs image classification. 
As a use case, you will use the Fashion-MNIST, released by Zalando Research and available on GitHub at the [this link](https://github.com/zalandoresearch/fashion-mnist) and released under the MIT license. The dataset contains a training set of 60,000 examples and a test set of 10,000 examples. Each example consists of a 28x28 grayscale image, associated with a label from one of the 10 classes.

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
* the [dashboard](https://www.comet.ml/packt/deep-learning)
* the [report](https://www.comet.ml/packt/deep-learning/reports/clothes-classification)