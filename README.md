# oom-notifier
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/ALinuxPerson/oom-notifier/pulse/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/ALinuxPerson/oom-notifier.svg)](https://github.com/ALinuxPerson/oom-notifier/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/ALinuxPerson/oom-notifier.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/ALinuxPerson/oom-notifier/network/)
[![GitHub stars](https://img.shields.io/github/stars/ALinuxPerson/oom-notifier.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/ALinuxPerson/oom-notifier/stargazers/)
[![GitHub watchers](https://img.shields.io/github/watchers/ALinuxPerson/oom-notifier.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/ALinuxPerson/oom-notifier/watchers/)
[![GitHub followers](https://img.shields.io/github/followers/ALinuxPerson.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/ALinuxPerson?tab=followers)
[![GitHub contributors](https://img.shields.io/github/contributors/ALinuxPerson/oom-notifier.svg)](https://github.com/ALinuxPerson/oom-notifier/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/ALinuxPerson/oom-notifier.svg)](https://GitHub.com/ALinuxPerson/oom-notifier/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/ALinuxPerson/oom-notifier.svg)](https://GitHub.com/ALinuxPerson/oom-notifier/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/ALinuxPerson/oom-notifier.svg)](https://GitHub.com/ALinuxPerson/oom-notifier/pull/)
[![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/ALinuxPerson/oom-notifier.svg)](https://GitHub.com/ALinuxPerson/oom-notifier/pull/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![HitCount](http://hits.dwyl.io/ALinuxPerson/badges.svg)](http://hits.dwyl.io/ALinuxPerson/badges)
[![PyPI download week](https://img.shields.io/pypi/dw/oom-notifier.svg)](https://pypi.python.org/pypi/oom-notifier/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/oom-notifier.svg)](https://pypi.python.org/pypi/oom-notifier/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/oom-notifier.svg)](https://pypi.python.org/pypi/oom-notifier/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/oom-notifier.svg)](https://pypi.python.org/pypi/oom-notifier/)

![product-library](https://i.imgur.com/9ztbONM.png) ![product-notfication](https://i.imgur.com/6oWvzV4.png) ![product-wall](https://i.imgur.com/Xps47Xa.png)

oom-notifier is a program and a library used to track oom scores for Linux.

## Description

oom-notifier gets the oom score of each process by getting the `/proc/<PID>/oom_score` value. As a program, it tracks
the oom scores of each process (by default) every 5 seconds and the threshold is set to 1000. If you want to change these
values, refer to the configuration header below.

But what is an `oom_score`?

An `oom_score` is basically a score assigned to a process by the Linux kernel which is the likelihood that a process will
be terminated in case a computer is out of memory. If a process oom score is high, it means it will be one of the first processes to be killed in case
of low memory resources. If a process oom score is low, it means it will be the least likely to be killed in case of low memory
resources.

## Getting Started

### Dependencies

* Any Linux-based distribution
* Python>=3.6
* pip

### Installing

1. Install `oom-notifier` using pip.
```bash
$ pip install oom-notifier
```

### Usage

As a library:
```python
import oom_notifier

oom = oom_notifier.OOM()

# to get all pids and oom scores of each process, use this:
all_oom_scores = oom.info  # this is a dictionary

# to get the maximum oom score of all processes, use this:
max_oom_score = oom.max  # this is also a dictionary
```
As a program:
```bash
$ oom-notifier  # launches oom-notifier in the background
```

### Configuration
In `~/.config/oom-notifier/config.ini`:
```ini
[Main]
; this sets the threshold to where oom-notifier will trigger a notification if it passes this value
threshold = <NUMBER_HERE>
; this sets the time where oom-notifier will wait to refresh the oom-scores
wait_time = <NUMBER_HERE>
```

## Help

#### **`oom-notifier` only displays in the command line**

This usually means that the dbus can't contact the notification service (as, internally, `dbus-python` raises an exception incase of failure).
AFAIK, most of the time the reason this happens is because the notification service isn't installed.

In XFCE:

Check if `xfce4-notifyd` is running in the background.
```bash
$ ps cax | grep xfce4-notifyd
```
if there's no output, it means xfce4-notifyd isn't running and means it isn't started or isn't installed. If it isn't installed,
you can install using your distribution's package manager.

## License

This project is licensed under the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/) License - see the [LICENSE](https://github.com/ALinuxPerson/oom-notifier/blob/master/LICENSE) file for details
