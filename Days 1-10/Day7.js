// 7kyu on CodeWars: https://www.codewars.com/kata/square-every-digit/train/javascript

// Welcome. In this kata, you are asked to square every digit of a number.
//
// For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
//
// Note: The function accepts an integer and returns an integer

function squareDigits(num){
    //first I need to split the number into pieces so I can manipulate each piece. To do that I will make the number
    // a string and then split that string into an array by digit.
    let numberSplit = num.toString().split('');
    console.log(numberSplit);
    // now I will loop through the array and square each digit. So I will make a new array that will hold these values.
    let squaredNumber = [];
    for (let i = 0; i < numberSplit.length; i++) {
        squaredNumber.push(numberSplit[i] * numberSplit[i]);
    }
    console.log(squaredNumber);
    // the final step is putting the number back together again and returning a number again instead of a string.
    let answer = Number(squaredNumber.join(''));
    console.log(answer);
    return answer;
}
squareDigits(9119);
