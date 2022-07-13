# Python_multiThreading
captures concepts of python multithreading  
# GIL- Global Interpreter Lock in python  
global interpreter lock is basically a mutex (lock) which allows only 1 kernel level thread to run in python  
so even if we use Normal multiThreading in python, we are able to execute potentially only ONE kernel thread at a time instance, even though we may create multiple user level threads  
# Hyperthreading  
with modern hyperthreading oncept CPU cores are logically divided into several Logical Cores, so for example if there are 4 Actual cores and through hyperthreading there are 8 Logical cores, then we are potentially utilizing only 100/8, i.e ONLY 12% of our CPU which is very low  
# for Cpu bound tasks  
this concept leaves CPU intensive tasks with a poor performance because we are utilizing less capability of CPU  
# for I/O bound tasks  
but at the same time I/O tasks are very well handled becuase there we are merely waiting  
# comparison between single threading and multithreading for I/O based tasks  
without multithreading  
![io_without_multi](https://user-images.githubusercontent.com/72104547/178823248-1a4c550c-a84b-44ea-be66-a09bb15eb7cc.png)  
with multithreading  
![io_wit_multi](https://user-images.githubusercontent.com/72104547/178823389-b4423900-b129-4544-afca-b3ef093e9464.png)  
so we can clearly not the difference between time taken for IO task with and without multithreading  
# program output with multithreading  
![m](https://user-images.githubusercontent.com/72104547/178823920-6bf7e9cb-65d4-4382-bb35-4c5bff0f9573.png)  
# program output without multithreading  
![nm](https://user-images.githubusercontent.com/72104547/178824016-fa134640-e2fe-4c02-99d1-df43613b903d.png)  
:)
