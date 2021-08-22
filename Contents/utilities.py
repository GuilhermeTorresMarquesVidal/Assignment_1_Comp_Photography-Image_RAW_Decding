import numpy as np

from .params import limit_up, limit_down

def remove_out_layers(image):
    
    mask = image < limit_down
    image[mask] = limit_down
    mask = image > limit_up
    image[mask] = limit_up
    
    return image

def extract_RGB(CFA, dict_bayer_mask):
    
    R = CFA*dict_bayer_mask['R']
    G = CFA*dict_bayer_mask['G']
    B = CFA*dict_bayer_mask['B']
    
    return R, G, B

def united(R, G, B):
    
    size = R.shape
    
    RGB = np.zeros((size[0], size[1], 3))
    
    RGB[:,:,0] = R.copy()
    RGB[:,:,1] = G.copy()
    RGB[:,:,2] = B.copy()
    
    return RGB