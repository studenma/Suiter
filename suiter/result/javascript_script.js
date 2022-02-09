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
    if(test_case == "test_case_01") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_02") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_03") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_04") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=1&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_05") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=1&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_06") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=1&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_07") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=2&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_08") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=2&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_09") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=2&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_10") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=3&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_11") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=3&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_12") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=3&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_13") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_14") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_15") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_16") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_17") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_18") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_19") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=0&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_20") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=0&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_21") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=0&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_22") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_23") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_24") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_25") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=2&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_26") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=2&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_27") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=2&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_28") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=3&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_29") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=3&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_30") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=3&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_31") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=4&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_32") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=4&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_33") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=4&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_34") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_35") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_36") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_37") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=0&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_38") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=0&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_39") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=0&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_40") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=1&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_41") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=1&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_42") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=1&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_43") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_44") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_45") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_46") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=3&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_47") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=3&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_48") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=3&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_49") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=4&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_50") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=4&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_51") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=4&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_52") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=5&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_53") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=5&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_54") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=5&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_55") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=0&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_56") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=0&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_57") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=0&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_58") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=1&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_59") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=1&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_60") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=1&num2=3
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_61") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=2&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_62") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=2&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_63") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=2&num2=2
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_64") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_65") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_66") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_67") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=4&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_68") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=4&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_69") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=4&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_70") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=5&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_71") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=5&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if(test_case == "test_case_72") {
        if(request_id == "call_1") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=5&num2=1
            // method = POST
            // header = {"Content-type": "json"}
            // body = ./body_files/request_1_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else if(request_id == "call_2") {
            // Test Case Information
            // endpoint = http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5
            // method = GET
            // header = {"Content-type": "json"}
            // body = ./body_files/request_2_body_1
            assert.strictEqual(response.statusCode,200);
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else {
        throw new Error("Should have never gotten here: [${test_case},${request_id}]")
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
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_02") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_03") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=0&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_04") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=1&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_05") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=1&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_06") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=1&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_07") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=2&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_08") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=2&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_09") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=2&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_10") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=3&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_11") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=3&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_12") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=3&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_13") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_14") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_15") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_16") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_17") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_18") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=5&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_19") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=0&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_20") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=0&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_21") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=0&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_22") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_23") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_24") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=1&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_25") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=2&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_26") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=2&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_27") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=2&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_28") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=3&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_29") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=3&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_30") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=3&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_31") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=4&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_32") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=4&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_33") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=4&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_34") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_35") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_36") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_37") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=0&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_38") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=0&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_39") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=0&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_40") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=1&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_41") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=1&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_42") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=1&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_43") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_44") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_45") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=2&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_46") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=3&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_47") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=3&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_48") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=3&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_49") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=4&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_50") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=4&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_51") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=4&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_52") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=5&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_53") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=5&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_54") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=5&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_55") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=0&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_56") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=0&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_57") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=0&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=0"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_58") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=1&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_59") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=1&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_60") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=1&num2=3"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=1"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_61") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=2&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_62") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=2&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_63") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=2&num2=2"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=2"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_64") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_65") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_66") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=3&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=3"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_67") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=4&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_68") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=4&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_69") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=4&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=4"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_70") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=5&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=add&num1=4&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_71") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=5&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=substract&num1=5&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else if( test_case == "test_case_72") {
        if(request_id == "call_1") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=divide&num1=5&num2=1"
            method = "POST"
            header = {"Content-type": "json"}
            body = "./body_files/request_1_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else if(request_id == "call_2") {
            url = "http://127.0.0.1:5000/api/v1/calculator?operation=multiply&num1=6&num2=5"
            method = "GET"
            header = {"Content-type": "json"}
            body = "./body_files/request_2_body_1"
            endpoint_params = []
            method_params = []
            header_params = []
            body_params = []
        }
        else {
            throw new Error("Should have never gotten here: [${test_case},${request_id}]")
        }
    }
    else {
        throw new Error("Should have never gotten here: [${test_case},${request_id}]")
    }


    return new ContextClass([url,method,header,body],endpoint_params,method_params,header_params,body_params)
}

