from oom_notifier import utils
from typing import Dict, List
import os

__all__: List[str] = ["utils"]

class OOM:
    def __init__(self, proc_path: str = "/proc"):
        self.proc_path = proc_path

    @property
    def _pid_paths(self) -> List[str]:
        return [os.path.join(self.proc_path, pid) for pid in os.listdir(self.proc_path) if pid.isdigit()]

    @property
    def info(self) -> Dict[str, int]:
        ret: Dict[str, int] = {}
        for path in self._pid_paths:
            if not os.path.exists(path):
                continue
            with open(f"{path}/oom_score", "r") as oom_score:
                score: int = int([line.strip() for line in oom_score.readlines()][0])
                ret.update({os.path.basename(path): score})

        return ret

    @property
    def max(self) -> Dict[str, int]:
        largest_score: int = max(self.info.values())
        ret: Dict[str, int] = {"0": 0}
        for pid, score in self.info.items():
            if score == largest_score:
                ret = {pid: score}

        return ret

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.proc_path}')"
