from typing import List, Dict

Vector = List[int]


def create_sequences(J: Vector, p: int) -> List[List[int]]:
    """Splitting J into sequences of length p"""

    output = []
    for i, number in enumerate(J):
        sequence = J[i : i + p]
        if len(sequence) == p:
            output.append(sequence)
        else:
            break
    return output


def min_max_moving_avg(J: Vector, p: int) -> Dict[str, float]:
    """
    Calculates the min and max average from a list of lists
    
    params:
    *x = A list of lists of ints
    
    returns:
    Dictionary of the min and max moving averages
    """
    sequences = create_sequences(J, p)

    means = []
    for seq in sequences:
        means.append(sum(seq) / len(seq))

    min_max = {}
    min_max["min"] = min(means)
    min_max["max"] = max(means)

    return min_max

# load necessary data
J = [4, 4, 4, 9, 10, 11, 12]
p = 3

assert min_max_moving_avg(J=J, p=p) == {"min": 4.0, "max": 11.0}