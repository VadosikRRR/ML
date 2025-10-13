# ML

## Description

I upload my own ML projects to this repository. I will also describe the tasks that were solved here.

### Image caption

The solution code is [here](./image_caption/image-captioning.ipynb)

* **Stack**: PyTorch, torchvision, Transformers, datasets, Pillow, numpy, matplotlib
* **Description**: Solving the image caption task using EfficientNet + LSTM / transformer combinations
* Data augmentation has been performed
* Learning the EfficientNet + LSTM model
* Learning the EfficientNet + transformer model

### Text classifier

The solution code is [here](./text_classifier/text_classifier.ipynb)

* **Stack**: PyTorch, SkLearn, catboost, nltk, gensim, Pandas
* **Description**: Building different text classifiers
* the TfIdf + LogisticRegression option has been implemented
* the TfIdf + RandomForestClassifier option has been implemented
* the word2vec/doc2vec + linear models option has been implemented
* the word2vec/doc2vec + LSTM option has been implemented

### Test Task 1

The solution code is [here](./test_task1/testtask.ipynb)

* **Stack**: PyTorch, SkLearn, Pandas, seaborn, numpy
* **Description**: Given a function with unknown coefficients and data. Find the coefficients of this function
* Pre-selection of several coefficients to bypass local minima
* Final selection of all coefficients

### Other tasks

Other tasks were at the first ML immersion stage