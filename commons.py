import io

from PIL import Image
from torchvision import models
import torchvision.transforms as transforms
import torch

from Pytorch.pythonModel import CSRNet

def get_model():
    model = CSRNet()
    model.load_state_dict(torch.load('/Users/charliemackie/CSRNET_DEPLOYMENT/Pytorch/model.pt', map_location='cpu')) # Where we upload our model (Download model to local)
    model.eval()
    return model