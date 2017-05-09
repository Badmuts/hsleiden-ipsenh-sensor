from data.DatabaseConnection import *
from api.ApiRegister import *


class main(object):

    def __init__(self):
        database = DatabaseConnection()

        registered = database.checkApiRegister()

        if(not registered):
            api = ApiRegister(database)
            sensors = api.getSensors()
            api_key = api.registerHub(sensors)
            database.registerHUB(api_key)

if __name__ == '__main__':
    # main().__init__()
    main()
