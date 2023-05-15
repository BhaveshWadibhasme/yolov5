import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt') 

# Image
im = 'https://ultralytics.com/images/zidane.jpg'

# Inference
results = model(im)

results.pandas().xyxy[0]
