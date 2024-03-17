from typing import Optional


class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def create_node_list(nums: list) -> ListNode:
    head_node = ListNode(nums[0])
    for num in nums[1:]:
        head_node.next = ListNode(num)
        head_node = head_node.next
    return head_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fake_node = ListNode()
        head_node = fake_node
        remainder = 0

        while l1 or l2 or remainder:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + remainder

            # Каждый раз, когда сумма больше 10 - переносим остаток на следующее число
            remainder = total // 10

            # Число должно быть меньше 10
            head_node.next = ListNode(total % 10)
            head_node = head_node.next

            # Переходим к следующей ноде, если она существует
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Возвращаем первую ноду
        return fake_node.next


l1 = create_node_list([2,4,3])
l2 = create_node_list([5,6,4])

print(Solution().addTwoNumbers(l1, l2).val)
