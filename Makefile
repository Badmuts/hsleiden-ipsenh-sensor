REPO=badmuts

# Name of the image
IMAGE=hsleiden-ipsenh-sensor

raspberry-jeroen:
	zip -r ../hsleiden-ipsenh-sensor.zip ../hsleiden-ipsenh-sensor
	ssh pi@192.168.1.58 "rm -rf hsleiden-ipsenh-sensor/; exit"
	lftp sftp://pi:raspberry@192.168.1.58  -e "put ../hsleiden-ipsenh-sensor.zip; bye"
	rm -rf ../hsleiden-ipsenh-sensor.zip
	ssh pi@192.168.1.58 "unzip hsleiden-ipsenh-sensor.zip -d ~/; rm -rf ~/hsleiden-ipsenh-sensor.zip; source hsleiden-ipsenh-sensor/venv/bin/activate; cd hsleiden-ipsenh-sensor/src/; python main.py; deactivate; exit"


install:
	# pip install -r requirements.txt
	pip install --user pyinstaller
	sudo apt-get install python-dev python-rpi.gpio
	pip install --user requests


ci: pythonpath ci-test ci-build

pythonpath:
	export PYTHONPATH=$PYTHONPATH:$(pwd)

ci-test:
	python src/test/data_test/DatabaseConnectionTest.py

ci-build:
	pyinstaller src/main.py