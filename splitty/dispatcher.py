class _Dispatcher:
    def __init__(self, func):
        self.func = func
        self.slots = []

    def __call__(self, args, *rest):
        for func, arg_type in self.slots:
            if isinstance(args, arg_type):
                return func(args, *rest)
        return self.func(args, *rest)

    def register(self, func):
        ann = getattr(func, '__annotations__', {})
        arg_types = tuple(ann.values())
        self.slots.append((func, arg_types))

        def inner(*args):
            return func(*args)
        return inner


def _singledispatch(func):
    return _Dispatcher(func)
