# from unittest import TestCase
import pytest

""" import suiter package """ 
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from input_parser import url_parser

"""
Valid test cases
"""
test_cases = [
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

invalid_test_cases = [
    ['><<123>><<123,456>><<123,456,789>><<:123:>><<:123:>><<::::::::::::::::>><<[123],[4892]>><<>><<a>><<**>><<\t\t>><<&t>><<%f>><<%a>><:test:>>>>>>>>>>>>>>']
]

@pytest.mark.parametrize("test_case", test_cases)
def test_url_default_tags(test_case):
    # # change the configuration
    # URL_PARAM_ENUM_START_TAG='<'
    # URL_PARAM_ENUM_END_TAG='>'
    # URL_PARAM_ENUM_SEPARATOR=','
    # URL_PARAM_VARIABLE_START_TAG='<:'
    # URL_PARAM_VARAIBLE_END_TAG=':>'

    # expected
    expected_url = test_case[1]
    expected_params = test_case[2]

    # execute
    result = url_parser(test_case[0])
    actual_url = result[0]
    actual_params = result[1]

    # verify    
    assert actual_url == expected_url
    assert len(actual_params) == len(expected_params)
    for idx in range(len(actual_params)):
        assert actual_params[idx] == expected_params[idx]
