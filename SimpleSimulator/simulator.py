import MEM
import EE
import sys


PC= 0
halt = False
while not halt:
    inst=MEM.fetchdata(PC)
    halt, PC_new= EE.execute(inst, PC, halt)
    #print Pc in bin
    # print values of all registers
    sys.stdout.write(f"{EE.dectobinary(PC)}        {EE.dectobinary_16(EE.reg_val['R0'])} {EE.dectobinary_16(EE.reg_val['R1'])} {EE.dectobinary_16(EE.reg_val['R2'])} {EE.dectobinary_16(EE.reg_val['R3'])} {EE.dectobinary_16(EE.reg_val['R4'])} {EE.dectobinary_16(EE.reg_val['R5'])} {EE.dectobinary_16(EE.reg_val['R6'])} {EE.dectobinary_16(EE.reg_val['FLAGS'])}\n")
    
    PC=PC_new
# print memory 
for i in MEM.memory:
  # print(i)
  sys.stdout.write(i+"\n")

#  for kx in final_list:
#         sys.stdout.write(kx)