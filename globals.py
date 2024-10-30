import instaloader
import argparse
import toml
import os

CONFIG_FILE_NAME = 'config.toml'
BANNER_FILE_NAME = 'banner.txt'

TELEGRAM_TOKEN = None
BANNER = None
USER = None
PSW = None
LOADER = None

def _load_config(profile=None):
    config_file = CONFIG_FILE_NAME
    if profile is not None:
        config_file = f'config-{profile}.toml'
    with open(config_file, 'r') as file:
        config = toml.load(file)
    return config
    
def _load_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', help='Profile to use in config file', required=True)
    return parser.parse_args()
    
def _instaloader_login(username, password):
    L = instaloader.Instaloader()
    session_file = f'session-{username}'
    if os.path.exists(session_file):
        try:
            L.load_session_from_file(username, session_file)
            print("Session loaded successfully!")
            return L
        except Exception as e:
            print(f"Failed to load session: {e}")

    try:
        L.login(username, password)
        L.save_session_to_file(session_file)
        print("Logged in and session saved successfully!")
        return L
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid username or password.")
    except instaloader.exceptions.ConnectionException:
        print("Connection error.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Two-factor authentication required.")
    return L

def load_config():
    global TELEGRAM_TOKEN, BANNER, USER, PSW, LOADER
    try:
        args = _load_args()
        config = _load_config(args.profile)

        with open(BANNER_FILE_NAME, 'r') as banner_file:
            BANNER = banner_file.read()

        TELEGRAM_TOKEN = config['telegram_token']
        USER = config['ig_user']
        PSW = config['ig_psw']
        LOADER = _instaloader_login(USER, PSW)
    except FileNotFoundError as e:
        print(f'++ Unable to load configuration. Make sure config.toml file exists. Error: {e}')
    except toml.TomlDecodeError as e:
        print(f'++ Error decoding TOML file. Please check the syntax of your config file. Error: {e}')
    except Exception as e:
        print(f'++ An unexpected error occurred. Error: {e}')
    return config
