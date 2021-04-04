class ConfigDataClass(object):
    def __init__(self, config):
        # TODO: configuration file check - all values should be mandatory
        self.check_config_file(config)
        
        # GENERAL
        self.default_framework = config['GENERAL']['default_framework']
        self.default_input_file = config['GENERAL']['default_input_file']
        self.default_output_folder = config['GENERAL']['default_output_folder']

        # URL
        self.url_enum_start = config['URL']['url_enum_start']
        self.url_enum_end = config['URL']['url_enum_end']
        self.url_enum_separator = config['URL']['url_enum_separator']
        self.url_variable_start = config['URL']['url_variable_start']
        self.url_variable_end = config['URL']['url_varaible_end']

        #  METHOD
        self.method_variable_start = config['METHOD']['method_variable_start']
        self.method_variable_end = config['METHOD']['method_variable_end']

        # HEADER
        self.header_enum_start = config['HEADER']['header_enum_start']
        self.header_enum_end = config['HEADER']['header_enum_end']
        self.header_enum_separator = config['HEADER']['header_enum_separator']
        self.header_variable_start = config['HEADER']['header_variable_start']
        self.header_variable_end = config['HEADER']['header_variable_end']

        # BODY
        self.body_enum_start = config['BODY']['body_enum_start']
        self.body_enum_end = config['BODY']['body_enum_end']
        self.body_enum_separator = config['BODY']['body_enum_separator']
        self.body_variable_start = config['BODY']['body_variable_start']
        self.body_variable_end = config['BODY']['body_variable_end']

    def check_config_file(self, config):
        print("Check config file")