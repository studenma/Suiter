var assert = require('assert');
var request = require('request');

class ContextClass {
    constructor(req, endpoint_params, method_params, header_params, body_params) {
        this.endpoint = req[0];
        this.method = req[1];
        this.header = req[2];
        this.body = req[3];
        // parameters
        this.endpoint_params = endpoint_params;
        this.method_params = method_params;
        this.header_params = header_params
        this.body_params = body_params
    }
}

function setup() {
    /*#####################################
    # TODO: HERE IS YOUR CODE
    # Insert your code to define prerequisities of SUT*/
    void(0);
}

function verify(test_case, request_id, response, context) {
    /*
    Method to describe the expected values for all test cases
    Take into account that these if-else statements will be duplicated for all test cases
    You can also rewrite whole method from scretch and use [TODO:] argument while calling 
    suiter to avoid code duplicate     
    */
    // DO NOT TOUCH THIS <DUPLICATE>
<VERIFY> 
    // DO NOT TOUCH THIS </DUPLICATE>
}

function teardown() {
    // #####################################
    // # TODO: HERE IS YOUR CODE
    // # Write a code to set the SUT to it's original state
    // # if it is dependend on given test_case, add a 'test_case' parameter to this function
    // # and write a code for all test_cases
    void(0);
}

function all_test_cases(test_case, request_id) {
    /*
    List of all test cases in this test suite
    */
    var url, method, header, body;
    var endpoint_params, method_params, header_params, body_params

    // DO NOT TOUCH THIS <DUPLICATE>
<TEST_CASE_LIST>
    // DO NOT TOUCH THIS </DUPLICATE>

    return new ContextClass([url,method,header,body],endpoint_params,method_params,header_params,body_params)
}

describe('AllTestCases', function() {
<TEST_SEQUENCE>
});