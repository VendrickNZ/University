def average_trials(p_loss):
    return 1/(1 - p_loss)
print (f"{average_trials(0.1):.3f}")