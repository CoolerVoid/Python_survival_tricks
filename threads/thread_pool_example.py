# threadpool example
import sys
from threading import Thread
import queue
import time

class Worker(Thread):
   def __init__(self,queue):
      super(Worker, self).__init__()
      self._q = queue
      self.daemon = True
      self.start()
   def run(self):
      while True:
         f,args,kwargs = self._q.get()
         try:
            if f(*args, **kwargs)!=None:
                f(*args, **kwargs)
         except Exception as e:
            print(e.message)
         self._q.task_done()

class ThreadPool(object):
   def __init__(self, num_t=max):
      self._q = queue.Queue(num_t)
      # Create Worker Thread
      for _ in range(num_t):
         Worker(self._q)
   def add_task(self,f,*args,**kwargs):
      self._q.put((f, args, kwargs))
   def wait_complete(self):
      self._q.join()

def teste_call(n):
   print("Test number : "+str(n)) 
   time.sleep(3)

if __name__ == '__main__':

# threads ao mesmo tempo rodando no caso 3 ao memso tempo
   pool = ThreadPool(6)

   var=[]
   var.append("opa1")
   var.append("opa2")
   var.append("opa3")
   var.append("opa4")
   var.append("opa5")
   var.append("opa6")

   # quantidade de elementos diferentes
   counter=6

# 3 seria para rodar 3 vezes  
   for _ in range(3):
      for tmp in var:
          # roda 5 threads por vez, cada vez passando um elemento da lista diferente
          if counter!=0:
              pool.add_task(teste_call,tmp) 
              counter-=1
          if counter == 0:
              counter=6  
              pool.wait_complete()
      time.sleep(1)
      print("\nLoop range end\n")
