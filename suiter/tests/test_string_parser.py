import pytest
import configparser

""" import suiter package """ 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from suiter_preparator import general_string_parser
from suiter_input_parser import create_default_config
from suiter_input_parser import read_config_file
from suiter_exceptions import *

"""
Valid test cases
"""

"""
conf.url_enum_start = '<'
conf.url_enum_end = '>'
conf.url_variable_start = '<:'
conf.url_variable_end = ':>'
"""
test_cases_default = [
    # Test case 0
    [
        'https://mydomain/addUser/<:user:>/<1,2,3>/<:user2:>/<>/<9,8,7>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>', 
        [
            { 'location': 'endpoint', 'type': 'global_variable',    'name': 'user',         'id': 0 },
            { 'location': 'endpoint', 'type': 'enumerate',          'content': '1,2,3',     'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': 'user2',        'id': 2 },
            { 'location': 'endpoint', 'type': 'local_variable',                             'id': 3 },
            { 'location': 'endpoint', 'type': 'enumerate',          'content': '9,8,7',     'id': 4 }
        ]   
    ],
    # Test case 1
    [
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'local_variable',      'id': 0 },
            { 'location': 'endpoint', 'type': 'local_variable',      'id': 1 },
            { 'location': 'endpoint', 'type': 'local_variable',      'id': 2 },
            { 'location': 'endpoint', 'type': 'local_variable',      'id': 3 },
            { 'location': 'endpoint', 'type': 'local_variable',      'id': 4 }
        ]   
    ],
    # Test case 2
    [
        'https://mydomain/addUser/<:a:>/<:b:>/<:c:>/<:d:>/<:e:>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'a',      'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'b',      'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'c',      'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'd',      'id': 3 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'e',      'id': 4 }
        ]   
    ],
    # Test case 3
    # empty variable element: <::>
    [
        'https://mydomain/addUser/<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',                   'id': 0 },
            { 'location': 'endpoint', 'type': 'enumerate', 'content': 'sfnsfsfsjkfns',      'id': 1 },
            { 'location': 'endpoint', 'type': 'enumerate', 'content': '--',                 'id': 2 },
            { 'location': 'endpoint', 'type': 'local_variable',                 'id': 3 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 4
    [
        '<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        '<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',                   'id': 0 },
            { 'location': 'endpoint', 'type': 'enumerate', 'content': 'sfnsfsfsjkfns',      'id': 1 },
            { 'location': 'endpoint', 'type': 'enumerate', 'content': '--',                 'id': 2 },
            { 'location': 'endpoint', 'type': 'local_variable',                  'id': 3 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 5
    # random characters
    [
        '::::::<><:%$#^&!()*&#:><:\n:><123,456,789,789>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        '::::::<><><><>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        [
            { 'location': 'endpoint', 'type': 'local_variable',                     'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '%$#^&!()*&#',           'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '\n',                    'id': 2 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '123,456,789,789',       'id': 3 }
        ]   
    ],
    # Test case 6
    # empty string
    [
        '',
        '',
        []   
    ],
    # Test case 7
    # reversed tags
    # two variables with a same name
    [
        '><123>><123,456>><123,456,789>><:123:>><:123:>><::::::::::::::::>><[123],[4892]>><>><:%f:>><**>><\t\t>><&t>><%f>><%a>><:test:>>>>>>>>>>>>>><:[123],[4892]:>',  
        '><>><>><>><>><>><>><>><>><>><>><>><>><>><>><>>>>>>>>>>>>>><>',
        [
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '123',                    'id': 0 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '123,456',                'id': 1 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '123,456,789',            'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '123',                    'id': 3 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '123',                    'id': 4 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '::::::::::::::',         'id': 5 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '[123],[4892]',           'id': 6 },
            { 'location': 'endpoint', 'type': 'local_variable',                      'id': 7 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '%f',                     'id': 8 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '**',                     'id': 9 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '\t\t',                   'id': 10 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '&t',                     'id': 11 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '%f',                     'id': 12 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': '%a',                     'id': 13 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': 'test',                   'id': 14 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '[123],[4892]',           'id': 15 },
        ]  
    ]
]

"""
conf.url_enum_start = '<:'
conf.url_enum_end = ':>'
conf.url_variable_start = '<'
conf.url_variable_end = '>'
"""
test_cases_reversed_default = [
    # Test case 0
    [
        'https://mydomain/addUser/<:user:>/<1,2,3>/<:user2:>/<>/<9,8,7>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>', 
        [
            { 'location': 'endpoint', 'type': 'enumerate',   'content': 'user',      'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '1,2,3',     'id': 1 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': 'user2',     'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '',       'id': 3 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '9,8,7',     'id': 4 }
        ]   
    ],
    # Test case 1
    [
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',      'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',      'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',      'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',      'id': 3 },
            { 'location': 'endpoint', 'type': 'global_variable',  'name': '',      'id': 4 }
        ]   
    ],
    # Test case 2
    [
        'https://mydomain/addUser/<:a:>/<:b:>/<:c:>/<:d:>/<:e:>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'a',      'id': 0 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'b',      'id': 1 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'c',      'id': 2 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'd',      'id': 3 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'e',      'id': 4 }
        ]   
    ],
    # Test case 3
    # empty variable element: <::>
    [
        'https://mydomain/addUser/<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'local_variable',                   'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': 'sfnsfsfsjkfns',      'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable',   'name': '--',                 'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable',      'name': '',               'id': 3 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 4
    [
        '<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        '<>/<>/<>/<>/<>',
        [
            { 'location': 'endpoint', 'type': 'local_variable',                 'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable', 'name': 'sfnsfsfsjkfns',      'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable', 'name': '--',                 'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable', 'name': '',                   'id': 3 },
            { 'location': 'endpoint', 'type': 'enumerate',  'content': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 5
    # random characters
    [
        '::::::<><:%$#^&!()*&#:><:\n:><123,456,789,789>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        '::::::<><><><>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        [
            { 'location': 'endpoint', 'type': 'global_variable',       'name': '',                       'id': 0 },
            { 'location': 'endpoint', 'type': 'enumerate',      'content': '%$#^&!()*&#',           'id': 1 },
            { 'location': 'endpoint', 'type': 'enumerate',      'content': '\n',                    'id': 2 },
            { 'location': 'endpoint', 'type': 'global_variable',       'name': '123,456,789,789',       'id': 3 }
        ]   
    ],
    # Test case 6
    # empty string
    [
        '',
        '',
        []   
    ],
    # Test case 7
    # reversed tags
    # two variables with a same name
    [
        '><123>><123,456>><123,456,789>><:123:>><:123:>><::::::::::::::::>><[123],[4892]>><>><:%f:>><**>><\t\t>><&t>><%f>><%a>><:test:>>>>>>>>>>>>>><:[123],[4892]:>',  
        '><>><>><>><>><>><>><>><>><>><>><>><>><>><>><>>>>>>>>>>>>>><>',
        [
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '123',                    'id': 0 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '123,456',                'id': 1 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '123,456,789',            'id': 2 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': '123',                    'id': 3 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': '123',                    'id': 4 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': '::::::::::::::',         'id': 5 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '[123],[4892]',           'id': 6 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '',                       'id': 7 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': '%f',                     'id': 8 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '**',                     'id': 9 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '\t\t',                   'id': 10 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '&t',                     'id': 11 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '%f',                     'id': 12 },
            { 'location': 'endpoint', 'type': 'global_variable',    'name': '%a',                     'id': 13 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': 'test',                   'id': 14 },
            { 'location': 'endpoint', 'type': 'enumerate',   'content': '[123],[4892]',           'id': 15 },
        ]  
    ]
] 

invalid_test_cases = [
    ['<::<>'],
    ['<'],
    ['<:'],
    ['<:>']
]

@pytest.fixture()
def resource():
    """ SETUP """
    # crate a default configuration file
    config_file = '../../config.ini'
    create_default_config(config_file)

    # read the data from configuration file and crate a class out of it 
    global conf
    conf = read_config_file(config_file)
    conf.extend_of_priority_tags()

    # trigger tests
    yield "resource"

    # crate default configuration file
    create_default_config(config_file)


@pytest.mark.parametrize("test_case", test_cases_default)
def test_url_default_tags(test_case, resource):
    # expected
    expected_url = test_case[1]
    expected_params = test_case[2]

    # general_string_parser(content_string, location, param_id_cnt, config):
    # execute
    result = general_string_parser(test_case[0], 'endpoint', 0, conf)

    actual_url = result[0]
    actual_params = result[1]

    # verify    
    assert actual_url == expected_url
    assert len(actual_params) == len(expected_params)
    for idx in range(len(actual_params)):
        assert actual_params[idx] == expected_params[idx]

@pytest.mark.parametrize("test_case", test_cases_reversed_default)
def test_url_reversed_default_values(test_case, resource):
    # change the configuration values
    conf.endpoint.enum.start = '<:'
    conf.endpoint.enum.end = ':>'
    conf.endpoint.variable.start = '<'
    conf.endpoint.variable.end = '>'
    # conf.url_enum_start = '<:'
    # conf.url_enum_end = ':>'
    # conf.url_variable_start = '<'
    # conf.url_variable_end = '>'

    # expected
    expected_url = test_case[1]
    expected_params = test_case[2]

    # execute
    # result = url_parser(test_case[0], conf)
    result = general_string_parser(test_case[0], 'endpoint', 0, conf)
    actual_url = result[0]
    actual_params = result[1]

    # verify    
    assert actual_url == expected_url
    assert len(actual_params) == len(expected_params)
    for idx in range(len(actual_params)):
        assert actual_params[idx] == expected_params[idx]

@pytest.mark.parametrize("test_case", invalid_test_cases)
def test_url_invalid_values(test_case, resource):
    # execute
    with pytest.raises(EndpointSemanticError):
        # result = url_parser(test_case[0], conf)
        result = general_string_parser(test_case[0], 'endpoint', 0, conf)