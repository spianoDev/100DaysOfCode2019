//  5kyu on CodeWars: https://www.codewars.com/kata/59847be2dff3ac9f0200011f/train/javascript

// A teacher decides to give toffees to his students. He asks n students to stand in a queue. Since the teacher is very partial, he follows the following rule to distribute toffees.
//     He looks at the first two students and gives more toffees to the student having higher marks than the other one. If they have the same marks they get the same number of toffees. The same procedure is followed for each pair of adjacent students starting from the first one to the last one.
//     It is given that each student receives at least one toffee. You have to find the number of toffees given to each student by the teacher such that the total number of toffees is minimum.
//
//     Input:
// The input gives a string with n - 1(where 2 ≤ n ≤ 1000) characters consisting of 'L', 'R' and '='. For each pair of adjacent students, 'L' means that the left student has higher marks, 'R' means that the right student has higher marks and '=' means that both have equal marks.
//
//     Output:
// Output consists of array with n integers representing the number of toffees each student receives in the queue starting from the first one to the last one.
//
//     Examples:
//
// ('LRLR') => [2, 1, 2, 1, 2]
// ('=RRR') => [1, 1, 2, 3, 4]

function partialTeacher(s){
    // variable for array output
    let answer = [];
    // count variables
    let equalCount = 1;
    let rightCount = 1;
    let leftCount = 1;
    // begin the answer with initial values according to s values
    if (s[0] === '=') {
        answer.push(1);
    } if (s[0] === 'L') {
        answer.push(2);
        answer.push(1);
    } if (s[0] === 'R') {
        answer.push(1);
        rightCount = 2;
        answer.push(rightCount);
    }
    // loop through each character in s
    for (let i = 0; i < s.length; i++) {
        console.log(s[i]);
        // assign values according to the char result
        if (s[i] === '='){
            answer.push(equalCount);
        } else if (s[i] === 'R') {
            if (s[i - 1] === 'R') {
                rightCount += 1;
                answer.push(rightCount);
            } if (s[i - 1] === 'L') {
                rightCount = leftCount + 1;
                answer.push(rightCount);
            } if (s[i - 1] === '='){
                rightCount = equalCount + 1;
                answer.push(rightCount);
            }
        } else if (s[i] === 'L') {
            if (s[i - 1] === 'R') {
                leftCount = rightCount - leftCount;
                answer.push(leftCount);
            } if (s[i - 1] === 'L') {
                leftCount = leftCount - 1;
                answer.push(leftCount);
            } if (s[i - 1] === '='){
                leftCount = equalCount;
                answer.push(leftCount);
            }
        }
    }
    console.log(answer);
    return answer;
}

// partialTeacher('LRLR'); // [2,1,2,1,2]
// partialTeacher('=RRR'); // [1,1,2,3,4]
// partialTeacher('=RLR');
partialTeacher('RRRR');
