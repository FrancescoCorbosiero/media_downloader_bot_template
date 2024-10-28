import argparse
import toml

CONFIG_FILE_NAME = 'config.toml'
BANNER_FILE_NAME = 'banner.txt'

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

def load_config():
    try:
        args = _load_args()
        config = _load_config(args.profile)
        with open(BANNER_FILE_NAME, 'r') as banner_file:
            config['banner'] = banner_file.read()
    except FileNotFoundError as e:
        print(f'++ Unable to load configuration. Make sure config.toml file exists. Error: {e}')
    except toml.TomlDecodeError as e:
        print(f'++ Error decoding TOML file. Please check the syntax of your config file. Error: {e}')
    except Exception as e:
        print(f'++ An unexpected error occurred. Error: {e}')
    return config
