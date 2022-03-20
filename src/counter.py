from functools import partial
from typing import Callable


class _Counter:

    class _MethodCounter:
        def __init__(self):
            self.solved = 0
            self.called = 0

    def __init__(self):
        self._method_counters: dict[str, _Counter._MethodCounter] = dict()
        self.rounds = 0

    def __getitem__(self, item: Callable):
        name = (item.args[0] if isinstance(item, partial) else item).__name__
        return self._method_counters.setdefault(name, self._MethodCounter())
