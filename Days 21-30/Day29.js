// 6kyu on CodeWars:  https://www.codewars.com/kata/santas-master-plan/train/javascript

// Happy Holidays fellow Code Warriors!
//     Santa has just revealed his master plan! His goal was to automate as many of his tasks as possible by posting them as challenges in the #hackingholidays section of Codewars. Thanks to the solutions from these challenges, Santa has completed his tasks a week before Christmas! You know what that means...Party at Santa's place! All that's left is to invite everyone. Santa sent out a large amount of invitations, and is patiently waiting for responses.
//
//                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Who's attending the Party?
// Write a function called getAttendees that takes two arguments:
//
//     Array containing all the names of the people Santa invited
// An array of responses (objects) with the following structure:
// {name: 'Easter Bunny', response: 'declined'}
// getAttendees should return an array containing the names of all the people who accepted Santa's invitation and the names of those who did not respond to the invitation.
// Santa is very positive, so he is assuming those who did not respond will show up. Anyone who declined the invitation will not be attending the party.
// If nobody is attending the party, return an empty array [].
//
// Example:
//     Javascript/CoffeeScript:
//
// getAttendees( ['Easter Bunny', 'Tooth Fairy', 'Frosty the Snowman', 'Jack Frost'] ,
//     [
//         {name: 'Easter Bunny', response: 'declined'},
//         {name: 'Jack Frost', response: 'declined'},
//         {name: 'Tooth Fairy', response: 'accepted'}
//     ] );// => returns ['Tooth Fairy', 'Frosty the Snowman']

// trying a new tactic since I realized none of my slice pieces were working.
function getAttendees(people, responses) {
    //I need an internal array to add the people coming based on responses.
    let peopleList = [];
    let peopleComing = [];
    for (let j = 0; j < people.length; j++) {
        for (let k = 0; k < responses.length; k++) {
            if (people[j] === responses[k].name) {
                people.splice(j, 1);
            }
        }
    }
    console.log(people);
    // next I will determine who is coming based on the responses
    for (let i = 0; i < responses.length; i++) {
        if (responses[i].response === 'accepted') {
            peopleList.push(responses[i].name);
        }
        // console.log('peeps saying they are coming: ' + peopleComing);
    }
    // I was struggling with this so I looked up a possible solution: https://www.tutorialrepublic.com/faq/how-to-remove-duplicate-values-from-a-javascript-array.php
    function getUnique(array){
        let uniqueArray = [];
        // Loop through array values
        for(let value of array){
            if(uniqueArray.indexOf(value) === -1){
                uniqueArray.push(value);
            }
        }
        return uniqueArray;
    }
    console.log(peopleList);
    // finally return the complete list of attendees
    peopleComing = peopleList.concat(people);
    // But, there might be some repeats so
    return getUnique(peopleComing);
}


let people = ['Easter Bunny', 'Tooth Fairy', 'Frosty the Snowman',
    'Jack Frost', 'Cupid', 'Father Time'];
let responses = [
    {name: 'Easter Bunny', response: 'declined'},
    {name: 'Jack Frost', response: 'declined'},
    {name: 'Tooth Fairy', response: 'accepted'}
];

getAttendees(people, responses);
