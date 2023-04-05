import pandas as pd
import numpy as np


chat_id = 407415686 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    const = np.array([335 for _ in range(len(x))])
    x = x - const
    return np.log(x).mean()
