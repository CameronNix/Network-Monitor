#  Python Network Monitor

A beginner-friendly Python script that monitors devices on a local network using ICMP ping requests. 
The program checks which devices are online or offline and prints their status in real time.

> Built as a first project to explore networking, automation, and Python programming.

---

#  Features

-  Pings devices on your local network  
-  Checks device status every 10 seconds  
-  Displays whether each device is ONLINE or OFFLINE  
-  Easily customizable with your own IP addresses  
-  (Optional) Saves results to a log file for future analysis  

---

# Tech Stack

- **Python 3**  
- [`ping3`](https://pypi.org/project/ping3/) – lightweight ping utility  
- Command Line / Terminal  

---

# Installation

1. **Install Python**  
    [Download Python 3 here](https://www.python.org/downloads/)

2. **Install the required package**

   ```bash
   pip install ping3
   ```

---

# How to Use

1. Download or clone this repository  
2. Open the `network_monitor.py` file  
3. Update the `devices` dictionary with your own IPs and names:

   ```python
   devices = {
       "Router": "192.168.1.1",
       "Laptop": "192.168.1.10",
       "Phone": "192.168.1.14"
   }
   ```

4. Run the script:

   ```bash
   python network_monitor.py
   ```

 The program will continuously print the online/offline status of each device every 10 seconds.

---

# What I Learned

- Writing and running Python scripts  
- Using third-party libraries (`ping3`)  
- Basics of local IP addresses and network pings  
- Troubleshooting with command line tools  
- Real-world applications of programming in electrical engineering  

---

# Future Improvements

- Save status updates to a `.txt` log file  
- Add colored terminal output (green = online, red = offline)  
- Build a simple GUI using `tkinter`  
- Add email/text alerts for offline devices  

---

# About Me

I'm a first-year Electrical Engineering student at **Oregon State University**, exploring projects in **telecommunications**, **Python programming**, and **network tools**.
This is one of my first self-driven coding projects, and I’m continuing to build more.

Feel free to connect with me on Linkedin (https://www.linkedin.com/in/cameron-nix-5bb678371/) More projects to come!
