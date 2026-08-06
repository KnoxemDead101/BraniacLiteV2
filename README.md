# TroubleLog

## Overview

TroubleLog is a lightweight Python command-line application designed to document and organize homelab maintenance, troubleshooting, and system administration tasks.

Originally developed as a learning project, TroubleLog has grown into a practical utility for recording service history across multiple computers and servers. It serves as both a documentation tool and a way to strengthen Python programming skills.

The primary goal of TroubleLog is to maintain a searchable history of system changes while reinforcing software development fundamentals such as file handling, modular programming, version control, and project organization.

---

## Project Goals

* Learn Python through a real-world application.
* Document Linux and Windows system administration tasks.
* Maintain organized service logs for multiple machines.
* Practice Git and professional software development workflows.
* Build a portfolio-quality command-line application.

---

## Current Features

* Create new service logs
* Read existing service logs
* Update existing service logs
* Multi-machine support
* Automatic machine directory creation
* Markdown-based service logs
* Simple command-line interface

---

## Project Structure

```text
TroubleLog/
├── logs/
│   ├── friday/
│   ├── windows-pc/
│   └── macbook/
│
├── src/
│   ├── main.py
│   └── menu.py
│
├── README.md
├── CHANGELOG.md
└── .gitignore
```

---

## Service Log Format

Each service log is stored as a Markdown document.

Example:

```markdown
# Service Log 001

## Machine

Friday

## Title

Installed OpenSSH Server

## Status

Resolved

## Summary

Installed and configured OpenSSH Server for remote administration.
```

---

## Current Version

**v0.2**

Current functionality includes:

* Create Service Log
* Read Service Log
* Update Service Log
* Multi-machine support

---

## Planned Features

### v0.3

* Automatic timestamps
* Delete service logs
* Search logs
* Improved log formatting

### v0.4

* Log categories
* Service history reports
* Log statistics

### v1.0

* Stable command-line release
* Complete documentation
* Cross-platform support
* Production-ready project structure

---

## Technologies

* Python 3
* pathlib
* Markdown
* Git
* Visual Studio Code

---

## Purpose

TroubleLog is one component of the KTT Software Ecosystem.

It is intended to operate as a standalone application while serving as a learning platform for Python, Linux administration, and software engineering principles.

---

## Author

**Leighton Knox**

KTT Software Development

Built to document systems, strengthen programming skills, and support continuous learning through real-world projects.
