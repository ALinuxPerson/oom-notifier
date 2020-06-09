from typing import Dict, List
import os

class OOM:
    def __init__(self, proc_path: str = "/proc"):
        self.proc_path = proc_path

    @property
    def _pid_paths(self) -> List[str]:
        return [os.path.join(self.proc_path, pid) for pid in os.listdir(self.proc_path) if pid.isdigit()]

    @property
    def max(self) -> Dict[str, int]:
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.proc_path}')"
