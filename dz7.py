def test():    

 b = c = 1      

 numbers = [0, 1, 1]      

 for n in range(100):            

    a = b + c            

    b = c            

    c = a            

    numbers.append(c)      

 print(numbers)

def speed_test():  

 import time  

 t0 = time.time()  

 test()  

 t1 = time.time()  

 complete = t1-t0  
 print(complete)