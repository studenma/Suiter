import configparser
from suiter_classes import ConfigDataClass

def create_default_config(file_path):
    """ change the configuration values - used for testing purposes """
    config = configparser.ConfigParser()
    config['URL'] = {
        'url_enum_start': '<',
        'url_enum_end': '>',
        'url_enum_separator': ',',
        'url_variable_start': '<:',
        'url_varaible_end': ':>'
    }
    config['METHOD'] = {
        'method_variable_start': '<:',
        'method_variable_end': ':>'
    }
    config['HEADER'] = {
        'header_enum_start': '<',
        'header_enum_end': '>',
        'header_enum_separator': ',',
        'header_variable_start': '<:',
        'header_variable_end': ':>'
    }
    config['BODY'] = {
        'body_enum_start': '<',
        'body_enum_end': '>',
        'body_enum_separator': ',',
        'body_variable_start': '<:',
        'body_variable_end': ':>'
    }
    config['GENERAL'] = {
        'default_framework': "Pytest",
        'default_input_file': "./unit_tests/test_input/valid.json",
        'default_output_folder': "./result/"
    }
    with open(file_path, 'w') as configfile:
        config.write(configfile)

def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return ConfigDataClass(config)