class QueueToken():
    def __init__(self, *args) -> None:
        self._start = 0
        self._stop = 1
        if len(args) < 1:
            raise TypeError(f'Need atleast one argument, got {len(args)}')

    def __iter__(self):
        return self
    