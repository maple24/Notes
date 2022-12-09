## python requests vs javascript fetch
Although python and javascript are both syncronous programming language by default, python requests module is blocking and javascript fetch/axios module is not.
This means after sending a request, python waits for response, while javascript continues running following codes.
Both have some problems, for python, no further codes proceed until get response back, it is gonna take lots of time waiting. 
For javascript, response may be lost.
Asyncronous is most widely used in such situation. However, multiple threads can also solve the above problem for python since it does not lose data, it is just a matter of time.

## python same module being imported in different files
The imported module is set as a global variable, and only will be imported **once**
```python
# middleware.py
from task import TaskManager
print(TaskManager.queue)
def func():
    from task import TaskManager # not imported again
    print(TaskManager.queue)

# task.py
class TaskManager:
    queue = None

# main.py
from middleware import func
from task import TaskManager # not imported again
TaskManager.queue = 'hello' # assign value to global variable
func()

# output
# >> None
# >> hello
```

## thread with queue
```python
from queue import Queue
from threading import Thread

class p:
    name = None
class q:
    name = None

a = Queue()
p.name = a
q.name = a

def add_p():
    for i in range(20):
        p.name.put(i)
        print(f"add {i}")

def add_q():
    for i in range(10):
        q.name.put(i*10)
        print(f"---add {i*10}")

t1 = Thread(target=add_p)
t2 = Thread(target=add_q)
t1.start()
t2.start()
t1.join()
t2.join()
print("Pullout queue")
for i in a.queue:
    print(i)

# output: p and q share the same queue, the will write into the queue one by one(depending one running situation)
# at the end of day, there will be 30 values in the queue
```