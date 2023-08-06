from Node import Node


class DoublyLinkedList:

	# Constructor
	def __init__(self):
		self.head = Node()
		self.head = None
		self.length = 1

	# ------------------->>>>>>TRAVERSAL<<<<<<-------------------

	# Traversing the list FORWARD
	def listLength_forward(self):
		current = self.head
		count = 0
		while current.getNext() is not None:
			count = count + 1
			current = current.getNext()
		return count

	# Traversing while printing the list FORWARD
	def printList_forward(self):
		if self.head is None:
			print("Empty Linked List")
		else:
			current = self.head
			while current is not None:
				print(current.getData())
				current = current.getNext()

	# Traversing the list BACKWARD
	def listLength_Backward(self):
		current = self.head
		count = 0
		while current.getNext() is not None:
			count = count + 1
			current = current.getNext()
		while current.getPrev() is not None:
			count = count - 1
			current = current.getPrev()
		return count

	# Traversing while printing the list BACKWARD
	def printList_backward(self):
		if self.head is None:
			print("Empty Linked List")
		else:
			current = self.head
			while current.getNext() is not None:
				current = current.getNext()
			while current.getPrev() is not None:
				print(current.getData())
				current = current.getPrev()
			print((current.getData()))


	#------------------->>>>>>INSERTION<<<<<<-------------------

	#****Beginning****#


	def addNodeBeginning(self, data):
		newNode = Node()
		newNode.setData(data)

		if self.head is None:
			self.head = newNode
		else:
			newNode.setNext(self.head)
			newNode.setPrev(None)
			self.head.setPrev(newNode)
			self.head = newNode
		self.length += 1

	# ****End****#

	def addNodeEnd(self, data):
		newNode = Node()
		newNode.setData(data)

		if self.head is None:
			self.head = newNode
		else:
			current = self.head
			while current.getNext() is not None:
				current = current.getNext()
			current.setNext(newNode)
			newNode.setPrev(current)
			newNode.setNext(None)
		self.length += 1

	# ****Travel to given node****#

	def addNodeInPos(self, pos, data):
		if pos > self.length - 1 or pos < 0:
			return None
		elif pos == 0:
			self.addNodeBeginning(data)
		elif pos == self.length - 1:
			self.addNodeEnd(data)
		else:
			newNode = Node()
			newNode.setData(data)
			count = 0
			current = self.head

			while count != pos - 1:
				count += 1
				current = current.getNext()
			newNode.setPrev(current)
			newNode.setNext(current.getNext())
			current.setNext(newNode)
		self.length += 1

	# ------------------->>>>>>DELETION<<<<<<-------------------

    # ****Delete First Node****#

	def deleteFirstNode(self):
		if self.head is None:
			print("Empty Linked List")
			return None
		elif self.head.getNext() is None:
			self.head = None
			print("None")
			self.length -= 1
		else:
			self.head = self.head.getNext()
			self.head.setPrev(None)
			self.length -= 1

	# ****Delete Last Node****#

	def deleteLastNode(self):
		if self.head is None:
			print("Empty Linked List")
			return None
		elif self.head.getNext() is None:
			self.head = None
			print("None")
			self.length -= 1
		else:
			current = self.head
			previous = None
			while current.getNext() is not None:
				previous = current
				current = current.getNext()
			previous.setNext(None)
			self.length -= 1

	# ****Delete Node by position****#

	def deleteNodeByPos(self, pos):
		if self.head is None:
			print("Empty Linked List")
			return None

		if self.length > pos > - 1:
			if pos == 0:
				self.deleteFirstNode()
			elif pos == self.length - 1:
				self.deleteLastNode()
			else:
				count = 0
				current = self.head
				while count != pos - 1:
					count += 1
					current = current.getNext()
				deletingNode = current.getNext()
				nextNode = deletingNode.getNext()
				current.setNext(deletingNode.getNext())
				nextNode.setPrev(current)
				self.length -= 1

	# ------------------->>>>>>SELECTION<<<<<<-------------------

	# Searching for the given data with printing the position of the node
	def Search(self, x):
		current = self.head
		count = 0
		while current.data != x:
			count = count + 1
			current = current.getNext()
		else:
			print("The position of given data is:", count)
			print("The position of previous node is:", count - 1)
			print("The position of next node is:", count + 1)
