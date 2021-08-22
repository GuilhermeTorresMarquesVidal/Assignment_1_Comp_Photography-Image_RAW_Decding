import numpy as np

def bayer_mask(CFA_colors, color_desc):
    
    RGB_mask = ({'R': np.zeros_like(CFA_colors), 
                 'B': np.zeros_like(CFA_colors), 
                 'G': np.zeros_like(CFA_colors)})
    
    n_channels = np.unique(CFA_colors)
    
    for n_channel, color in zip(n_channels, color_desc):
        
        mask = CFA_colors == n_channel
        
        RGB_mask[chr(color)][mask] = 1
        
    return RGB_mask