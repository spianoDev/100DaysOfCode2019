// 7kyu on CodeWars: https://www.codewars.com/kata/sort-santas-reindeer/train/javascript

// Happy Holidays fellow Code Warriors!
//     Now, Dasher! Now, Dancer! Now, Prancer, and Vixen! On, Comet! On, Cupid! On, Donder and Blitzen! That's the order Santa wanted his reindeer...right? What do you mean he wants them in order by their last names!? Looks like we need your help Code Warrior!
//
// Sort Santa's Reindeer
// Write a function called sortReindeer (sort_reindeer in Ruby) that accepts an array of Reindeer names, and returns an array with the Reindeer names sorted by their last names.
//
//     ###Examples
//
// sortReindeer([
//     "Dasher Tonoyan",
//     "Dancer Moore",
//     "Prancer Chua",
//     "Vixen Hall",
//     "Comet Karavani",
//     "Cupid Foroutan",
//     "Donder Jonker",
//     "Blitzen Claus"
// ])
// => returns
//
//     [
//     "Prancer Chua",
//         "Blitzen Claus",
//         "Cupid Foroutan",
//         "Vixen Hall",
//         "Donder Jonker",
//         "Comet Karavani",
//         "Dancer Moore",
//         "Dasher Tonoyan",
//     ]

// first we need to create a compare function
// to change how sorting works.
// function sortReindeer(reindeerNames){
//     let alphaOrderLastName = [];
//     let answer = [];
//     // I think I want to split the names but I need to loop through the values of the array
//     for (let i = 0; i < reindeerNames.length; i++) {
//         let individualReindeer = reindeerNames[i];
//         // now I want the index number of the space so I can sort by the character that comes AFTER the space
//         let spaceIndex = individualReindeer.lastIndexOf(' ');
//         // console.log(spaceIndex);
//         let lastNames = individualReindeer.substring(spaceIndex + 1);
//         alphaOrderLastName.push(lastNames);
//         alphaOrderLastName = alphaOrderLastName.sort();
//         // console.log(alphaOrderLastName[7]);
//         // Now i have a sorted list of last names, but I need to compare this with the original list to return the
//         // sorted answer.
//         // Ok so if I take the last entry and add them in reverse order I should get the results I'm looking for.
//         for (let j = 7; j >= 0; j--) {
//             if (alphaOrderLastName[j] > lastNames) {
//                 answer.unshift(individualReindeer);
//                 alphaOrderLastName.pop();
//             } else if (alphaOrderLastName[j] <= lastNames) {
//                 answer.push(individualReindeer);
//                 alphaOrderLastName.pop();
//             }
//             console.log(answer);
//         }
//     }
// }
// This original idea wasn't working at all so I found a resource to help me:
// http://hubrik.com/2015/11/16/sort-by-last-name-with-javascript/


// Get two names to compare (a and b)
function compare (a,b) {

    //split the names as strings into arrays
    let aName = a.split(" ");
    let bName = b.split(" ");

    // get the last names by selecting
    // the last element in the name arrays
    // using array.length - 1 since full names
    // may also have a middle name or initial
    let aLastName = aName[aName.length - 1];
    let bLastName = bName[bName.length - 1];

    // compare the names and return either
    // a negative number, positive number
    // or zero.
    if (aLastName < bLastName) return -1;
    if (aLastName > bLastName) return 1;
    return 0;
}

let answer = [];
function sortReindeer(reindeerNames){
    answer = reindeerNames.sort(compare);
    console.log(answer);
    return answer;
}
sortReindeer([
    "Dasher Tonoyan",
    "Dancer Moore",
    "Prancer Chua",
    "Vixen Hall",
    "Comet Karavani",
    "Cupid Foroutan",
    "Donder Jonker",
    "Blitzen Claus"
]);
