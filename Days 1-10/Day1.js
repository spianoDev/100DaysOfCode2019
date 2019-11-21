// For my first challenge I picked an algorithm from the easiest level: 8kyu on CodeWars.

//Return the Nth Even Number
//
// nthEven(1) //=> 0, the first even number is 0
// nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)
//
// nthEven(100) //=> 198
// nthEven(1298734) //=> 2597466
// The input will not be 0.

// function nthEven(n){
//     let evenNumber = n * 2;
//     //create a loop that will iterate through the provided number of even returns
//     for (let i = 0; i < evenNumber; i+=2) {
//         // the console of i returns the desired answer in the final console return
//         console.log([i]);
//         let answer = evenNumber - 2;
//         // to get to the desired answer, I then needed to take the evenNumber and subtract 2 to get the same result
//         // this makes the loop unnecessary.
//         console.log(answer);
//         return answer;
//     }
//
// }
//
// nthEven(5);

// refactored answer:
function nthEven(n){
    let answer = (n * 2) - 2;
    return answer;
}
nthEven(6);
console.log(nthEven(6));
