start_capital = 10000
new_capital=start_capital
new_base_capital=start_capital
factor=2
j=0

while j<200:
    new_capital=new_capital+(new_base_capital/10)
    
    if new_capital > start_capital*factor:
        new_base_capital=new_capital
        factor=factor+1
    j=j+1

    print(new_capital)
