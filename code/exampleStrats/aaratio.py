from typing import Any, Dict, Literal, Tuple, Union
import random
import numpy as np

def strategy(history: np.ndarray, memory: Union[Dict[str, Any], None]) -> Tuple[int, Union[Dict[str, Any], None]]:

    #First Round
    if history.shape[1] == 0:
        memory = {}
        memory['next_prediction'] = 1
        return 1, memory

    else:
        if (len(history[1]) - np.count_nonzero(history[1]))/len(history[1]) > 0.1:
            memory['next_prediction'] = 0
        else:
            memory['next_prediction'] = 1

        if memory['next_prediction'] == 0:
            return 0, memory
        else:
            return 1, memory