# Image-Captioning

Image Captioning is the process of generating textual description of an image. It requires both methods from computer vision to understand the content of the image and a language model from the field of natural language processing to turn the understanding of the image into words in the right order. Recently, deep learning methods have achieved state-of-the-art results on examples of this problem.

### Dataset

Flickr8k dataset (1 GB size) is used for now. Later MS COCO will be used on GCP which is about (14 GB). Flickr8k has 6000 training images with 5 captions each and 1000 each for validation and test set. 

### Model Architecture

#### Image Feature Extractor

This is an Inceptionv3 model pre-trained on the ImageNet dataset. We have pre-processed the photos with the InceptionV3 model (without the output layer) and will use the extracted features predicted by this model as input.

To caption images, we need a Convolutional Neural Network to extract features from an image which is then fed into a Recurrent Neural Network (Long Short Term Memory) along with the captions. The features can be extracted by the models trained on Imagenet. The most popular networks for this are VGG-16, Resnet-50 and InceptionV3. While VGG-16 has more 130 million parameters, InceptionV3 has about 21 million parameters.
 
Keras provides this pre-trained model directly. Instead, we can pre-compute the “image features” using the pre-trained model and save them to file. We can then load these features later and feed them into our model as the interpretation of a given image in the dataset. It is no different to running the image through the full model; it is just we will have done it once in advance. It took about 20 mins for extracting 6000 training images. 

We will remove the last layer from the loaded model, as this is the model used to predict a classification for an image. We are not interested in classifying images, but we are interested in the internal representation of the image right before a classification is made. These are the “features” that the model has extracted from the image.

#### Sequence Processor

This is a word embedding layer for handling the text input, followed by a Long Short-Term Memory (LSTM) recurrent neural network layer.

The model we will develop will generate a caption given an image, and the caption will be generated one word at a time. The sequence of previously generated words will be provided as input. Therefore, we will need a ‘first word’ to kick-off the generation process and a ‘last word‘ to signal the end of the caption. Fir this, we have <start> and <end> as part of each caption. 


#### Output 
Both the feature extractor and sequence processor output a fixed-length vector. These are merged together and processed by a Bidirectional LSTM and then Dense layer to make a final prediction.

The ultimate prediction can be made in two ways - 

1. Argmax Search is where the maximum value index(argmax) in the 8256 long predicted vector is extracted and appended to the result. This is done until we hit <end> or the maximum length of the caption.

2. Beam Search is where we take top k predictions, feed them again in the model and then sort them using the probabilities returned by the model. So, the list will always contain the top k predictions. In the end, we take the one with the highest probability and go through it till we encounter <end> or reach the maximum caption length.

The results can be seen in the jupyter notebook. 


