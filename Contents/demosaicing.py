import numpy as np

from scipy.ndimage.filters import convolve

from .utilities import remove_out_layers, united

def demosaicing_bayer_bilinear(CFA, dict_bayer_mask):
    
    G_filter = np.array([[0.0, 1.0, 0.0],
                     [1.0, 4.0, 1.0],
                     [0.0, 1.0, 0.0]])
    
    RB_filter = np.array([[1.0, 2.0, 1.0],
                          [2.0, 4.0, 2.0],
                          [1.0, 2.0, 1.0]])
    
    R = convolve(CFA[:,:,0] * dict_bayer_mask['R'], RB_filter)
    G = convolve(CFA[:,:,1] * dict_bayer_mask['G'], G_filter)
    B = convolve(CFA[:,:,2] * dict_bayer_mask['B'], RB_filter)
    
    R = remove_out_layers(R)
    G = remove_out_layers(G)
    B = remove_out_layers(B)
    
    return united(R,G,B)