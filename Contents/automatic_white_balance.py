import numpy as np

from .utilities import remove_out_layers

def automatic_white_balance(image):
    
    # automatic white balance using gray world assumption
    
    # Get the mean for each channel
    
    R_avg = np.mean(image[:,:,0])
    G_avg = np.mean(image[:,:,1])
    B_avg = np.mean(image[:,:,2])
    
    # Calculate alpha and beta
    
    alpha = G_avg/R_avg
    beta = G_avg/B_avg
    
    # Correct the image
    
    image_with_white_balance = np.zeros_like(image)
    
    image_with_white_balance[:,:,0] = alpha * image[:,:,0].copy()
    image_with_white_balance[:,:,1] = image[:,:,1].copy()
    image_with_white_balance[:,:,2] = beta * image[:,:,2].copy()
    
    # Remove out layers
    
    image_with_white_balance = remove_out_layers(
        image_with_white_balance)
    
    return image_with_white_balance