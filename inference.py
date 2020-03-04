import json

from commons import get_model

from matplotlib import cm as c

# Custom Imports 
import numpy as np
from matplotlib import pyplot as plt
import h5py
from transform import transform
import PIL.Image as Image

# Access commons
model = get_model()

def get_prediction(file):

    img = transform(Image.open(file).convert('RGB')).cpu() # Added file reference as input from method call
    output = model(img.unsqueeze(0))
    prediction = int(output.detach().cpu().sum().numpy())
    print("Predicted Count : ",int(output.detach().cpu().sum().numpy())) # Output the prediction
    return prediction
