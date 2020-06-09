from typing import Dict
import oom_notifier
import configparser
import platform
import pathlib
import os

class Configuration:
    def __init__(self, config_directory: str = ""):
        pass

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
