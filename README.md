# Fish Classification App of IOS

## Overview
This is a under developed fishing app I started to learn more about mobile development specfially on IOS along with computer vision and transfer learning.</br>

The app as of now has only one function and that is to classify fish images using a photo either provided from the photo libray on the phone or directly from the camera itself.


### Classification

The main function of the app consisted of a fish classifier capable of successfully classifying around 20 different fish species native to Idaho.

The classifier used transfer learning utilizing ResNet50 as the underlying model. 

#### Detector

A function that's indirectly in the app is a custom fish detector and image cleaner. The detector can locate fish in an image and cut out the remaining image leaving you with a 
clean picture of a fish to use for building a fish classifier with. This saves tons of time during the process of cleaning the images as most fish images scraped from the internet
have a person holding them adding extra noise to the image. This custom detector can save tons of time if a higher quality fish classifier were to be built.


