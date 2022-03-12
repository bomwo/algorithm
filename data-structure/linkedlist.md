# Linked List

연결 리스트라고도 불리는 링크드 리스트는 배열과 달리
연결되지 않고 떨어진 곳에 존재하는 데이터를 경로를 지정하여
관리하는 데이터 구조.
파이썬에서는 리스트 자료구조가 링크드 리스트 기능을 모두 지원함

기능
node : 데이터 저장 단위로 데이터 값 + 포인터로 구성되어 있다.
Point : 각 노드안에서 다음 이나 이전의 노드의 주소를 가지는 값

장점 
미리 데이터 공간을 미리 할당할 필요가 없다

단점
연결을 위한 별도 데이터 공간 (아래 예제에서는 next변수)가 필요하므로 효율이 낮습니다.
데이터를 찾는데 접근성이 안 좋아서 속도가 느립니다.
중간 데이터 삭제시, 앞 뒤를 모두 고려하여 재구성하는 코드를 작성해야 합니다.

node 구현
```python
class Node:
    def __init__(self, data):
        self.data = data # 데이터를 저장하는 node
        self.next = None # 포인터를 대체함
```

Linked List 구현

```python
class Node:
    def __init__(self, data):
        self.data = data # 데이터를 저장하는 node
        self.next = None # 포인터를 대체함
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head: # head가 
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
        pass

    def delete(self, data):
        node = self.head
        if node.data == data:
            self.head = node.next
            del node
        else:
            while node.next:
                next_node = node.next
                if next_node.data == data:
                    node.next = next_node.next
                    del next_node
                else:
                    node = node.next
    
    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
```


# DoubleLinkedList(이중 연결 리스트)
```python
class Node:
    def __init__(self, data):
        self.data = data # 노드
        self.next = None # 포인터
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
```