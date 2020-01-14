//6kyu on CodeWars: https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/javascript

// You've just discovered a square (NxN) field and you notice a warning sign.
// The sign states that there's a single bomb in the 2D grid-like field in front of you.
//
// Write a function mineLocation/MineLocation that accepts a 2D array, and returns the location of the mine.
// The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s.
//
// The location returned should be an array (Tuple<int, int> in C#) where the first element is the row index,
// and the second element is the column index of the bomb location (both should be 0 based).
// All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.
//
//     Examples:
// mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] ) => returns [0, 0]
// mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] ) => returns [1, 1]
// mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] ) => returns [2, 1]

function mineLocation(field){
    let mineLocation = [];
    let secondPlace;
    // I think the best way to do this is to compare values using a double loop to search the arrays
    for (let i = 0; i < field.length; i++) {
        // This tells me the second position of the mine
        secondPlace = field[i].indexOf(1);
        // I know the value that isn't -1 will contain the mine
        if (secondPlace >= 0) {
            console.log(i);
            mineLocation.unshift(i);
        }
           // console.log(secondPlace)
         if (secondPlace !== -1) {
             mineLocation.push(secondPlace);
        //     // console.log(mineLocation);
         }
    }

     console.log(mineLocation);
        return mineLocation;
}

mineLocation([[0, 0, 0], [0, 0, 1], [0, 0, 0] ]);
