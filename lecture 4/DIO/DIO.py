print("chose pin if in or out: ")

in_put=['in','0']
out_put=['out','1']
ddr=0
i=0

while i<8:
    pin=str(input(f'port A pin{i}: ' )).format().strip()
    if pin in in_put:
        ddr &= ~(0<<(i))
    elif pin in out_put:
        ddr |= (1<<(i))
    else:
        i -= 1
    i+=1
    
ddr="{0:b}".format(ddr)

port="PORTA"

with open ("DIO_init.txt","w") as r:
    r.write(f'void init{port}_DIR (void)\n')
    r.write("{")
    r.write(f'\n\t DDR{port[-1].capitalize()}={ddr};\n')
    r.write("}")  
