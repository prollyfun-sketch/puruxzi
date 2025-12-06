# organs/kernel/context.py

class Context:
    def __init__(self, kernel_map=None):
        self.kernel_map = kernel_map or {}
