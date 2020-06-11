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
from typing import Dict, Union
import configparser
import pathlib

class Configuration:
    def __init__(self, config_directory: str = f"{str(pathlib.Path.home())}/.config/oom-notifier"):
        self.config: configparser.ConfigParser = configparser.ConfigParser()
        self.config_directory: str = config_directory

    @property
    def config_dict(self) -> Dict[str, configparser.SectionProxy]:
        self.config.read(f"{self.config_directory}/config.ini")
        return dict(self.config.items())

    @property
    def main(self) -> Union[configparser.SectionProxy, Dict[str, str]]:
        return self.config_dict.get("Main", {
            "threshold": "1000",
            "wait_time": "5"
        })

    @property
    def threshold(self) -> int:
        return int(self.main.get("threshold", "1000"))

    @property
    def wait_time(self) -> int:
        return int(self.main.get("wait_time", "5"))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.config_directory}')"
