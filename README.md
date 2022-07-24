# Uctronics SSD1306 display

Display IP, hostname, CPU load, CPU temperature and memory usage on Adafruit SSD1306 display, part of Uctronics Raspberry Pi Rackmount Complete Enclosure.

## Instalation

Install git, pip and Python packages:

```
sudo apt-get install git python3-pip

sudo pip install Adafruit-SSD1306
sudo pip install psutil
sudo pip install pillow
```

Enable I2C interface:

```
sudo raspi-config nonint do_i2c 0
```

Clone this repository:

```
git clone https://github.com/jvaclavovic/uctronics_ssd1306.git
```

Insert into /etc/rc.local:

```
/usr/bin/python3 /home/pi/uctronics_ssd1306/monitoring.py &
```

