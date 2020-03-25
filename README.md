# SIZE.AI

This Web Application was developed using: Python, Flask, Pytorch, and HTML

The CSRNet DNN Model, Training, and Testing, was adapted from: https://www.analyticsvidhya.com/blog/2019/02/building-crowd-counting-model-python/

The Flask Develeopment was adapted from: https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html

## Python

All Flask and Pytorch code was written and compiled in Python 3.7

## Flask

A REST API was developed to accept user input in the form of JPG images and render a tempalte that dispalyed the forward feed through of the test image in our model.
Flask apps can be hosted locally with:

`app = Flask(__name__)`

`@app.route('/', methods=['GET', 'POST'])`

## Pytorch 

The model used the VGG16 CNN structure and was trained with 400 images from the Shanghai DataSet.

## HTML 

Stylistic elements were developed in HTML and CSS.

Using the `render_template` function in Flask, HTML pages could be loaded to a local web Host
