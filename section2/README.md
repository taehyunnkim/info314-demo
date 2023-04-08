# DDoS Demo

**Prerequisites**
- Install the necessary dependencies
    - `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
    - If pip is not installed, run `python -m ensurepip --upgrade` or `python3 -m ensurepip --upgrade`
        - Or `sudo apt install python3-pip` on Linux
        - Or download the installation script [here](https://bootstrap.pypa.io/get-pip.py) and run the script `python3 get-pip.py`

- Allow incoming connection in Firewall Settings
    - [MacOS](https://support.apple.com/guide/mac-help/change-firewall-settings-on-mac-mh11783/)
    - [Windows](https://stackoverflow.com/questions/36646093/allowing-a-program-through-windows-firewall)


**Botnet DDoS**
- `c2_client.py`: Send commands to bots
- `c2_server.py`: Receive responses from bots
- `bot.py`: Bot

**Standalone DoS**
- `python3 synflood.py -t [target ip] -p 80 -c [number of packets]`