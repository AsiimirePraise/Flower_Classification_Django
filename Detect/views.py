from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
import numpy as np
from PIL import Image

# Create your views here.
def classify_flower(request):
    if request.method == 'POST':
        # Load the pre-trained model
        model = load_model('CNN/flowers_model.h5')
        
        class_names = [
            'Daisy',
            'Dandelion', 
            'Rose',
            'Sunflower',
            'Tulip'
        ]
        # Get the image from the request
        flower_image = request.FILES['flower_image']
        
        # Preprocess the image (resize, normalize, etc.)
        image = Image.open(flower_image)
        image = image.resize((150, 150))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        
        # Make prediction
        predictions = model.predict(image)
        predicted_label = np.argmax(predictions[0])
        
        # Get the flower name instead of just the label
        predicted_flower = class_names[predicted_label]
        confidence = float(predictions[0][predicted_label]) * 100
        
        
        return HttpResponse(f'Predicted flower: {predicted_flower} (Confidence: {confidence:.2f}%)')
    
    return render(request, 'detect/classify_flower.html')