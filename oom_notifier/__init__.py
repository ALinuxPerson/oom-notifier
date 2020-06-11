# A library/program that gives information about oom scores
# Copyright (C) 2020  ALinuxPerson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from oom_notifier import utils
from typing import Dict, List
import platform
import os

if platform.system() != "Linux":
    raise EnvironmentError(f"unsupported operating system '{platform.system()}'")

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
