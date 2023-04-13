/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    let ans = {};
    for(let i = 0; i < this.length; ++i) {
        let temp = fn(this[i]);
        if(temp in ans)
            ans[temp].push(this[i]);
        else
            ans[temp] = [this[i]];
    }
    return ans;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */