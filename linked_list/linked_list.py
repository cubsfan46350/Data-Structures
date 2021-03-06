"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    elif self.tail and self.head:
      prev_tail = self.tail
      prev_tail.set_next(value)
    self.tail = new_node

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head.next_node is None:
      current_value = self.head
      self.head = None
      self.tail = None
      return current_value
    else:
      current_value = self.head
      self.head = current_value.next_node
      current_value.next_node = None
      return current_value

  def contains(self, value):
    result = self.head
    while result is not None:
      if result.get_value() == value:
        return True
      else:
        result = result.get_next
    return False
  def get_max(self):
    max_node = None
    current = self.head
    if current is not None:
      max_node = current.get_value
    while current is not None:
      if current.get_value() > max_node:
        max_node = current.get_value
      current = current.get_next
    return max_node
