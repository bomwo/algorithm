# Stack

가장 마지막에 넣은 데이터를 먼저 뺄 수 있는 구조
LIFO 방식을 사용한다.

스택은 내부 프로세스 구조 함수의 동작으로 사용됨

기능
- push() : 데이터를 밀어 넣는다
- pop() : 가장 마지막 데이터를 꺼낸다.

장점 
구조가 단순하고 구현이 쉬움
데이터 저장/불러오는 속도가 빠름

단점
데이터 최대 갯수를 사전에 정의해줘야함 (python 재귀함수는 1000번까지 가능)
저장 공간 낭비가 발생 할 수 있다 ^ 최대 갯수를 사전에 정의하기 때문에
 

```python

class stack:
    def __init__(self):
        self.mystack = list()

    def push(self, element):
        return self.mystack.append(element)

    def pop(self):
        return self.mystack.pop()
```