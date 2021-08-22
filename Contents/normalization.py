import numpy as np

from .params import limit_down, limit_up

from .utilities import remove_out_layers

def normalization(CFA, dict_bayer_mask, white_level_per_channel, black_level_per_channel):
    
    CFA_norm = np.zeros_like(CFA)
    
    minimum_new = limit_down
    maximum_new = limit_up
    
    for key in dict_bayer_mask.keys():
        
        CFA_n = (CFA - black_level_per_channel[key])*((maximum_new-minimum_new)/(
            white_level_per_channel[key]-black_level_per_channel[key])) + minimum_new
        
        CFA_filter = CFA_n*dict_bayer_mask[key]
        
        CFA_norm = CFA_norm + CFA_filter
    
    CFA_norm = remove_out_layers(CFA_norm)
    
    return CFA_norm