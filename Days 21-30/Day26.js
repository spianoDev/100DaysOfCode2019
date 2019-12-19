// 6kyu on CodeWars: https://www.codewars.com/kata/will-the-present-fit/train/javascript

// Santa's elves are boxing presents, and they need your help! Write a function that takes two arrays of dimensions
// of the present and the box, respectively, and returns a Boolean based on whether or not the present will fit in the box provided.
// The box's walls are one unit thick, so be sure to take that in to account.
//
//     Example:
//
// willFit([10,7,16], [13, 32,10]);  //Returns true, box is bigger than present
// willFit([5, 7, 9], [9, 5, 7]);    //Returns false, present and box are same size
// willFit([17, 22, 10],[5, 5, 10]); //Returns false, box is too small
//
// function willFit(present, box){
//     // I believe all I need to do is multiply each value together and then compare the present to the box making
//     // sure to add 3 to the answer to account for the box needing to be bigger than the present by one cubic unit.
//     let cubicPresent = (present[0] + 1) * (present[1] + 1) * (present[2] + 1);
//     let cubicBox = box[0] * box[1] * box[2];
//     if (cubicPresent >= cubicBox) {
//         return false;
//     } else {
//         return true;
//     }
// }
//
// console.log(willFit([10,7,16], [10,8,17]));

function willFit(present, box){
    // I believe all I need to do is get the cubic area of each rectangle and then compare the present to the box making
    // sure to add 1 unit to each side to account for the box needing to be bigger than the present by one unit.
    let presentSurfaceArea = (2 * (present[0] + 1)) + (2 * (present[1] + 1)) + (2 * (present[2] + 1));
    // // the extra is to account for the wall unit.
    let boxSurfaceArea = (2 * box[0]) + (2 * box[1]) + (2 * box[2]);
    // I also need to compare sorted sides, but there is a bit of a trick when comparing multiple digits to single
    // digits in sort:
    let presentSorted = present.sort((a, b) => a - b);
    let boxSorted = box.sort((a, b) => a - b);
    console.log(presentSurfaceArea);
    console.log(boxSurfaceArea);
    console.log(presentSorted);
    console.log(boxSorted[0]);
    if (presentSurfaceArea > boxSurfaceArea) {
        return false;
    } // Finally, I need to return false if any of the sides of the present are longer than the box side and make
    // sure I add one unit to the present sides to account for the width of the box.
      if ((presentSorted[0] + 1) >= boxSorted[0]) {
        return false;
    } else if ((presentSorted[1] + 1) >= boxSorted[1]) {
        return false;
    } else if ((presentSorted[2] + 1) >= boxSorted[2]) {
        return false;
    } else {
        return true;
    }
}
console.log(willFit([41, 44, 45],[43, 46, 46]));
