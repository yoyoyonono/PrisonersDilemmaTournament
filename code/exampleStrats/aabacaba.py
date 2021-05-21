from typing import Any, Dict, Literal, Tuple, Union
import random
import numpy as np

def strategy(history: np.ndarray, memory: Union[Dict[str, Any], None]) -> Tuple[int, Union[Dict[str, Any], None]]:
    if history.shape[1] == 0:
        return 1, memory
    else:
        if (100-history.shape[1])/100 < random.random() or history[1, -1] == 0:
            return 0, memory
        else:
            return 1, memory