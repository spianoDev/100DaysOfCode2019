// 6kyu on CodeWars: https://www.codewars.com/kata/ho-ho-ho-with-functions/train/javascript

// Santa is learning programming. And what could be the first program, he wants to write? Yes, the "Hello world!" of Christmas: "Ho Ho Ho!".
// He wants to write a function ho(), which should have the following return values:
//
// ho(); // should return "Ho!"
// ho(ho()); // should return "Ho Ho!"
// ho(ho(ho())); // should return "Ho Ho Ho!"
// Unfortunately he couldn't find any tutorial, which explains, how he could implement that. Can you help him?
//
// Rules:
//
//     each call of ho() must add a "Ho" to the string
// the "Ho"'s must be separated by a space
// at the end of the string, there must be an exclamation mark (!), without a space

let santaSays = ['Ho'];
function ho() {

    // make a loop that adds the word 'Ho' each time it goes through the function
    for (let i = 0; i > santaSays.length; i++) {
        console.log(santaSays[i]);
        santaSays[i].push(' Ho');
    }
    // if (santaSays.length === 0) {
    //     santaSays.push('Ho!');
    // } else if (santaSays.length >= 1) {
    //     // need a conditional that will add 'Ho ' to the beginning of the array.
    //     santaSays.unshift('Ho ');
    //     console.log(santaSays);
    // }
    // santaSays.splice(1, santaSays.length);
    return santaSays.join('') + '!';
}

console.log(ho());
console.log(ho(ho()));
console.log(ho(ho(ho())));
