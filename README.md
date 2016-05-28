# ttshelper
Group of commands that can be run to give spoken information via Ivona TTS.

##install these things:
```
sudo pip install pyvona
sudo apt-get install libxml2-dev libxslt-dev python-dev
sudo apt-get install python-feedparser python-dnspython mpg123 festival
sudo apt-get install python3-lxml
git clone https://github.com/lukezon/ttshelper.git
```

**It is recommended to use these programs along with StevenHicksons Voice Command System.  Instructions for that can be found [here](https://github.com/StevenHickson/PiAUISuite)**  

**Create RAMFS file to avoid wear on SD card:**
```
sudo mkdir -p /mnt/ram
echo "ramfs       /mnt/ram ramfs   nodev,nosuid,nodiratime,size=64M,mode=1777   0 0" | sudo tee -a /etc/fstab 
sudo mount -a
```

