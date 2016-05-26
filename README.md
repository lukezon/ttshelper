# ttshelper
A simple voice activated assistant for specific commands

##install these things:
'''
pip install gTTS
sudo apt-get install python-feedparser python-dnspython mpg123 festival

wget –-no-check-certificate “http://goo.gl/KrwrBa” -O PiAUISuite.tar.gz
tar -xvzf PiAUISuite.tar.gz
cd PiAUISuite/Install/
sudo ./InstallAUISuite.sh
'''

**You must also instal RPi.GPIO if you are not running a recent version of Rasbian.**  
Instructions on how to do that can be found here: [Raspberry Pi Spy Tutorial](http://www.raspberrypi-spy.co.uk/2012/05/install-rpi-gpio-python-library/)

**Create RAMFS file to avoid wear on SD card:**
'''
sudo mkdir -p /mnt/ram
echo "ramfs       /mnt/ram ramfs   nodev,nosuid,nodiratime,size=64M,mode=1777   0 0" | sudo tee -a /etc/fstab 
sudo mount -a
'''

