import MEM
def binarytodec(b):

    i =1
    d =0 
    b=b[::-1]
    for x in b :
        if x == "1":
            d=d+i
        i=i*2
    return d

#deciaml in int binary in str
def dectobinary(d):
    zero=7-len(bin(d)[2:])
    ans="0"*zero+bin(d)[2:]
    return(ans)
def dectobinary_16(d):
    zero=16-len(bin(d)[2:])
    ans="0"*zero+bin(d)[2:]
    return(ans)

def execute(inst, PC, halt):
    #in each condition if flags are not triggered then flag =0
    opcode= inst[0:5]
    # Type A 
    if ( opcode in A ):
        reg_1=reg_codes[inst[7:10]]
        reg_2=reg_codes[inst[10:13]]
        reg_3=reg_codes[inst[13:16]]
        if (A[opcode]=="add"):
            result= reg_val[reg_2]+reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                reg_val["FLAGS"]=8
                
        elif (A[opcode]=="sub"):
            result= reg_val[reg_2]-reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="mul"):
            result= reg_val[reg_2]*reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="xor"):
            result= reg_val[reg_2]^reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="or"):
            result= (reg_val[reg_2])|(reg_val[reg_3])
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8

        elif (A[opcode]=="and"):
            result= reg_val[reg_2]&reg_val[reg_3]
            if (0<= result<=127):
                reg_val[reg_1]=result
                reg_val["FLAGS"]=0
            else:
                #overflow handle crow
                reg_val["FLAGS"]=8
        PC+=1

    # TYPE B 
    elif ( opcode in B):
        reg_1=reg_codes[inst[6:9]]
        imm_val= binarytodec(inst[9:16])

        if (B[opcode]=="mov"):
            reg_val[reg_1]= imm_val
            reg_val["FLAGS"]=0

        elif (B[opcode]=="rs"):
            reg_val[reg_1]= reg_val[reg_1]>>imm_val
            reg_val["FLAGS"]=0

        elif (B[opcode]=="ls"):
            reg_val[reg_1]= reg_val[reg_1]<<imm_val
            reg_val["FLAGS"]=0
        PC+=1
    #TYPE C
    elif ( opcode in C):
        reg_1=reg_codes[inst[10:13]]
        reg_2=reg_codes[inst[13:16]]

        if (C[opcode]=="mov"):

            reg_val[reg_1]=reg_val[reg_2]
            reg_val["FLAGS"]=0

        elif (C[opcode]=="div"):
            if ( reg_2==0):
                #overflow handle crow
                reg_val["FLAGS"]=8
                reg_val["R1"]=0
                reg_val["R0"]=0
            else:
                reg_val["FLAGS"]=0
                quo= reg_1//reg_2
                rem= reg_1%reg_2
                reg_val["R0"]=quo
                reg_val["R1"]=rem

        elif (C[opcode]=="not"):
            reg_val["FLAGS"]=0
            reg_val[reg_1]= ~reg_val[reg_2]

        elif (C[opcode]=="cmp"):
            if  reg_val[reg_1] < reg_val[reg_2]:
                reg_val["FLAGS"]=4

            elif  reg_val[reg_1] > reg_val[reg_2]:
                reg_val["FLAGS"]=2

            elif  reg_val[reg_1] == reg_val[reg_2]:
                reg_val["FLAGS"]=1
        PC+=1
    #TYPE D
    elif ( opcode in D):
        reg_1=reg_codes[inst[6:9]]
        mem_addr= binarytodec(inst[9:16])

        if (D[opcode]=="ld"):
            reg_val[reg_1]= binarytodec( MEM.memory[mem_addr])
            reg_val["FLAGS"]=0

        elif (D[opcode]=="st"):
             MEM.memory[(mem_addr)]=dectobinary_16( reg_val[reg_1])
             reg_val["FLAGS"]=0
        PC+=1
    #TYPE E
    elif ( opcode in E):
        mem_addr= inst[9:16]

        if (E[opcode]=="jmp"):
            PC= binarytodec (mem_addr)
            reg_val["FLAGS"]=0

        elif (E[opcode]=="jlt"):
            if reg_val["FLAGS"]==4:
                PC= binarytodec (mem_addr)
            else:
                PC+=1
        elif (E[opcode]=="jgt"):
            if reg_val["FLAGS"]==2:
                PC= binarytodec (mem_addr)
            else:
                PC+=1

        elif (E[opcode]=="je"):
            if reg_val["FLAGS"]==1:
                PC= binarytodec (mem_addr)
            else:
                PC+=1
        reg_val["FLAGS"]=0
    elif ( opcode in F):
        halt= True
    return halt ,PC
    
    

#reading input from file

A={"00000":"add","00001":"sub","00110":"mul","01010":"xor","01011":"or","01100":"and"}

B={"00010":"mov","01000":"rs","01001":"ls"}

C={"00011":"mov","00111":"div","01101":"not","01110":"cmp"}

D={"00100":"ld","00101":"st"}

E={"01111":"jmp","11100":"jlt","11101":"jgt","11111":"je"}

F={"11010":"hlt"}

reg_codes={"000":"R0","001":"R1","010":"R2","011":"R3","100":"R4","101":"R5","110":"R6","111":"FLAGS"}
reg_val={"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"FLAGS":0}