from dis import dis
import glob
import re
import numpy as np

# Sort strings with a number inside
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


# Get the instance file path and instance name
INSTANCE_PATH = "instance/*"
instances = sorted(glob.glob(INSTANCE_PATH, recursive=True), key=natural_keys)

for instance_dir in instances:
    file_name = instance_dir + instance_dir.replace("instance", "") + ".txt"
    with open(file_name) as f:
        line_ct = 1
        for line in f:
            line_array = line.split()
            if line_ct == 1:
                dim = int(line_array[0])
                factroy_mtx = np.zeros((dim, dim), dtype=np.int64)
                distance_mtx = np.zeros((dim, dim), dtype=np.int64)
            else:
                if 2 <= line_ct <= 1 + dim:
                    for s in range(len(line_array)):
                        factroy_mtx[line_ct-2, s] = int(line_array[s])
                elif 2 + dim <= line_ct:
                    for s in range(len(line_array)):
                        distance_mtx[line_ct-dim-2, s] = int(line_array[s])
            line_ct += 1
