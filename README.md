# Bigdue

## Network Packet Analysis

### Raw Packet
<img src="./img/packet_row.png" width="300px" height="150px">

### Map Packet Graph
<img src="./img/packet_map.png" width="600px" height="350px">

### Bubble Packet Graph
<img src="./img/packet_bubble.png" width="400px" height="380px">

### Node Packet Graph
<img src="./img/packet_node.png" width="400px" height="380px">

### Time Packet Graph
<img src="./img/packet_time.png" width="500px" height="300px">

## Project
  1. Visualization
  2. Usage

## Usage methods
  0. clone git repository
  1. python -m venv ./
  2. activate virtual environments
    - (Linux/OSX) source ./bin/activate
    - (Windows) \Scripts\activate
  3. pip install -r requirements.txt
  4. Do something
  5. deactivate virtual environments
    - (Linux/OSX) deactivate
    - (Windows) \Scripts\deactivate

## Installation

## Windows
  #### 0. Clone Bigdue Project
    - $ git clone https://github.com/Boeing737ng/Bigdue.git

  #### 1. Install python3.6v, Download WinPcap, WinPcap Dev Pack
    - python3.6v : https://www.python.org/downloads/
    - WinPcap : https://www.winpcap.org/install/default.htm
    - WinPcap Dev Pack : https://www.winpcap.org/devel.htm

  #### 2. Install Maxmind db
    - GeoLite2 City DB : https://dev.maxmind.com/geoip/geoip2/geolite2/
    - Copy the installed GeoLite2-City.mmdb file under geolite folder
    
  #### 3. Create virtual environments
    - $ python -m venv ./

  #### 4. Download and copy WinPcap Devs files to venv
    - Copy all the file in the "Include" folder which is in "Winpcap dev pack" and paste to "Include" folder in project root directory
    - Copy Packet.lib and wpcap.lib in Winpcap dev pack/"Lib" and paste to "Lib" folder. If you are using 64bits, copy the file from x64 folder
    
  #### 5. Activate virtual environments
    In cmd
    - $ cd Scripts
    - $ activate.bat
    - $ cd ..

    In git bash
    - $ source ./Scripts/activate

  #### 6. Install requirements modules
    - $ pip install -r requirements.txt

  #### 7. Enjoy
    - $ python routes.py
    
## Mac OS / Linux
  #### 0. Clone Bigdue Project
    - $ git clone https://github.com/Boeing737ng/Bigdue.git
    - $ cd Bigdue

  #### 1. Install python3.6v
    - python3.6v : https://www.python.org/downloads/

  #### 2. Install Maxmind db
    - GeoLite2 City DB : https://dev.maxmind.com/geoip/geoip2/geolite2/
    - Copy the installed GeoLite2-City.mmdb file under geolite folder

  #### 3. Create virtual environments
    - $ python3 -m venv ./

  #### 4. Activate virtual environments
    - $ source ./bin/activate

  #### 5. Install requirements modules
    - $ pip3 install -r requirements.txt

  #### 6. Enjoy
    - $ python3 routes.py