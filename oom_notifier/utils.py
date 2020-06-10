from typing import Dict, Union
import configparser
import platform
import pathlib

class Configuration:
    def __init__(self, config_directory: str = None):
        self.config: configparser.ConfigParser = configparser.ConfigParser()
        if config_directory is None:
            self.config_directory = self._config_location
        else:
            self.config_directory = config_directory
        self.config.read(f"{self.config_directory}/config.ini")

    @property
    def _config_location(self) -> str:
        home_folder: str = str(pathlib.Path.home())
        os_platform: str = platform.system()
        switch_case: Dict[str, str] = {
            "Linux": f"{home_folder}/.config/oom-notifier",
            "Darwin": f"{home_folder}/Library/Preferences/oom-notifier"
        }

        return switch_case[os_platform]

    @property
    def config_dict(self) -> Dict[str, configparser.SectionProxy]:
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
