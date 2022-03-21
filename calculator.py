import numpy as np
import glob


teams = ['ferr','redb','merc','mcla','alp','alpha','alfa','haas','will','ast']

race_files = glob.glob("r*txt")
race_files.sort()
print(race_files)

column = 0

join = lambda line : (line.replace(" ", "")).lower()

for i in range(len(teams)):
    column = 0
    posit = -1
    with open(race_files[0]) as file:       
        for line in file.readlines():            
            posit+=1
            if teams[i] in join(line):
                print(teams[i])
                print(posit)
            elif not line.strip():
                break
                


