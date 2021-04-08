# objects
config = ''
inputData = ''

# preparator varaibles
parameters = []
global_variables_to_set = {}
url_param_set = {}  
priority_tag = ''
not_priority_tag = ''
not_priority_tag_end = ''

param_id_counter = 0
all_parameters = []
global_params_with_value = {}

list_of_allowed_http_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"]

# variables
config_path = '../config.ini'

from preparator import tag_substring_evaluation

class ConfigDataClass(object):
    def __init__(self, config):
        # TODO: configuration file check - all values should be mandatory        
        # GENERAL
        self.default_framework = config['GENERAL']['default_framework']
        self.default_input_file = config['GENERAL']['default_input_file']
        self.default_output_folder = config['GENERAL']['default_output_folder']
        # URL
        self.url = self.ConfigUrlClass(config['URL'])
        #  METHOD
        self.method = self.ConfigMethodClass(config['METHOD'])
        # HEADER
        self.header = self.ConfigHeaderClass(config['HEADER'])
        # BODY
        self.body = self.ConfigBodyClass(config['BODY'])

    def extend_of_priority_tags(self):
        # URL start
        priority,non_priority = tag_substring_evaluation(self.url.enum.start, self.url.variable.start)
        self.url.priority_start = priority
        self.url.non_priority_start = non_priority
        # URL end
        priority,non_priority = tag_substring_evaluation(self.url.enum.end, self.url.variable.end)
        self.url.priority_end = priority
        self.url.non_priority_end = non_priority
        # METHOD start
        priority,non_priority = tag_substring_evaluation(self.method.enum.start, self.method.variable.start)
        self.method.priority_start = priority
        self.method.non_priority_start = non_priority
        # METHOD end
        priority,non_priority = tag_substring_evaluation(self.method.enum.end, self.method.variable.end)
        self.method.priority_end = priority
        self.method.non_priority_end = non_priority
        # HEADER start
        priority,non_priority = tag_substring_evaluation(self.header.enum.start, self.header.variable.start)
        self.header.priority_start = priority
        self.header.non_priority_start = non_priority
        # HEADER end
        priority,non_priority = tag_substring_evaluation(self.header.enum.end, self.header.variable.end)
        self.header.priority_end = priority
        self.header.non_priority_end = non_priority
        # BODY start
        priority,non_priority = tag_substring_evaluation(self.body.enum.start, self.body.variable.start)
        self.body.priority_start = priority
        self.body.non_priority_start = non_priority
        # BODY end
        priority,non_priority = tag_substring_evaluation(self.body.enum.end, self.body.variable.end)
        self.body.priority_end = priority
        self.body.non_priority_end = non_priority

    class ConfigUrlClass(object):
        def __init__(self, configUrl):
            self.enum = self.ConfigEnumClass(configUrl)
            self.variable = self.ConfigVariableClass(configUrl)
        class ConfigEnumClass(object):
            def __init__(self, configEnum):
                self.start = configEnum['url_enum_start']
                self.end = configEnum['url_enum_end']
                self.separator = configEnum['url_enum_separator']
        class ConfigVariableClass(object):
            def __init__(self, configVariable):
                self.start = configVariable['url_variable_start']
                self.end = configVariable['url_varaible_end']

    class ConfigMethodClass(object):
        def __init__(self, ConfigMethod):
            self.enum = self.ConfigEnumClass(ConfigMethod)
            self.variable = self.ConfigVariableClass(ConfigMethod)
        class ConfigEnumClass(object):
            def __init__(self, configEnum):
                self.start = configEnum['method_enum_start']
                self.end = configEnum['method_enum_end']
                self.separator = configEnum['method_enum_separator']
        class ConfigVariableClass(object):
            def __init__(self, configVariable):
                self.start = configVariable['method_variable_start']
                self.end = configVariable['method_variable_end']

    class ConfigHeaderClass(object):
        def __init__(self, header):
            self.enum = self.ConfigEnumClass(header)
            self.variable = self.ConfigVariableClass(header)
        class ConfigEnumClass(object):
            def __init__(self, configEnum):
                self.start = configEnum['header_enum_start']
                self.end = configEnum['header_enum_end']
                self.separator = configEnum['header_enum_separator']
        class ConfigVariableClass(object):
            def __init__(self, configVariable):
                self.start = configVariable['header_variable_start']
                self.end = configVariable['header_variable_end']

    class ConfigBodyClass(object):
        def __init__(self, body):
            self.enum = self.ConfigEnumClass(body)
            self.variable = self.ConfigVariableClass(body)
        class ConfigEnumClass(object):
            def __init__(self, configEnum):
                self.start = configEnum['body_enum_start']
                self.end = configEnum['body_enum_end']
                self.separator = configEnum['body_enum_separator']
        class ConfigVariableClass(object):
            def __init__(self, configVariable):
                self.start = configVariable['body_variable_start']
                self.end = configVariable['body_variable_end']

class InputDataClass(object):
    def __init__(self, json_content):
        self.test_sequence = json_content['test_sequence']
        self.global_params = json_content['global_params']
        self.main_level_tway = json_content['t-way']