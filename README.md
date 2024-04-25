# NVIDIA Power Management Tool

This application provides a graphical user interface to adjust the power limits of NVIDIA GPUs on Linux systems. It utilizes `nvidia-smi` for managing power configurations directly from the desktop.

## Features

- **GUI to Adjust Power Limits**: Easily adjust the power limits of your NVIDIA GPU through a user-friendly slider.
- **Real-Time Feedback**: View current power settings directly within the application.

## Prerequisites

- Linux OS with graphical user interface.
- NVIDIA drivers and `nvidia-smi` installed.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/nvidea_power.git
```

## Configuring Sudo for GUI
To allow this application to run without entering a password each time, you can configure sudoers file:
Open a terminal and type:

````
sudo visudo
````

```
yourusername ALL=(ALL) NOPASSWD: /path/to/main.py
```