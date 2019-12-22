// 7kyu on CodeWars: https://www.codewars.com/kata/naughty-or-nice/train/javascript

// Happy Holidays fellow Code Warriors!
//     It's almost Christmas! That means Santa's making his list, and checking it twice.
//     Unfortunately, Santa's Javascript and CoffeeScript Elves accidentally mixed the Naughty and Nice list together! Santa needs your help to save Christmas!
//
// Save Christmas!
//     Santa needs you to write two functions, getNiceNames and getNaughtyNames.
//     Both of the functions accept an array of objects. getNiceNames returns an array containing only the names of the nice people,
//     and getNaughtyNames returns an array containing only the names of the naughty people.
//     Return an empty array [] if the result from either of the functions contains no names.
//
//     The objects in the passed in array will represent people. Each object contains two properties: name and wasNice.
//     name - The name of the person
//     wasNice - True if the person was nice this year, false if they were naughty
//
// Person Object Examples
// JavaScript
// { name: 'Warrior reading this kata', wasNice: true }
// { name: 'xDranik', wasNice: false }

// initially I made the arrays global but then each test would add the names so I had to move them inside the
// individual functions to pass the tests.
function getNiceNames(people) {
    let niceList = [];
    // loops through all the people
    for (let i = 0; i < people.length; i++) {
        // conditional accessing only those people who were 'nice'
        if (people[i].wasNice === true) {
            // console.log(people[i].name);
            // add the nice people to the nice list
            niceList.push(people[i].name);
        }
            }
    return niceList;
}
function getNaughtyNames(people){
    let naughtyList = [];
    //basically I'm going to repeat the process with the naughty names
    for (let i = 0; i < people.length; i++) {
        // conditional accessing only those people who were 'naughty'
        if (people[i].wasNice === false) {
            // console.log(people[i].name);
            // add the nice people to the naughty list
            naughtyList.push(people[i].name);
        }
    }
    return naughtyList;
}

let peopleObjects = [{ name: 'Warrior reading this kata', wasNice: true },
    { name: 'xDranik', wasNice: false },  {name: 'Santa', wasNice: true},  {name: 'Satan', wasNice: false},];

console.log(getNiceNames(peopleObjects));
console.log(getNaughtyNames(peopleObjects));