describe('AllTestCases', function() {
    it('test_sequence_01', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_01", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_01", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_01", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_01", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_02', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_02", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_02", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_02", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_02", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_03', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_03", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_03", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_03", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_03", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_04', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_04", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_04", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_04", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_04", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_05', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_05", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_05", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_05", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_05", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_06', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_06", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_06", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_06", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_06", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_07', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_07", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_07", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_07", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_07", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_08', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_08", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_08", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_08", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_08", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_09', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_09", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_09", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_09", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_09", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_10', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_10", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_10", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_10", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_10", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_11', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_11", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_11", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_11", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_11", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_12', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_12", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_12", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_12", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_12", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_13', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_13", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_13", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_13", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_13", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_14', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_14", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_14", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_14", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_14", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_15', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_15", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_15", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_15", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_15", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_16', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_16", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_16", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_16", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_16", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_17', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_17", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_17", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_17", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_17", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_18', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_18", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_18", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_18", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_18", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_19', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_19", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_19", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_19", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_19", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_20', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_20", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_20", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_20", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_20", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_21', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_21", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_21", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_21", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_21", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_22', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_22", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_22", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_22", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_22", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_23', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_23", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_23", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_23", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_23", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_24', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_24", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_24", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_24", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_24", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_25', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_25", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_25", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_25", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_25", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_26', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_26", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_26", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_26", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_26", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_27', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_27", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_27", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_27", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_27", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_28', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_28", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_28", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_28", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_28", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_29', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_29", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_29", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_29", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_29", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_30', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_30", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_30", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_30", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_30", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_31', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_31", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_31", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_31", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_31", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_32', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_32", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_32", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_32", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_32", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_33', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_33", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_33", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_33", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_33", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_34', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_34", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_34", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_34", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_34", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_35', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_35", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_35", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_35", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_35", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_36', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_36", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_36", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_36", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_36", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_37', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_37", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_37", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_37", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_37", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_38', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_38", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_38", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_38", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_38", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_39', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_39", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_39", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_39", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_39", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_40', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_40", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_40", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_40", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_40", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_41', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_41", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_41", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_41", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_41", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_42', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_42", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_42", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_42", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_42", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_43', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_43", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_43", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_43", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_43", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_44', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_44", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_44", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_44", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_44", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_45', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_45", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_45", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_45", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_45", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_46', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_46", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_46", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_46", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_46", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_47', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_47", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_47", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_47", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_47", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_48', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_48", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_48", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_48", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_48", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_49', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_49", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_49", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_49", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_49", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_50', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_50", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_50", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_50", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_50", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_51', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_51", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_51", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_51", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_51", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_52', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_52", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_52", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_52", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_52", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_53', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_53", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_53", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_53", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_53", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_54', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_54", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_54", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_54", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_54", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_55', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_55", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_55", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_55", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_55", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_56', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_56", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_56", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_56", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_56", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_57', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_57", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_57", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_57", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_57", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_58', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_58", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_58", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_58", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_58", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_59', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_59", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_59", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_59", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_59", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_60', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_60", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_60", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_60", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_60", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_61', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_61", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_61", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_61", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_61", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_62', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_62", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_62", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_62", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_62", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_63', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_63", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_63", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_63", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_63", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_64', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_64", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_64", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_64", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_64", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_65', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_65", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_65", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_65", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_65", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_66', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_66", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_66", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_66", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_66", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_67', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_67", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_67", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_67", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_67", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_68', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_68", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_68", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_68", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_68", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_69', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_69", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_69", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_69", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_69", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_70', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_70", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_70", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_70", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_70", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_71', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_71", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_71", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_71", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_71", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });

    it('test_sequence_72', function() {
        // SUT setup
        setup();
        // 1. request
        req = all_test_cases("test_case_72", "call_1");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_72", "call_1", response, req);
        });
        // 2. request
        req = all_test_cases("test_case_72", "call_2");
        var options = {
        	'url': req.endpoint,
        	'method': req.method,
        	'headers': req.header
        }
        request(options, function (error, response) {
        	if (error) throw new Error(error);
        	verify("test_case_72", "call_2", response, req);
        });
        // SUT Teardown 
        teardown();
    });


});