// 6kyu on CodeWars: https://www.codewars.com/kata/5970df092ef474680a0000c9/train/javascript

// The alphabetized kata
// Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order.
// Whitespace and punctuation shall simply be removed!
//
// The input is restricted to contain no numerals and only words containing the english alphabet letters.
//
//     Example:
//
// alphabetized("The Holy Bible") // "BbeehHilloTy"

function alphabetized(s) {
    console.log(s);
    let letters = /^[A-Za-z]/g;
    // need to delete all non-alpha characters including spaces
    let newArr = [];
    for (let n = 0; n < s.length; n++) {
        // console.log(s[n].search(letters));
        if (s[n].search(letters) === -1) {
            console.log(s[n]);
        } else {
            newArr.push(s[n]);
        }
    }
    console.log(newArr);
    // if the string is reduced to nothing, return an empty string
    if (newArr.length === 0) {
        return '';
    } else {
        let nonAlphaRemoved = newArr.join('');
        console.log('nonAlphaRemoved = ' + nonAlphaRemoved);
        let alphaOrder = newArr.sort();
        console.log('sorted array ' + alphaOrder);
        let alphaString = alphaOrder.join('');
        let uppers = /([^A-Z])/g;
        // in order to get the alpha order also in order of appearance, I need to compare the
        // uppercase instances with the lowercase ones
        let count = 0;
        for (let char of alphaOrder) {
            // console.log(uppers);
            if (char.search(uppers)) {
                count += 1;
            }
        }
        // now I will check the values of the uppercase against the original array
        for (let c = 0; c < count; c++) {
            let character = alphaString[c];

            if (nonAlphaRemoved.indexOf(character) > nonAlphaRemoved.indexOf(character.toLowerCase())) {
                let targetIndex = alphaString.indexOf(character.toLowerCase());
                // console.log(targetIndex);
                // this will move the uppercase letter to behind the lowercase letter
                if (targetIndex >= 0) {
                    alphaOrder.splice(targetIndex + 1, 0, character);
                }
                // this will move the uppercase letter to alpha order at the end
                if (targetIndex === -1) {
                    alphaOrder.splice(targetIndex, 0, character);
                }
            }// if the uppercase letter is after the lowercase in the original string I need to move it after
            // but now both the uppercase letters are placed after the lowercase letters.
             else if (nonAlphaRemoved.indexOf(character) < nonAlphaRemoved.lastIndexOf(character)){
                let targetIndex = alphaString.lastIndexOf(character.toLowerCase());
                alphaOrder.splice(targetIndex + 1, 0, character);
            }
             //changing the else if to if statements returns the uppercase J to in front of the lowercase ones
             else if (nonAlphaRemoved.indexOf(character) < nonAlphaRemoved.indexOf(character.toLowerCase())) {
                let targetIndex = alphaString.indexOf(character.toLowerCase());
                // this will move the uppercase letter to behind the lowercase letter
                if (targetIndex >= 0) {
                    alphaOrder.splice(targetIndex, 0, character);
                }
            }
            // now I need to remove the extra capitol letters from the beginning of the array
            let newString = alphaOrder.join('');
            console.log('after all the moves ' +newString);
            // console.log('resulting ' +newString);
            if (newString.lastIndexOf(character) !== newString.indexOf(character)) {
                console.log(character);
                alphaOrder.splice(newString.indexOf(character), 1);
            }
        }
        console.log(alphaOrder.join());
        // console.log(alphaString);
        return alphaOrder.join('');
    }
}

// alphabetized('The Holy Bible'); //'BbeehHilloTy'
// alphabetized('6$)*+,-@^');
// alphabetized('waJ NeFnou6tAf Tfkn6knWKjg'); // 'aAeFffgJjkkKNnnnotTuwW'
alphabetized('NnosvPo6fkJjCgVfpjK6Jpck'); // 'CcffgJjjJkKkNnooPppsvV'
