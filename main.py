
import numpy as np 

#size
N = int(input('enter size: ' or 3))
#auto gen function
np.random.shuffle(function:=np.arange(N))

# Custom 
# function = np.array([0,1,2])
# N = len()

def main ():
    state = func_apply()#initial state
    i = 0# nomber of iterations
    while not np.array_equal(state, np.arange(N)):
        state = func_apply(state)
        print(state)
        i+=1
    print (f"\nf() is reapeating it's self after {i} iteration\n{function}")

def func_apply(array=np.arange(N)) -> np.array:
    return array[function]

if __name__ ==  '__main__':
    main()