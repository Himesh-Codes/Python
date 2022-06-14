class QueueToken():
    def __init__(self, *args) -> None:
        self._step = 1
        self._start = 0
        self._stop = 10
        if len(args) < 1:
            raise TypeError(f'Need atleast one argument, got {len(args)}')
        elif len(args) == 1:
            self._stop = args[0]
        elif len(args) == 2:
            self._start = args[1]
        
        self._current = self._start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current > self._stop:
            raise StopIteration
        else:
            current = self._current
            self._current += self._step
            return current
            
for item in QueueToken(8):
    print(item, end=' ')
        