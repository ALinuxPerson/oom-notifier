from plyer import notification
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
