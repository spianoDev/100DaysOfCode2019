//  7kyu on CodeWars: https://www.codewars.com/kata/only-one-gift-per-child/train/javascript

// Santa is handing out gifts in the kindergarten. Many toddlers are around there and everyone should have the opportunity to have a seat on Santa's lap. But there's Peter, a 5 year old boy, who is a bit naughty. He tries to get two gifts. After he got the first one, he lines up again in the queue of children.
//
//     But fortunately Santa is not alone. His elves keep a list with the names of the children, which already were on Santa's lap. We know, that each child name is unique. If a child tries to get a second gift, the elves will tell Santa.
//
// OK, let's help Santa and his elves with a simple function handOutGift() (hand_out_gift in Ruby, HandOutGift in C# ) which takes the name of the next child. If this child already got a gift, it must throw an error in order to remind Santa.
//
// Example:
//
//     handOutGift("Peter");
// handOutGift("Alison");
// handOutGift("John");
// handOutGift("Maria");
// handOutGift("Peter"); // <-- must throw an error

let children = [];
function handOutGift(name) {
    // I think the easiest way to do this is to collect the names in an array and test them to see if there are any
    // duplicates.
    // the loop will iterate through the array to check for duplicate names.
    for (let i = 0; i < children.length; i++) {
        console.log(children[i]);
        if (children[i] === name) {
            throw "error"
        }
    }
    // this will add the name to an array only if it isn't a duplicate
    children.push(name);
    console.log(children);
}
handOutGift("Peter");
handOutGift("Alison");
handOutGift("John");
handOutGift("Maria");
handOutGift("Peter");
