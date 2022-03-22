from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # node의 value
        self.next = next # 포인터 역할


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_list = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                dummy_list.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                dummy_list.next = list2
                list2 = list2.next
            dummy_list = dummy_list.next
        dummy_list.next = list1 or list2 # 이값이 빠지면 마지막 value 값이 채워지지 않음
        return cur.next
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def add(self, data):
#         newNode = ListNode(data) # 데이터를 추가함
#
#         if self.head is None: # 첫번째 할당 했을때에는 값이 없을꺼니까
#             self.head = newNode
#             # else 를 사용하지 않고 return 바로 리턴해도됨
#         else: # 그렇지 않다면 마지막 노드를 찾아서 노드의 다음 포인터를 새로추가되는 노드로 연결해야하는 과정이 필요함
#             listnode = self.head
#             while listnode.next:
#                 listnode = listnode.next
#
#             listnode.next = newNode
#
#     def find(self):
#         temp = self.head
#         while temp:
#             print(temp.val, end="")
#             temp = temp.next
#
#
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummpylist = ListNode(0)
    while True:
        if list1.val < list2.val:
            dummpylist.next = list1
            list1 = list1.next
        else:
            dummpylist.next = list2
            list2 = list2.next
        dummpylist = dummpylist.next

    return dummpylist.next
#
#
# if __name__ == "__main__":
#     list1 = Linkedlist()
#     list2 = Linkedlist()
#
#     list1.add(1)
#     list1.add(2)
#     list1.add(4)
#
#     list2.add(1)
#     list2.add(3)
#     list2.add(6)
#
#     list1.head = mergeTwoLists(list1.head, list2.head)
#     list1.find()
#
