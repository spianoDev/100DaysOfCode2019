// 7kyu on CodeWars: https://www.codewars.com/kata/sort-the-gift-code/train/javascript

//Happy Holidays fellow Code Warriors!
// Santa's senior gift organizer Elf developed a way to represent up to 26 gifts by assigning a unique alphabetical character to each gift. After each gift was assigned a character, the gift organizer Elf then joined the characters to form the gift ordering code.
//
// Santa asked his organizer to order the characters in alphabetical order, but the Elf fell asleep from consuming too much hot chocolate and candy canes! Can you help him out?
//
// Sort the Gift Code
// Write a function called sortGiftCode/sort_gift_code/SortGiftCode that accepts a string containing up to 26 unique alphabetical characters, and returns a string containing the same characters in alphabetical order.
//
// Examples:
// sortGiftCode( 'abcdef' ); //=> returns 'abcdef'
// sortGiftCode( 'pqksuvy' ); //=> returns 'kpqsuvy'
// sortGiftCode( 'zyxwvutsrqponmlkjihgfedcba' ); //=> returns 'abcdefghijklmnopqrstuvwxyz'

function sortGiftCode(code){
    //I'm going to start by splitting the string into an array.
    let codeArray = code.split('');
    //Next I will sort the values into alphabetical order
    codeArray = codeArray.sort();
    //Finally, I will join the array to return the sorted string.
    codeArray = codeArray.join('');
    console.log(codeArray);
    return codeArray;
}

sortGiftCode( 'pqksuvy' );
