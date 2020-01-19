//6kyu on CodeWars: https://www.codewars.com/kata/5783ef69202c0ee4cb000265/train/javascript

// JavaScript's indexOf does not work with arrays as input. This is because [1,2] === [1,2] will return false in JavaScript.
// Many other languages have similar quirks.
//
// However, sometimes it is useful to search for an Array. Write a function that looks for an array within a two-dimensional
// array and returns the index of the first matching element. If there is no match, your function should return -1.
//
// See some examples in JavaScript below.
//
//     var arrayToSearch = [[1,2],[3,4],[5,6]];
// var query = [1,2]; // => 0
// query = [5,6]; // => 2
// query = [9,2]; // => -1
// And some examples in C#:
//
// var arrayToSearch = new object[] { new object[] { 1,2 } , new object[] { 3,4 }, new object[] { 5,6 } };
// var query = new object[] { 1,2 }; // => 0
// query = new object[] { 5,6 }; // => 2
// query = new object[] { 9,2 }; // => -1

let searchArray = function (arrayToSearch, query) {
    // There are some conditionals that were not included in the description
    // Must throw error if the to search isn't an array or the query isn't an array pair
    if (!Array.isArray(query) || query.length !== 2) {
        throw 'error';
    } // also needs to throw error if the search isn't done on a two dimensional array
    else if (!Array.isArray(arrayToSearch[0])) {
        throw 'error';
    } // finally, needs to throw error if the array to search has a value that isn't a pair (line 38)
    else {

        console.log(arrayToSearch);
        console.log(query);
//I believe I need to go through each value of the arrayToSearch and compare it with the query
        for (let value in arrayToSearch) {
            if (arrayToSearch[value].length !== 2) {
                throw 'error';
            }
            // since a direct comparison doesn't work, I will need to compare the values for each pair
            else if (arrayToSearch[value][0] === query[0] && arrayToSearch[value][1] === query[1]) {
                // I need to store this answer into a variable
                answer = arrayToSearch[value];
                // console.log(answer);

                // now I can access the desired index so I just need to return the first instance
                // console.log(arrayToSearch.indexOf(answer));
                if (arrayToSearch.indexOf(answer) >= 0) {
                    return arrayToSearch.indexOf(answer);
                }
                // queryIndex.push(arrayToSearch.indexOf(answer));
            }
        }
    }
    // if the array doesn't contain the answer return -1
    return -1;
};

console.log(searchArray([ [ 1, 2 ], [ 3, 4 ], [ 5, 6, 7 ], [ 8, 9 ] ],
    [ 9, 20 ]));

