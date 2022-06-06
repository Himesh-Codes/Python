class QueueToken():
    def __init__(self, *args) -> None:
        self._start = 0
        self._stop = 1
        if len(args) < 1:
            raise TypeError(f'Need atleast one argument, got {len(args)}')
        elif len(args) == 1:
            self._stop = args[0]
        elif len(args) == 2:
            self._start = args[1]

    def __iter__(self):
        self._start += 1
        return self._start
    