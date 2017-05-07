from Data.databaseConnection import *
from API_Connection.ApiRegister import *

class main(object):

    def __init__(self):
        database = DatabaseConnection()

        registered = database.checkApiRegister()

        if(not registered):
            api = ApiRegister(database)


if __name__ == '__main__':
    # main().__init__()
    main()
