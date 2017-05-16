raspberry-jeroen:
	zip -r ../hsleiden-ipsenh-sensor.zip ../hsleiden-ipsenh-sensor
	ssh pi@192.168.1.58 "rm -rf hsleiden-ipsenh-sensor/; exit"
	lftp sftp://pi:raspberry@192.168.1.58  -e "put /Users/jeroen_van_ottelen/Documents/School/Jaar_3/IPSENH/Workspaces/hsleiden-ipsenh-sensor.zip; bye"
	rm -rf /Users/jeroen_van_ottelen/Documents/School/Jaar_3/IPSENH/Workspaces/hsleiden-ipsenh-sensor.zip
	ssh pi@192.168.1.58 "unzip hsleiden-ipsenh-sensor.zip -d ~/; rm -rf hsleiden-ipsenh-sensor/build/*; cd hsleiden-ipsenh-sensor/build/; pyinstaller ../src/main/main.py; ./dist/main/main; rm -rf ~/hsleiden-ipsenh-sensor.zip; exit"