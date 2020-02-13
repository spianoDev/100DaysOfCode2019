// 6kyu on CodeWars: https://www.codewars.com/kata/5208f99aee097e6552000148/train/javascript

// Complete the solution so that the function will break up camel casing, using a space between words.
//
//     Example
// solution("camelCasing")  ==  "camel Casing"

function solution(string) {
        // after much trial and error I discovered this simplified solution using regex
        let newString = string.replace(/([A-Z])/g, ' $1').trim();
        console.log(newString);
        return newString;
}

// solution('helloWorld'); // hello World
solution('heyThereBeautiful'); // hey There Beautiful
