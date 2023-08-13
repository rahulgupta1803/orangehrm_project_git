import configparser

config = configparser.RawConfigParser()
fPath = "D:\\credence\\Orangehrm_pytest_project\\Configuration\\config.ini"
config.read(fPath)

class ReadConfig():
    @staticmethod
    def getuserName():
        username = config.get('common data','Username')
        return username

    @staticmethod
    def getuserPassword():
        password = config.get("common data","Password")
        return password