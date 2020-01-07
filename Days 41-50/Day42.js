//  6kyu on CodeWars: https://www.codewars.com/kata/snakes-on-a-plane-number-1-easy/train/javascript

// Did you ever see the movie called Snakes on a Plane?
// It starred Samuel L. Jackson as the hero and had a complicated plot with (SPOILER) snakes that were (SPOILER) on a plane.
// In this Kata there are also snakes on a plane but now YOU can be the hero.
//
//     Task
// Count how many snakes are on the plane
//
// If you are correct  everybody lives!
//
//     If you fail,  we all die!
//
//     No pressure!
//
//     Start counting NOW...
//
// 1.. 2.. 3.. 4.. hang on didn't you count that one twice? 1.. 2.. dammit stop wriggling
//
// Notes:
//
//     snakeskins are uniquely patterned with a single character per snake
// snakes can be any length

function snakesOn(aPlane) {
    let snakes = [];
    // first I want to access the individual arrays inside the larger plane array
    for (let char in aPlane) {
        let snakeArrays = aPlane[char];
        // console.log(aPlane[char]);
        // next I will loop through the individual array and check for characters.
        for (let letters in snakeArrays) {
            // console.log(snakeArrays[letters]);
            // now I will iterate over these snakeArrays looking for characters that are letters
            // but first I need to narrow down the field.
            if (snakeArrays[letters] === '_') {
                delete snakeArrays[letters][0];
            }
            else {
                // this will add all letters to an array
                snakes.push(snakeArrays[letters]);
            }
        }
    }
    // now I can compare the letters in the snakes array and count the number of unique characters present
    let totalSnakes = 0;
    let uniqueSnakes = snakes.sort();
    for (let i = 0; i < snakes.length; i++) {
        // since the sorted list will group all duplicates together, now we can count the characters that are different
        if (uniqueSnakes[i] !== snakes[i + 1]) {
            totalSnakes += 1;
        }
    }
    console.log(totalSnakes);
    return totalSnakes;
}


snakesOn([
    '__AAAAA__A'.split(''),
    '__A___A__A'.split(''),
    'K_____AAAA'.split(''),
    'K_DDDD____'.split(''),
    'K____DDDD_'.split('')
]);
