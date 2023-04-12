/**
 * @param {Function} fn
 */
function memoize(fn) {
    const memos = {};
    return function(...args) {
        if(!(args in memos))
            memos[args] = fn(...args);
        return memos[args];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */