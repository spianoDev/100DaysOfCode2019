// 5kyu on CodeWars: https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/javascript

// Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue.
// The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue.
// Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.
//
//     For example, Penny drinks the third can of cola and the queue will look like this:
//
// Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny
// Write a program that will return the name of the person who will drink the n-th cola.
//
//     Input
// The input data consist of an array which contains at least 1 name, and single integer n which may go as high as the biggest
// number your language of choice supports (if there's such limit, of course).
//
// Output / Examples
// Return the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1.
//
// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) == "Sheldon"
// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny"
// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard"

function whoIsNext(names, r){
    // for tests I needed to see the value options
    console.log(names);
    console.log(r);
    let answer;
    //edge cases for r < or = names.length
    if (r < names.length) {
        answer = names[r-1];
        console.log(answer);
        return answer
    } else {
        // Since each time the person drinking doubles at the end of the queue, it means new sequence of the queue
        // increases by 10. So, after first 5 people, you add 10, after that it's 20, and 30, and 40...
        let count = names.length * 2;
        r -= names.length;
        while (r > 0) {
            r -= count;
            count += names.length * 2;
        }
        if (Math.abs(r) < names.length) {
            answer = names[r - 1];
            console.log('this is the answer : ' + answer);
        // }
        // if (Math.abs(r) < names.length * names.length) {
        //     let index = Math.floor(Math.abs(r) / names.length);
        //     console.log('this is the index: ' + index);
        //     console.log('this is now r : ' + r);
        //     answer = names[index];
        //     console.log('This is what is returned ' + answer);
        //     return answer;
        } else {
            let index = Math.floor(Math.abs(r) / names.length);
            // if the index value is very high, need to keep dividing the value by 5 until you reach a number less than 5.
            while (index > names.length) {
                index /= names.length;
                console.log(index);
            }
            // if the index is an int, need to subtract 1 from the answer
            if (Number.isInteger(index)) {
                index -= 1;
            } else {
                // need to round down and that will return the correct value of the index.
                index -= 1;
                index = Math.floor(index);
            }
            console.log('this is the index: ' + index);
            console.log('this is now r : ' + r);
            answer = names[index];
            console.log('This is what is returned ' + answer);
            return answer;
        }
    }
}

// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1); // "Sheldon"
// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52); // "Penny"
// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951); // "Leonard"
// whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 6);
whoIsNext([ 'Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard' ], 1802);

// I can pass the test cases, but I'm stumped on the wider tests. Tried some new things and I'm still stumped since
// sometimes I'm off by one but other times I'm off more than that...
