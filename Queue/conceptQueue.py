class Queue:
  def __init__(self):
    self.queue = []
    self.input_error = 0
    self.dequeue_error = 0
    self.enqueue_count = 0

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)

  def is_empty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)


def concept_queue(commands):
  queue = Queue()

  for command in commands:
    print(f'Step : {command}')
    if command[0] == 'D':
      rnd = int(command[1:])
      for _ in range(rnd):
        if not queue.is_empty():
          queue.dequeue()
        else:
          queue.dequeue_error += 1
      print(f"Dequeue : {queue.queue}")
    elif command[0] == 'E':
      rnd = int(command[1:])
      for _ in range(rnd):
        queue.enqueue(f'*{queue.enqueue_count}')
        queue.enqueue_count += 1
      print(f"Enqueue : {queue.queue}")
    else:
      print(queue.queue)
      queue.input_error += 1

    print(f"Error Dequeue : {queue.dequeue_error}")
    print(f"Error input : {queue.input_error}")
    print('--------------------')


if __name__ == '__main__':
  commands = input("input : ").split(',')

  concept_queue(commands)