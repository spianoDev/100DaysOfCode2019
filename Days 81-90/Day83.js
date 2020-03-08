//  5kyu on CodeWars: https://www.codewars.com/kata/513fa1d75e4297ba38000003/train/javascript

//     For this exercise you will create a global flatten method.
//     The method takes in any number of arguments and flattens them into a single array.
//     If any of the arguments passed in are an array then the individual objects within the array will be flattened so
//     that they exist at the same level as the other arguments.
//     Any nested arrays, no matter how deep, should be flattened into the single array result.
//
//     The following are examples of how this function would be used and what the expected results would be:
//
//     flatten(1, [2, 3], 4, 5, [6, [7]]) // returns [1, 2, 3, 4, 5, 6, 7]
//     flatten('a', ['b', 2], 3, null, [[4], ['c']]) // returns ['a', 'b', 2, 3, null, 4, 'c']
function flatten() {
    // variable for the flattened array
    let arr = [];
    // loop through contents of the arguments
    // console.log(arguments);
    for (let i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
        // create an array of all the values
            arr.push(arguments[i]);
        }
    let oneArray = [].concat.apply([], arr);
    for (let j = 0; j < oneArray.length; j++){
        // need to keep applying the concat until the array is one dimensional
        while (Array.isArray(oneArray[j])) {
            oneArray = [].concat.apply([], oneArray);
        }
    }
    console.log(oneArray);
    return oneArray;
}

flatten(1, [2, 3], 4, 5, [6, [7]]); // [1, 2, 3, 4, 5, 6, 7]
// flatten('a', ['b', 2], 3, null, [[4], ['c']]); // returns ['a', 'b', 2, 3, null, 4, 'c']
