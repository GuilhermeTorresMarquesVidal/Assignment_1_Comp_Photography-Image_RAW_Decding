import numpy as np

from .params import*

from .utilities import remove_out_layers

def gamma_correction(image, gamma):
    
    # Gamma encoding
    
    image_with_gamma_correction = limit_up * np.power(image / limit_up, gamma)
    
    # Remove out layers
    
    image_with_gamma_correction = remove_out_layers(
        image_with_gamma_correction)
    
    return image_with_gamma_correction