# System-Info-Tool-with-Python-Code
A small python tool I coded that displays the CPU, RAM, and Network Info. You can also save it into a text document with one of the folders. Feel free to use and modify it yourself if, you'd like. I am also open to criticism so I can improve and learn stuff I didn't know of before :)





# System Info Tool

A Python script that displays hardware and network information, including CPU usage, memory, disk space, and adapter details.

## Features
- Cross-platform support (Windows, macOS, Linux)
- Real-time system information
- Save system info logs to a text file
- Network adapter and IP summary
- Error handling and user-friendly menu

## Technologies
- Python 3
- psutil
- platform
- datetime
- socket

## Author
Developed by **Jaylen Bell**  
Studying for CompTIA A+, Network+, and Security+ Certifications.



How to use:
## 🧰 Installation & Usage

### Requirements
- **Python:** Version 3.12 or newer (3.14 also works)
- **Library:** psutil

### Setup Steps
1. **Install Python**  
   Download it from [python.org/downloads](https://www.python.org/downloads/)  
   During installation, make sure to check **“Add Python to PATH.”**

2. **Install psutil**  
   Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:
   ```bash
   pip install psutil
Download or Clone This Repository
Click the green Code button above and choose Download ZIP, then extract it.
Or clone it directly:
git clone https://github.com/KyrivaJ/System-Info-Tool-with-Python-Code.git
cd system-info-tool

In the same folder as the script you can run:
python system_tool.py
or
py sys_tool.py

A menu will appear that looks like this:
--- System Tool ---
1) Show system info
2) Exit
3) Save system info to file (with timestamp)
4) Show detailed network info


