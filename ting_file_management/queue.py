class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def __queue__(self):
        return self.queue

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        current_out = self.queue[0]
        self.queue.pop(0)
        return current_out

    def search(self, index):
        if index >= self.__len__() or index < 0:
            raise IndexError
        return self.queue[index]
