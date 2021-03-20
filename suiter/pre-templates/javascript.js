var assert = require('assert');

function myFunction(p1, p2) {
    return p1 * p2;   // The function returns the product of p1 and p2
  }

describe('Test', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
        myFunction(1,2);
        assert.equal([1, 2, 3].indexOf(4), -1);
    });
  });
});
