🛠️ IT Support Utilities Toolkit

A collection of lightweight scripts and batch tools designed to assist IT Support and Help Desk teams with common troubleshooting tasks. Built by Bivek Kadel to improve efficiency in system maintenance, diagnostics, and basic application support.

⸻

📁 Features

1. clear_temp.py

Cleans up temporary files from the system to free up disk space and improve performance.

🔧 Usage: Run as admin to remove temp files from the current Windows user.

⸻

2. ping_test.py

Performs basic network checks by pinging commonly used hosts like Google DNS and websites.

📡 Usage: Helps identify network connectivity issues in real-time.

⸻

3. disk_usage.py

Displays total, used, and available disk space on the system.

💽 Usage: Useful for identifying low disk space issues during diagnostics.

⸻

4. zoom_reinstall.bat

A one-click batch file to uninstall and reinstall Zoom on Windows.

🧰 Usage: Solves problems related to corrupted Zoom installations in classrooms or user systems.

⸻

5. zoom_reinstall.sh (macOS)

A shell script to uninstall and reinstall Zoom on macOS.

🖥️ Usage: Resolves issues related to corrupted Zoom installations on macOS systems.

⸻

✅ How to Run

For Windows:
	1.	Ensure Python is installed on your system. You can download it from here.
	2.	Run the following Python scripts using Command Prompt (as Administrator):
	•	Open Command Prompt (Right-click and select Run as administrator).
	•	Run the following commands:
    
**python clear_temp.py
python ping_test.py
python disk_usage.py**
```

3.	To run the Zoom reinstallation batch script (zoom_reinstall.bat):
	•	Open Command Prompt (as Administrator).
	•	Navigate to the folder where zoom_reinstall.bat is located and run:

    #( zoom_reinstall.bat)


For macOS:
	1.	Ensure Python is installed on your system. You can download it from here.
	2.	Run the following Python scripts using Terminal:
	•	Open Terminal.
	•	Run the following commands:

```python
python3 clear_temp.py
python3 ping_test.py
python3 disk_usage.py
```

3.	To run the Zoom reinstallation script (zoom_reinstall.sh):
	1.	Open Terminal.
	2.	Navigate to the folder where the zoom_reinstall.sh file is located:
    cd /path/to/your/script

    3.	Make the script executable by running: chmod +x zoom_reinstall.sh

    4.	Run the script:# (./zoom_reinstall.sh)