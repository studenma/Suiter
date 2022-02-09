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
global_params_with_value = {}
global_params_reserved = []
combine_request = None

list_of_allowed_http_methods = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]

# variables
config_path = '../config.ini'

from suiter_general import tag_substring_evaluation

class ConfigDataClass(object):
    def __init__(self, config):       
        # GENERAL
        self.default_framework = config['GENERAL']['default_framework']
        self.default_input_file = config['GENERAL']['default_input_file']
        self.default_output_folder = config['GENERAL']['default_output_folder']
        # ENDPOINT
        self.endpoint = self.ConfigEndpointClass(config['ENDPOINT'])
        #  METHOD
        self.method = self.ConfigMethodClass(config['METHOD'])
        # HEADER
        self.header = self.ConfigHeaderClass(config['HEADER'])
        # BODY
        self.body = self.ConfigBodyClass(config['BODY'])
        # COMBINATION_LIMIT
        self.limits = self.ConfigLimitClass(config['COMBINATION_LIMIT'])

    def extend_of_priority_tags(self):
        # ENDPOINT start
        priority,non_priority = tag_substring_evaluation(self.endpoint.enum.start, self.endpoint.variable.start)
        self.endpoint.priority_start = priority
        self.endpoint.non_priority_start = non_priority
        # ENDPOINT end
        priority,non_priority = tag_substring_evaluation(self.endpoint.enum.end, self.endpoint.variable.end)
        self.endpoint.priority_end = priority
        self.endpoint.non_priority_end = non_priority
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

    class ConfigEndpointClass(object):
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

    class ConfigLimitClass(object):
        def __init__(self, limits):
            self.final_tc_limit = limits['final_tc_limit']

class InputDataClass(object):
    def __init__(self, json_content):
        self.test_sequence = json_content['test_sequence']
        self.global_params = json_content['global_params']

class CombineCallClass(object):
    def __init__(self):
        self.url = "https://combine.testos.org/generate"
        self.header = {"Content-Type": "application/json"}
        self.body = {
            "name": "SUT name",
            "t_strength": "",
            "dont_care_values": "no",
            "values":"values",
            "parameters": [],
            "constraints": []
        }