import math
width = 5 # cheeky
f = open("fitts_law_experiment_log.txt", 'r+')
summary_f = open("summary.csv", 'a')
summary_f.truncate(0)
summary_f.write('A               W               ID              mean time\n')
lines = f.readlines()

log_dict = dict() #amplitude, width, selection number

for line in lines:
    line = line.strip().split(' ')
    name, amplitude, width, selection_number, time = line[0], line[1], line[2], line[3], line[4]
    log_dict[(amplitude, width, selection_number)] = time

for key in log_dict:
    a, w = int(key[0]), int(key[1])
    value = (log_dict.get(key))
    mean_time = (float(value) / 1000)
    id = math.log(a/w + 1)
    summary_f.write(f"{a: <{width}}{w: <{width}}{id:<{width}.2f}{mean_time:<{width}.2f}\n")    
print(log_dict)