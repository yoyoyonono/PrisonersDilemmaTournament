from typing import Any, Dict, Literal, Tuple, Union
import random
import numpy as np

def strategy(history: np.ndarray, memory: Union[Dict[str, Any], None]) -> Tuple[int, Union[Dict[str, Any], None]]:

    #First Round
    if history.shape[1] == 0:
        memory = {}
        memory['total_defects'] = 0
        return 1, memory

    #Before 50
    elif history.shape[1] < 50:
        if history[1, -1] == 0:
            memory['total_defects'] += 1
        if memory['total_defects'] > 2:
            return 0, memory
        else:
            return history[1, -1], memory

    #After 50
    else:
        if history[1, -1] == 0:
            memory['total_defects'] += 1
        if memory['total_defects'] > 2:
            return 0, memory
        else:
            return 1, memory