//6kyu on CodeWars: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/javascript

// The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
// Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
//
//     Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
//
//     Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?
//
//     Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
//
//     Examples:
// tickets([25, 25, 50]) // => YES
// tickets([25, 100]) // => NO. Vasya will not have enough money to give change to 100 dollars
// tickets([25, 25, 50, 50, 100]) // => NO. Vasya will not have the right bills to give 75 dollars of change (you can't make two bills of 25 from one of 50)

function tickets(peopleInLine) {
    // I decided to keep track of the two smaller bill types collected
    let twentyFives = 0;
    let fifties = 0;
    for (let i = 0; i < peopleInLine.length; i++){
        if (peopleInLine[i] === 25) {
            twentyFives += 1;
        } else if (peopleInLine[i] === 50 && twentyFives >= 1) {
            fifties += 1;
            twentyFives -= 1;
            // need two conditionals for changing $100
        } else if (peopleInLine[i] === 100 && fifties >= 1 && twentyFives >= 1) {
                fifties -= 1;
                twentyFives -= 1;
        } else if (peopleInLine[i] === 100 && fifties <= 0 && twentyFives >= 3) {
                twentyFives -= 3;
        } else {
            return 'NO';
        }
        console.log(peopleInLine[i]);
        console.log(twentyFives);
        console.log(fifties);
    }
    // then it is a simple comparison to see if the result is zero/positive or negative
    if (twentyFives >= 0) {
        return 'YES';
    } else {
        return 'NO';
    }
}
console.log(tickets([25,25,50,100,25,25,25,100,25,25,25,100 ]));

