import pytest
import configparser

""" import suiter package """ 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from suiter_input_parser import url_parser
from input_configuration import create_default_config
from input_configuration import read_config_file
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
            { 'type': 'variable',   'content': 'user',      'id': 0 },
            { 'type': 'enumerate',  'content': '1,2,3',     'id': 1 },
            { 'type': 'variable',   'content': 'user2',     'id': 2 },
            { 'type': 'enumerate',  'content': '',          'id': 3 },
            { 'type': 'enumerate',  'content': '9,8,7',     'id': 4 }
        ]   
    ],
    # Test case 1
    [
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'type': 'enumerate',  'content': '',      'id': 0 },
            { 'type': 'enumerate',  'content': '',      'id': 1 },
            { 'type': 'enumerate',  'content': '',      'id': 2 },
            { 'type': 'enumerate',  'content': '',      'id': 3 },
            { 'type': 'enumerate',  'content': '',      'id': 4 }
        ]   
    ],
    # Test case 2
    [
        'https://mydomain/addUser/<:a:>/<:b:>/<:c:>/<:d:>/<:e:>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'type': 'variable',  'content': 'a',      'id': 0 },
            { 'type': 'variable',  'content': 'b',      'id': 1 },
            { 'type': 'variable',  'content': 'c',      'id': 2 },
            { 'type': 'variable',  'content': 'd',      'id': 3 },
            { 'type': 'variable',  'content': 'e',      'id': 4 }
        ]   
    ],
    # Test case 3
    # empty variable element: <::>
    [
        'https://mydomain/addUser/<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        [
            { 'type': 'variable',  'content': '',                   'id': 0 },
            { 'type': 'enumerate', 'content': 'sfnsfsfsjkfns',      'id': 1 },
            { 'type': 'enumerate', 'content': '--',                 'id': 2 },
            { 'type': 'enumerate', 'content': '',                   'id': 3 },
            { 'type': 'variable',  'content': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 4
    [
        '<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        '<>/<>/<>/<>/<>',
        [
            { 'type': 'variable',  'content': '',                   'id': 0 },
            { 'type': 'enumerate', 'content': 'sfnsfsfsjkfns',      'id': 1 },
            { 'type': 'enumerate', 'content': '--',                 'id': 2 },
            { 'type': 'enumerate', 'content': '',                   'id': 3 },
            { 'type': 'variable',  'content': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 5
    # random characters
    [
        '::::::<><:%$#^&!()*&#:><:\n:><123,456,789,789>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        '::::::<><><><>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        [
            { 'type': 'enumerate',  'content': '',                       'id': 0 },
            { 'type': 'variable',   'content': '%$#^&!()*&#',           'id': 1 },
            { 'type': 'variable',   'content': '\n',                    'id': 2 },
            { 'type': 'enumerate',  'content': '123,456,789,789',       'id': 3 }
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
            { 'type': 'enumerate',  'content': '123',                    'id': 0 },
            { 'type': 'enumerate',  'content': '123,456',                'id': 1 },
            { 'type': 'enumerate',  'content': '123,456,789',            'id': 2 },
            { 'type': 'variable',   'content': '123',                    'id': 3 },
            { 'type': 'variable',   'content': '123',                    'id': 4 },
            { 'type': 'variable',   'content': '::::::::::::::',         'id': 5 },
            { 'type': 'enumerate',  'content': '[123],[4892]',           'id': 6 },
            { 'type': 'enumerate',  'content': '',                       'id': 7 },
            { 'type': 'variable',   'content': '%f',                     'id': 8 },
            { 'type': 'enumerate',  'content': '**',                     'id': 9 },
            { 'type': 'enumerate',  'content': '\t\t',                   'id': 10 },
            { 'type': 'enumerate',  'content': '&t',                     'id': 11 },
            { 'type': 'enumerate',  'content': '%f',                     'id': 12 },
            { 'type': 'enumerate',  'content': '%a',                     'id': 13 },
            { 'type': 'variable',   'content': 'test',                   'id': 14 },
            { 'type': 'variable',   'content': '[123],[4892]',           'id': 15 },
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
        'https://mydomain/addUser/<::>/<::>/<::>/<::>/<::>', 
        [
            { 'type': 'enumerate',   'content': 'user',      'id': 0 },
            { 'type': 'variable',    'content': '1,2,3',     'id': 1 },
            { 'type': 'enumerate',   'content': 'user2',     'id': 2 },
            { 'type': 'variable',    'content': '',          'id': 3 },
            { 'type': 'variable',    'content': '9,8,7',     'id': 4 }
        ]   
    ],
    # Test case 1
    [
        'https://mydomain/addUser/<>/<>/<>/<>/<>',
        'https://mydomain/addUser/<::>/<::>/<::>/<::>/<::>',
        [
            { 'type': 'variable',  'content': '',      'id': 0 },
            { 'type': 'variable',  'content': '',      'id': 1 },
            { 'type': 'variable',  'content': '',      'id': 2 },
            { 'type': 'variable',  'content': '',      'id': 3 },
            { 'type': 'variable',  'content': '',      'id': 4 }
        ]   
    ],
    # Test case 2
    [
        'https://mydomain/addUser/<:a:>/<:b:>/<:c:>/<:d:>/<:e:>',
        'https://mydomain/addUser/<::>/<::>/<::>/<::>/<::>',
        [
            { 'type': 'enumerate',  'content': 'a',      'id': 0 },
            { 'type': 'enumerate',  'content': 'b',      'id': 1 },
            { 'type': 'enumerate',  'content': 'c',      'id': 2 },
            { 'type': 'enumerate',  'content': 'd',      'id': 3 },
            { 'type': 'enumerate',  'content': 'e',      'id': 4 }
        ]   
    ],
    # Test case 3
    # empty variable element: <::>
    [
        'https://mydomain/addUser/<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        'https://mydomain/addUser/<::>/<::>/<::>/<::>/<::>',
        [
            { 'type': 'enumerate',  'content': '',                   'id': 0 },
            { 'type': 'variable',   'content': 'sfnsfsfsjkfns',      'id': 1 },
            { 'type': 'variable',   'content': '--',                 'id': 2 },
            { 'type': 'variable',   'content': '',                   'id': 3 },
            { 'type': 'enumerate',  'content': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 4
    [
        '<::>/<sfnsfsfsjkfns>/<-->/<>/<:e:>',
        '<::>/<::>/<::>/<::>/<::>',
        [
            { 'type': 'enumerate',  'content': '',                   'id': 0 },
            { 'type': 'variable', 'content': 'sfnsfsfsjkfns',      'id': 1 },
            { 'type': 'variable', 'content': '--',                 'id': 2 },
            { 'type': 'variable', 'content': '',                   'id': 3 },
            { 'type': 'enumerate',  'content': 'e',                  'id': 4 }
        ]   
    ],
    # Test case 5
    # random characters
    [
        '::::::<><:%$#^&!()*&#:><:\n:><123,456,789,789>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        '::::::<::><::><::><::>////////*/*-///+-(*$#^@!)!_~5~!@@#$$%%^&&**(())',
        [
            { 'type': 'variable',       'content': '',                       'id': 0 },
            { 'type': 'enumerate',      'content': '%$#^&!()*&#',           'id': 1 },
            { 'type': 'enumerate',      'content': '\n',                    'id': 2 },
            { 'type': 'variable',       'content': '123,456,789,789',       'id': 3 }
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
        '><::>><::>><::>><::>><::>><::>><::>><::>><::>><::>><::>><::>><::>><::>><::>>>>>>>>>>>>>><::>',
        [
            { 'type': 'variable',    'content': '123',                    'id': 0 },
            { 'type': 'variable',    'content': '123,456',                'id': 1 },
            { 'type': 'variable',    'content': '123,456,789',            'id': 2 },
            { 'type': 'enumerate',   'content': '123',                    'id': 3 },
            { 'type': 'enumerate',   'content': '123',                    'id': 4 },
            { 'type': 'enumerate',   'content': '::::::::::::::',         'id': 5 },
            { 'type': 'variable',    'content': '[123],[4892]',           'id': 6 },
            { 'type': 'variable',    'content': '',                       'id': 7 },
            { 'type': 'enumerate',   'content': '%f',                     'id': 8 },
            { 'type': 'variable',    'content': '**',                     'id': 9 },
            { 'type': 'variable',    'content': '\t\t',                   'id': 10 },
            { 'type': 'variable',    'content': '&t',                     'id': 11 },
            { 'type': 'variable',    'content': '%f',                     'id': 12 },
            { 'type': 'variable',    'content': '%a',                     'id': 13 },
            { 'type': 'enumerate',   'content': 'test',                   'id': 14 },
            { 'type': 'enumerate',   'content': '[123],[4892]',           'id': 15 },
        ]  
    ]
] 

invalid_test_cases = [
    ['><<123>><<123,456>><<123,456,789>><<:123:>><<:123:>><<::::::::::::::::>><<[123],[4892]>><<>><<a>><<**>><<\t\t>><<&t>><<%f>><<%a>><:test:>>>>>>>>>>>>>>'],
    ['<<>>'],
    ['<::<>'],
    ['<:<:>'],
    ['>>>>>>>>>>><<<<<<<<<<<<<<<<>>'],
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

    # trigger tests
    yield "resource"

    # crate default configuration file
    create_default_config(config_file)


@pytest.mark.parametrize("test_case", test_cases_default)
def test_url_default_tags(test_case, resource):
    # expected
    expected_url = test_case[1]
    expected_params = test_case[2]

    # execute
    result = url_parser(test_case[0], conf)
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
    conf.url_enum_start = '<:'
    conf.url_enum_end = ':>'
    conf.url_variable_start = '<'
    conf.url_variable_end = '>'

    # expected
    expected_url = test_case[1]
    expected_params = test_case[2]

    # execute
    result = url_parser(test_case[0], conf)
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
        result = url_parser(test_case[0], conf)