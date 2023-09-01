# nvidia-driverupdate-selenium
Selenium tool that downloads a driver for NVIDIA GPUs when given parameters

What does the tool do?
The tool uses a python script with selenium automation to ask for user's NVIDIA GPU specs and clicks through the website to get the latest version. It also stores the version that was downloaded and stops the process if the version number has not changed (coming soon).

Old version: 1.0, only downloads drivers for a MX230 driver, without checking for a version.

Updated to version 1.5 (current): Tool now asks for user input in a terminal, once user inputs the value corresponding to the GPU they have, it should download the desired driver correctly.

**BUGS**

Windows 11 option crashes the tool. 


This tool was made as a small project, so I recommend you find something better than this for your personal use. This is just a testing ground to learn Selenium and Python.
