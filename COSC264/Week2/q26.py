import numpy
def average_trials(p_loss):
    return 1 / (1 - p_loss)
print (f"{average_trials(0.1):.3f}")

p = 0.2
k = 1000
print(p*((1-p)**(k-1)))