class Node:

	# Constructor
	def __init__(self):
		self.data = None
		self.prev = None
		self.next = None

	# Set data of the Node
	def setData(self, data):
		self.data = data

	# Get data of this Node
	def getData(self):
		return self.data

	# Set previous of the Node
	def setPrev(self, prevAddress):
		self.prev = prevAddress

	# Get data of this Node
	def getPrev(self):
		return self.prev

	# Set next of the Node
	def setNext(self, nextAddress):
		self.next = nextAddress

	# Get data of this Node
	def getNext(self):
		return self.next

	# Get if it has a previous
	def hasPrev(self):
		return self.prev is not None

	# Get if it has a Next
	def hasNext(self):
		return self.next is not None
