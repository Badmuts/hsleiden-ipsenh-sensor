class Config(object):
    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = super(Config, self).__new__(self)
        return self._instance

    def setConfig(self, config):
        self.config = config

    def get(self, key):
        return self.config[key]

    def getAll(self):
        return self.config