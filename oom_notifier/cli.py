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
        command: List[str] = ["wall"]
        command.extend(message.split())
        subprocess.call(command)

def fork():
    if os.fork():
        sys.exit()

def main():
    fork()
    oom: oom_notifier.OOM = oom_notifier.OOM()
    config: oom_notifier.utils.Configuration = oom_notifier.utils.Configuration()
    print("oom-notifier is now active and running in the background!")
    while True:
        pid, oom_score = tuple(oom.max.items())[0]
        if oom_score > config.threshold:
            notify(pid, oom_score, config.threshold)
        time.sleep(config.wait_time)
