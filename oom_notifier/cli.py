from plyer import notification
import oom_notifier
import time
import sys
import os

def notify(pid: int, oom_score: int, threshold: int):
    notification.notify(
        title="Warning",
        message=f"PID {pid} which has an OOM score of {oom_score} has passed the threshold of {threshold} and will "
                f"likely be killed.",
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
