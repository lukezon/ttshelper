# ttshelper
Group of commands that can be run to give spoken information via Ivona TTS.

##install these things:
```
pip install pyvona

sudo apt-get install libxml2-dev libxslt-dev python-dev
sudo apt-get install python-feedparser python-dnspython mpg123 festival
sudo apt-get install python3-lxml

sudo apt-get install libboost-regex1.49.0
sudo apt-get install git-core
git clone git://github.com/StevenHickson/PiAUISuite.git
cd PiAUISuite/Install/
./InstallAUISuite.sh
```

**You must also instal RPi.GPIO if you are not running a recent version of Rasbian.**  
Instructions on how to do that can be found here: [Raspberry Pi Spy Tutorial](http://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/)

**Create RAMFS file to avoid wear on SD card:**
```
sudo mkdir -p /mnt/ram
echo "ramfs       /mnt/ram ramfs   nodev,nosuid,nodiratime,size=64M,mode=1777   0 0" | sudo tee -a /etc/fstab 
sudo mount -a
```

