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
from plyer import notification
from typing import List
import dbus.exceptions
import oom_notifier
import subprocess
import time
import sys
import os

def notify(pid: int, oom_score: int, threshold: int):
    message: str = (f"PID {pid} which has an OOM score of {oom_score} has passed the threshold of {threshold} and will "
                    f"likely be killed.")
    try:
        notification.notify(
            title="Warning",
            message=message,
            app_name="OOM Notifier"
        )
    except dbus.exceptions.DBusException:
        command: List[str] = ["wall"] + message.split()
        try:
            subprocess.call(command)
        except FileNotFoundError:
            print(message)

def fork():
    if os.fork():
        sys.exit()

def to_high_priority() -> bool:
    try:
        os.nice(-20)
        return True
    except PermissionError:
        return False

def main():
    fork()
    oom: oom_notifier.OOM = oom_notifier.OOM()
    config: oom_notifier.utils.Configuration = oom_notifier.utils.Configuration()
    if not to_high_priority():
        print("info: if you want oom-notifier to run with the highest priority, run this command again as root. if "
              "you get a DistributionNotFound error, it means you need to reinstall oom-notifier as root.")
    print("oom-notifier is now active and running in the background!")
    while True:
        pid, oom_score = tuple(oom.max.items())[0]
        if oom_score > config.threshold:
            notify(pid, oom_score, config.threshold)
        time.sleep(config.wait_time if config.wait_time > 0 else 5)
