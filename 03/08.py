class Queue:
    def __init__(self, *queue: list[int]) -> None:
        self.queue = list(queue)

    def append(self, *values: int) -> None:
        self.queue += values

    def copy(self) -> 'Queue':
        return Queue(*self.queue)
    
    def pop(self) -> int | None:
        return self.queue.pop(0)
    
    def extend(self, other: 'Queue') -> None:
        self.queue.extend(other.queue)

    def next(self) -> 'Queue':
        return Queue(*self.queue[1:] if self.queue else [])
    
    def __add__(self, other: 'Queue') -> 'Queue':
        return Queue(*(self.queue + other.queue))
    
    def __iadd__(self, other: 'Queue') -> 'Queue':
        self.queue += other.queue
        return self

    def __eq__(self, other: 'Queue') -> bool:
        return self.queue == other.queue
    
    def __rshift__(self, value: int) -> 'Queue':
        return Queue(*self.queue[value:])
    
    def __str__(self) -> str:
        return '[' + ' -> '.join(map(str, self.queue)) + ']' if self.queue else '[]'
    
    def __next__(self) -> 'Queue':
        return self.next()
