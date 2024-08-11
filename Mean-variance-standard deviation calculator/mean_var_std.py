import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    list = np.reshape(list,(3,3))

    calculations = {
    'mean': [np.mean(list,axis=0), np.mean(list,axis=1), np.mean(list)],
    'variance': [np.var(list,axis=0), np.var(list,axis=1), np.var(list)],
    'standard deviation': [np.std(list,axis=0), np.std(list,axis=1), np.std(list)],
    'max': [np.max(list,axis=0), np.max(list,axis=1), np.max(list)],
    'min': [np.min(list,axis=0), np.min(list,axis=1), np.min(list)],
    'sum': [np.sum(list,axis=0), np.sum(list,axis=1), np.sum(list)]
    }

    calculations = {key: [item.tolist() if isinstance(item, np.ndarray) else item for item in value]
                    for key, value in calculations.items()}

    return calculations