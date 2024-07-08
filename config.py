import configparser

class ConfigReader:
    
    """
    Class includes some functions that reads the config file and returns dictionaries as result.
    """

    def __init__(self, config_path: str) -> None:
        self.config_path = config_path
        self.config = configparser.ConfigParser()
        read_files = self.config.read(filenames=self.config_path)
        if not read_files:
            print(f"Configuration file {self.config_path} not found or could not be read.")
        else:
            print(f"Configuration file {self.config_path} read successfully.")

    def getSpotifyCredentials(self) -> dict:
        """
        Returns Spotify Credentials as dictionary
        """
        try:
            client_id = self.config.get('SpotifyAPICredentials', 'client_id')
            client_secret = self.config.get('SpotifyAPICredentials', 'client_secret')
            return {
                "client_id": client_id,
                "client_secret": client_secret
            }
        except configparser.NoSectionError as e:
            print(f"Section not found: {e.section}")
        except configparser.NoOptionError as e:
            print(f"Option not found: {e.option}")
        return None
    
    def getApplicationSettings(self) -> dict:
        """
        Returns Application Settings as dictionary
        """
        try:
            output_path = self.config.get('ApplicationSettings', 'output_path')
            output_file_type = self.config.get('ApplicationSettings', 'output_file_type')
            return {
                "output_path": output_path,
                "output_file_type": output_file_type
            }
        except configparser.NoSectionError as e:
            print(f"Section not found: {e.section}")
        except configparser.NoOptionError as e:
            print(f"Option not found: {e.option}")
        return None