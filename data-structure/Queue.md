# Queue
먼저 넣은 데이터를 가장 먼저 꺼내는 데이터 구조
FIFO(선입선출) LILO(후입후출) 방식을 사용합

# 용어
enqueue : 큐에 데이터 넣는 기능을 의미 list append() 메서드와 유사
dequeue : 큐에 데이터를 꺼내는 기능을 의미, list pop() 메서드와 유사함

# python

import queue 라이브러리를 제공하는데 list로 구현이 가능하다

#queue
```python
import queue

data_queue = queue.Queue()
data_queue.put(1) # 1
data_queue.put(2) # 1 - 2
data_queue.put(2) # 1 - 2 - 3
data_queue.get() # 1
data_queue.get() # 2
```

#LIFO

```python
import queue

data_queue = queue.LifoQueue()

data_queue.put(1) # 1 
data_queue.put(2) # 2 - 1
data_queue.put(3) # 3 - 2 - 1
data_queue.get() # 3
data_queue.get() # 2
```

# PriorityQueue
```python
import queue

data_queue = queue.PriorityQueue()
data_queue.put((10, 1)) # (10,1) 
data_queue.put((5, 2))  # (5, 2) - (10,1) 
data_queue.put((15, 3)) # (5, 2) - (10, 1) - (15,3) 
data_queue.get() # (5,2) 출력 
data_queue.get() # (10, 1) 출력

```

# class 로 직접 구현
```python

class Queue:
    def __init__(self):
        self.my_list = list()

    def get(self, element):
        return self.my_list.append(element)

    def put(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)
```

큐는 멀티 테스킹을 위한 프로세스 스케쥴링 방식
