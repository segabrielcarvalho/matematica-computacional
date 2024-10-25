from itertools import product

def tabela_verdade():
    print("P\tQ\tM\tR")
    print("-" * 20)
    for P, Q, M in product([True, False], repeat=3):
        cond1 = (not P or Q)
        cond2 = (P or Q)     
        cond3 = (not P or (M and True)) 
        R = cond1 and cond2 and cond3
        
        print(f"{P}\t{Q}\t{M}\t{R}")

tabela_verdade()
