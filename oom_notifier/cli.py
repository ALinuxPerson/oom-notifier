from plyer import notification
from typing import List
import sys
try:
    import oom_notifier
except EnvironmentError as error:
    print(f"error: {error}")
    sys.exit(2)
import subprocess
import platform
import time
import os

def notify(pid: int, oom_score: int, threshold: int):
    message: str = (f"PID {pid} which has an OOM score of {oom_score} has passed the threshold of {threshold} and will "
                    f"likely be killed.")
    if not os.environ.get("ENVIRON", None) and platform.system() == "Linux":
        command: List[str] = ["wall"]
        command.extend(message.split())
        subprocess.call(command)
        return
    notification.notify(
        title="Warning",
        message=message,
        app_name="OOM Notifier"
    )

def fork():
    if os.fork():
        sys.exit()

def main():
    fork()
    oom: oom_notifier.OOM = oom_notifier.OOM()
    config: oom_notifier.utils.Configuration = oom_notifier.utils.Configuration()
    while True:
        pid, oom_score = tuple(oom.max.items())[0]
        if oom_score > config.threshold:
            notify(pid, oom_score, config.threshold)
        time.sleep(config.wait_time)
