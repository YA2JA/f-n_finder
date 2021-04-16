
import numpy as np 

#size of the function
N = 5
#gen random function, with size N
np.random.shuffle(function:=np.arange(N))

# Custom
# function = np.array([0,1,2])
# N = len(function)

def main ():
    state = func_apply()#initial state
    i = 0#nomber of iterations
    while not np.array_equal(state, np.arange(N)):
        state = func_apply(state)
        print(f"\nf() after{i} iterations\n{function}")
        i+=1
    print (f"\nf() is reapeating it's self after {i} iterations\n{function}")

def func_apply(array=np.arange(N)) -> np.array:
    return array[function]

if __name__ ==  '__main__':
    main()