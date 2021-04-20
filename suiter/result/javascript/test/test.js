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
    void(0);
}

function verify(test_case, request_id, response, context) {
    /*
    Method to describe the expected values for all test cases
    Take into account that these if-else statements will be duplicated for all test cases
    You can also rewrite whole method from scretch and use [TODO:] argument while calling 
    suiter to avoid code duplicate     
    */
    if(test_case == "test_case_01") {
        if(request_id == "call_1") {
            /*
            # Test Case Information
            # endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0
            # method = GET
            # header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"}
            # body = ./body_files/request_1_body_1
            */
            assert.strictEqual(response.statusCode,200);
            console.log(context)
        }
        else {
            throw 'This case does not exist'
        }
    }
    else {
        throw 'This case does not exist'
    }
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

    if(test_case == "test_case_01") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=0";
            method = "GET";
            header = {"Content-type": "json", "testInt": "12", "dalsiTest": "test"};
            body = "./body_files/request_1_body_1";
            requestt = [url, method, header, body];
            // parameters
            endpoint_params = ["add", "0", "0"]
            method_params = []
            header_params = ["json", "12"]
            body_params = ['"ID": "SGML"']

            test_case_context = new ContextClass(requestt,endpoint_params,method_params,header_params,body_params)
        }
        else {
            throw new Error('This case does not exist')
        }
    }
    else {
        throw new Error('This case does not exist')
    } 
    return test_case_context
}

describe('AllTestCases', function() {
    it('test_sequence_01', function() {
        // SUT setup
        setup()
        // 1. request
        req = all_test_cases("test_case_01", "call_1")
        var options = {
            'url': req.endpoint,
            'method': req.method,
            'headers': req.header
        };
        request(options, function (error, response) {
            if (error) throw new Error(error);
            verify("test_case_01", "call_1", response, req)
        }); 
        teardown()
    });
});
