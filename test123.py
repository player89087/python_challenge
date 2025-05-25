import argparse
import requests 
import time 
import sys 

sys.set_int_max_str_digits(10000000) # set the limit higher
start = time.time()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="fibonacci sequence"
    )
    parser.add_argument("-n", required=True, type=int) # amount of places
   
    args = parser.parse_args()

    numb = args.n
    fib_list = [0, 1]
for i in range(0,numb):
    fib_list.append(fib_list[i] + fib_list[i+1])
end = time.time()

dur = end - start
print(f"the number: {fib_list[numb]}\n Time needed: {dur}")

