import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class readconfigclass:
    @staticmethod
    def get_data_for_email():
        return config.get("login_data", "email_id")
    @staticmethod
    def get_data_for_password():
        return config.get("login_data", "pass_word")
    @staticmethod
    def get_data_for_first_page():
        return config.get("urls", "first_page")
    @staticmethod
    def get_data_login_url():
        return config.get("urls", "login_url")
    @staticmethod
    def get_data_registration_url():
        return config.get("urls", "registration_url")

