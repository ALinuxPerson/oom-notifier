from typing import Dict

class OOM:
    def __init__(self, proc_path: str = "/proc"):
        self.proc_path = proc_path

    @property
    def max(self) -> Dict[str, int]:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.proc_path}')"
