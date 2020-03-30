from fastai.vision import *
import os

def analyze_age(image_data):
    defaults.device = torch.device('cpu')

    img = open_image(image_data)

    path = os.path.dirname(os.path.abspath(__file__))

    learn = load_learner(path, 'puppy_or_dog_analysis.pkl')

    pred_class, pred_idx, outputs = learn.predict(img)

    return pred_class
