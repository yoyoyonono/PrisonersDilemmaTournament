from typing import Any, Dict, Literal, Tuple, Union
import random
import numpy as np

def strategy(history: np.ndarray, memory: Union[Dict[str, Any], None]) -> Tuple[int, Union[Dict[str, Any], None]]:

    #First Round
    if history.shape[1] == 0:
        memory = {}
        memory['next_prediction'] = 1
        memory['total_defects'] = 0
        return 1, memory

    else:
        if history[1, -1] == 0:
            memory['total_defects'] += 1
            if memory['next_prediction'] != 0:
                if memory['total_defects']/len(history[1]) > 0.3 or memory['total_defects'] > 7:
                    memory['next_prediction'] = 0
                else:
                    memory['next_prediction'] = 1
        else:
            if memory['total_defects']/len(history[1]) > 0.5:
                memory['next_prediction'] = 0
            else:
                memory['next_prediction'] = 1

        return memory['next_prediction'], memory