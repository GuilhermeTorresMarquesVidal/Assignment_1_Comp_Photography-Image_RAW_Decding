import numpy as np

from .utilities import remove_out_layers

def gamma_correction(image, gamma):
    
    # Gamma encoding
    
    image_with_gamma_correction = np.power(image, gamma)
    
    # Remove out layers
    
    image_with_gamma_correction = remove_out_layers(
        image_with_gamma_correction)
    
    return image_with_gamma_correction