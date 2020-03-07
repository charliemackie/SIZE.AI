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

def GetStats(file):

    mae = 0
    img = transform(Image.open(file).convert('RGB')).cpu()
    gt_file = h5py.File(file.replace('.jpg','.h5').replace('images','ground_truth'),'r')
    groundtruth = np.asarray(gt_file['density'])
    output = model(img.unsqueeze(0))
    mae += abs(output.detach().cpu().sum().numpy()-np.sum(groundtruth))
    return mae