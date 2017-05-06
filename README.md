# hsleiden-ipsenh-sensor
Sensor code for RaspberryPi

Installeer Raspberian op een usb
Configureer een wifi connectie

Python:

Venv starten:
Venv starten: source venv/bin/activate

lib:
RPi.GPIO



Node:

Installatie node
wget http://node-arm.herokuapp.com/node_latest_armhf.deb
sudo dpkg -i node_latest_armhf.deb

NPM
sudo apt-get install npm

Packages
https://www.npmjs.com/package/r-pi-usonic
npm install raspi-io
https://www.npmjs.com/package/sqlite3

Handige links
- https://github.com/rwaldron/johnny-five/blob/master/docs/proximity-hcsr04.md


Aantekeningen:
johnny-five is niet mogelijk omdat een raspberry geen ping ondersteund https://github.com/rwaldron/johnny-five/issues/1167

2e test:
npm install raspi-sonar
