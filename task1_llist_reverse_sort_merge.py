class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # --------------------
    # BASIC OPERATIONS
    # --------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # --------------------
    # TASK 1: REVERSE
    # --------------------
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    # --------------------
    # TASK 2: MERGE SORT
    # --------------------
    def merge_sort(self, head=None):
        if head is None:
            head = self.head

        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self._sorted_merge(left, right)

        if head == self.head:
            self.head = sorted_list
        return sorted_list
    
    # Utility function to get the middle of the linked list
    # - 'slow' pointer moves 1 step at a time
    # - 'fast' pointer moves 2 steps
    # When the fast pointer reaches the end, the slow one is at the middle.
    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    # ------------------------------
    # TASK 3: MERGE TWO SORTED LISTS
    # ------------------------------
    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        dummy = Node(0)
        tail = dummy

        a = list1.head
        b = list2.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# --------------------
# DEMONSTRATION
# --------------------
if __name__ == "__main__":
    llist = LinkedList()

    # Insert nodes
    llist.insert_at_end(30)
    llist.insert_at_end(10)
    llist.insert_at_end(40)
    llist.insert_at_end(20)

    print("\nОригінальний список:")
    llist.print_list()

    # Reverse
    llist.reverse()
    print("\nСписок після реверсування:")
    llist.print_list()

    # Sort
    llist.merge_sort()
    print("\nСписок після сортування:")
    llist.print_list()

    # Merge two sorted lists
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(5)

    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    merged = LinkedList.merge_two_sorted_lists(list1, list2)
    print("\nОб’єднаний відсортований список:")
    merged.print_list()