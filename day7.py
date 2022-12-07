# NOT my solution. This one stumped me. This code is from https://github.com/PetchyAL/AoC2022/blob/main/solutions/day7/day7.py I'm including it here only so I can come back and break it down. See also https://www.reddit.com/r/adventofcode/comments/zesk40/2022_day_7_solutions/ for other solutions (some of which are very creative). NOTE: I did submit my answers to be sure the code worked. By that time, the Leaderboard had long been set. My submissions were numbers 29859 for Part 1 and 27844 for Part 2. 

from string import digits
from day7_data import data


dir_sizes = dict()
checked_f = dict()
crnt_dir = []

for line in data.split('\n'):
  ln = line.strip()
  #Changing current directory
  if ln.startswith('$ cd'):
    if len(crnt_dir) == 0:
      crnt_dir.append('/')
    elif ln.split(' ')[2] == '/':
      crnt_dir = crnt_dir[0]
    elif ln.split(' ')[2] == '..':
      crnt_dir = crnt_dir[:-1]
    else: crnt_dir.append(ln.split(' ')[2])

  #Get file sizes
  elif ln[0] in digits:
    dir_str = '\\'.join(crnt_dir)
    if dir_str not in checked_f.keys():
      checked_f[dir_str] = []
    if ln.split(' ')[1] not in checked_f[dir_str]:
      checked_f[dir_str].append(ln.split(' ')[1])
      for f in range(len(crnt_dir)+1):
        if '\\'.join(crnt_dir[:f]) not in dir_sizes.keys():
          if '\\'.join(crnt_dir[:f]).strip() == '':
            continue
          dir_sizes['\\'.join(crnt_dir[:f])] = 0
        dir_sizes['\\'.join(crnt_dir[:f])] += int(line.split(' ')[0])

#Part 1
sum = 0
for n in dir_sizes.values():
  if n < 100000:
    sum += n
print(sum)

#Part 2
sort_vals = sorted(dir_sizes.values())
space_needed = 30000000-(70000000-sort_vals[-1])
for n in sort_vals:
  if n >= space_needed:
    print(n)
    break


