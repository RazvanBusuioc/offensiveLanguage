- We firstly experimented with linear classifiers.
- Talk about naive bayes
- talk about svm - baseline model

- next model was a simple bert model
- bert layer untrainable
- early stopping, etc - tot ce e pe colab
- hyperparameter optimization - could sneak in some shit about taking a long time, bla bla
- choosing the best model and extracting metrics for it - TALK ABOUT WHAT METRICS DID WE EXTRACT
- manual walk through the bad results -> trying to figure what we could improve.

-biss but for bert with cnn


- leave room for a possible UI


/////////////////////////////////////
In this section we will present all the steps that were taken in order to conduct and evaluate our experiments with emphasis on the methods and frameworks that were used.

In the incipient phases of our investigations, we set out to build a simple baseline model for offensive language detection. Methods such as Multinomial Naive Bayes, Random Forest or Support Vector Machines were used. In terms of feature extraction, all these models were built upon a term frequency-inverse document frequency(TF-IDF) approach as we considered this method simple and effective. After conducting the experiments with linear classifiers, we decided to hold on to the SVM approach and refer to it in our thesis as it presented the best overall results.

In the training process we approached 2 methods as follows: 
-training only on the FB-RO-Offense dataset
-transfer learning using both datasets described previously.

In the first case, the model was trained on the validation and train batches from FB-RO-Offense dataset and evaluation was don using the test batch from the same dataset. 
In the case of transfer learning, the model was trained on the whole RO-Offense dataset and on the validation and train batches from FB-RO-Offense dataset. In the same manner as the first approach, evaluation was performed on the test batch from the FB-RO-Offense dataset.

In order to proper evaluate the SVM model, confusion matrices were build for both fine and coarse grained levels of classification as well as for every training approach. Furthermore, for every classification level, evaluation metrics such as accuracy, precision, recall, f1 score were computed. The last step on evaluating this model was to manual test its prediction on some on the spot texts. This step helped us in estimating the model`s capabilities in a real world(??) environment.

The framework that was used in order to experiment and evaluate the previously specified models is Scikit-learn(!CITE!). This framework offers support for all the mentioned linear classifiers as well as for specified evaluation metrics.



The next experiment involved building a model using BERT. More specific, this model was build using the pre-trained RoBERT-base tokenizer and the pre-trained RoBERT-base model(!CITE!) followed by a fully connected feed forward layer. It`s neural architecture will be described in detail during the next section. Early results for this model did not proved as satisfying and, therefore, multiple trials were conducted using this model. A hyperparameter optimization was approached using the Optuna library for Python(!CITE!) and, later on, using Weights and Biases platform(!CITE!). This optimization method brought many improvements and was adopted in the following experiments as well.

In the same manner as for the SVM methodology, the training and evaluation of this model was conducted using the 2 already presented approaches: training on the FB-RO-Offense dataset and transfer learning using the entire RO-Offense dataset and the training batch from FB-RO-Offense dataset.

Evaluation metrics such as confusion matrices, accuracy, precision, recall and f1 scores were computed in order to estimate the performance of the model. In the same manned as for the SVM approach, manual testing was conducted for this model where we noticed a clear improvement in context understanding.

This architecture proved to be more accurate than the linear one but we aspired to build a better model. Therefore, after experimenting with different parameters we decided that a more mature and complex architecture had to be build in order to obtain even better results.



Our last experiment was conducted with RoBert-base layer. This time, we decided to insert a Convolutional Neural Network between the BERT layer and the feed forward network. As for tokenizer we chose the same pre-trained RoBERT-base one in order to keep a certain level of similarity between the 2 BERT models. In the same manner as the previously described approaches, we proceeded towards a 2 way training of the model. For both methods a hyperparameter optimization was performed, each optimization run containing 50 trials.

The same evaluation metrics as for the vanilla BERT model were computed. As the improvement from the previous model was clearly visible we decided to stop experimenting with model architectures and try to fine-tune this last presented model. (!TODO! talk if we fine tune further)

As mentioned previously, a hyperparameter optimization was performed for the 2 BERT architectures. This optimization involved adjustments for the following 4 parameters:
-Batch size
-Learning rate
-Maximum number of tokens to be consumed for a input
-Size of the penultimate fully connected layer of the architecture

Statistics such as parameter importance or parameter values will be discussed in the Results section.

The frameworks and methods that were used in order to experiment and evaluate the previously specified models is Weights and Biases, Optuna, Scikit-learn and Tensorflow.