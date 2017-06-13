[![Build Status](https://travis-ci.com/Badmuts/hsleiden-ipsenh-sensor.svg?token=8xm9NPdEKiUxFtzhj7Zp&branch=master)](https://travis-ci.com/Badmuts/hsleiden-ipsenh-sensor)





# Raspberry pi configureren
Download Raspbian JESSIE LITE

https://www.raspberrypi.org/downloads/raspbian/

Configureer vervolgens een wifi verbinding zodat de raspberry automatisch daar verbinding mee maakt

# Python
Pi revision numbers

http://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/


**Venv ubuntu**

http://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/


**Venv installeren en aanmaken**

http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/

*Venv starten*
source venv/bin/activate

Controleer welke python wordt gebruikt
which python


**Venv sluiten**

deactivate



**Packages**

| Packages |
| ------ |
| RPi.GPIO |
| sqlite3 |
| requests |
| pyinstaller |


**Interessante Links**
https://realpython.com/blog/python/api-integration-in-python/

**Builden**
pyinstaller --onefile path/to/main.py

--onefile hoeft niet perse 
