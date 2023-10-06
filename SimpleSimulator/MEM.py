import sys
def fetchdata(pc):
    return memory[pc]
   
memory=sys.stdin.readlines()

memory = [x.strip() for x in memory]
l= len(memory)
rem= 128-l
for i in range(0,rem):
    memory.append("0"*16)
