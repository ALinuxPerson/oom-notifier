from typing import Dict
# import oom_notifier
import configparser
import platform
import pathlib
import os

class Configuration:
    def __init__(self, config_directory: str = None):
        self.config: configparser.ConfigParser = configparser.ConfigParser()
        if config_directory is None:
            self.config_directory = self._config_location
        else:
            self.config_directory = config_directory
        if not os.path.exists(self.config_directory):
            pathlib.Path(self.config_directory).mkdir(parents=True, exist_ok=True)
        try:
            self.config.read(f"{self.config_directory}/config.ini")
        except FileNotFoundError:
            self.config.add_section("Main")
            self.config["Main"]["threshold"] = "1000"
            with open(f"{self.config_directory}/config.ini", "w") as config_file:
                self.config.write(config_file)

    @property
    def _config_location(self) -> str:
        home_folder: str = str(pathlib.Path.home())
        os_platform: str = platform.system()
        switch_case: Dict[str, str] = {
            "Linux": f"{home_folder}/.config/oom-notifier",
            "Windows": f"{os.getenv('LOCALAPPDATA')}/oom-notifier",
            "Darwin": f"{home_folder}/Library/Preferences/oom-notifier"
        }

        return switch_case.get(os_platform, switch_case["Linux"])

    @property
    def threshold(self) -> int:
        return int(self.config["Main"]["threshold"])

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.config_directory}')"
