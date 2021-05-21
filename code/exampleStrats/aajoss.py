from typing import Any, Dict, Literal, Tuple, Union
import random
import numpy as np

def strategy(history: np.ndarray, memory: Union[Dict[str, Any], None]) -> Tuple[int, Union[Dict[str, Any], None]]:
    #first round
    if history.shape[1] == 0:
        memory = {}
        return 1, memory
    #2-4
    elif history.shape[1] < 5:
        return random.randint(0, 1), memory
    else:
        if (5 - np.count_nonzero(history[1][-5:]))/5 > 0.5 or random.random() < 0.2:
            return 0, memory
        else:
            return 1, memory