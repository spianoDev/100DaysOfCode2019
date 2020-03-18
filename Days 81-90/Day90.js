// 6kyu on CodeWars: https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9/train/javascript

// Sort the given strings in alphabetical order, case insensitive. For example:
//
//     ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
//         ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

sortme = function(names){
    // variable to hold the lowercase first letter of each word
    let lowerLetters = [];
    for (let word of names) {
        lowerLetters.push(word[0].toLowerCase());
    }
    console.log(lowerLetters);
    // sort the lower
    let sortedFirsts = lowerLetters.sort();
    console.log(sortedFirsts);
    // now compare the first letter to the first letter of the original array to reorder
    let finalOrder = [];
    for (let i = 0; i < lowerLetters.length; i++) {
        for (let firstLetter of names) {
            // console.log(firstLetter[0]);
            if (lowerLetters[i] === firstLetter[0].toLowerCase()) {
                finalOrder.push(firstLetter);
            }
                }
    }
    console.log(finalOrder);
    return finalOrder;
};

// sortme(["Hello", "there", "I'm", "fine"]);
sortme(["C", "d", "a", "B"]);

// I'm sure there is a more elegant way to do this, but if it works...
