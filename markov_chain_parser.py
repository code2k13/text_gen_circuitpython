import random

def _custom_random_choices(arr,weights):
    cum_weights = []
    weights_sum = 0
    for i in range(0,len(weights)):
        weights_sum = weights_sum + weights[i]
        cum_weights.append(weights_sum)
    assert abs(1-weights_sum) < 0.0001
    r_weight = random.uniform(0,1)

    start_idx = 0
    end_idx  = len(arr)-1
    middle_idx  = end_idx//2

    while end_idx-start_idx > 2 :
        if cum_weights[middle_idx] <= r_weight:
            start_idx = middle_idx
        else:
            end_idx = middle_idx
        middle_idx = start_idx + ((end_idx-start_idx)//2 )

    if cum_weights[middle_idx] < r_weight:
        return arr[end_idx]
    else:
        if cum_weights[start_idx] > r_weight:
            return arr[start_idx]
        return arr[middle_idx]
    return -1

def generate_text(n,chain):
    op = []
    all_states = list(chain.keys())
    initial_state = random.choice(all_states)
    op.append(initial_state)
    for i in range(0,n):
        possible_next_states = chain[initial_state].keys()
        possible_next_state_weights = list(chain[initial_state].values())
        total = sum(possible_next_state_weights)
        possible_next_state_weights = [n*1.000/total for n in possible_next_state_weights]
        #print(possible_next_state_weights,sum(possible_next_state_weights))
        #next_state = random.choices(list(possible_next_states),k = 1,weights = possible_next_state_weights)[0]
        next_state = _custom_random_choices(list(possible_next_states) ,possible_next_state_weights)
        op.append(next_state)
        initial_state = next_state
    return ''.join(op)
