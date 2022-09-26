

import numpy as np


def mrr(scores, labels, k):
    # only consider the position of the first passage that hit the ground truth 
    assert len(scores) == len(labels)
    
    reciprocal_rank = 0
    
    for q_id, p_ids in scores.items():
        
        for index, p_id in enumerate(p_ids):
            if index == k:
                break
            
            if p_id in labels[q_id]:
                reciprocal_rank += 1.0 / (index+1)
                break 

    return reciprocal_rank / len(scores)
