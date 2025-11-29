from PIL import Image, ImageOps
import numpy as np

def preprocess_image(uploaded_file):
    """
    Reads the uploaded Streamlit file, converts to PIL image,
    resizes to 224x224, and normalizes it for the model.
    """
    # Open the image directly from the uploaded memory buffer
    img = Image.open(uploaded_file).convert('RGB')
    
    # Resize to match model input
    img = img.resize((224, 224))
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Add batch dimension (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Normalize pixel values
    img_array = img_array / 255.0
    
    return img_array