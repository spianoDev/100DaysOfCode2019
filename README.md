# 100DaysOfCode2019

## A place where I show algorithmic problems and solutions in JavaScript and Python.

Please note the code will be organized by days and will include many comments to demonstrate my thinking as I work through the problem. This is much like a whiteboarding challenge and all answers are verified on [codewars](https://www.codewars.com/dashboard). Please visit the link to see more challenges.

Initially I wanted to only complete challenges that were algorithms but as December hit, I changed direction to 'themed' Kata specific to the upcoming holiday. Here is an example of a Christmas themed 6kyu javascript problem:

### Celebrating the Holidays - JavaScript Style

```javascript

function findOutChristmasWeekday(date) {
    // first I will set a new variable to the date as a date object
    const christmas = new Date(date);
    console.log(christmas.getDay());
    // the above console gives me exactly what I was expecting. So now I need to convert it to the return value of
    // the day of the week
    if (christmas.getDay() === 0) {
        return 'Sunday';
    } else if (christmas.getDay() === 1) {
        return 'Monday';
    } else if (christmas.getDay() === 2) {
        return 'Tuesday';
    } else if (christmas.getDay() === 3) {
        return 'Wednesday';
    } else if (christmas.getDay() === 4) {
        return 'Thursday';
    } else if (christmas.getDay() === 5) {
        return 'Friday';
    } else {
        return 'Saturday';
    }
}
console.log(findOutChristmasWeekday('2013 12 25'));
```

Here is an example of a 6kyu python problem that is a more typical algorithm. This particular piece of code passed all the codewars tests the first time I entered the solution!

### Python Algorithm Solution

```python
def clean_string(s):
    # Because any # later in the string will erase what is already added, I will use a list to store the values
    letters = []
    for char in s:
    # Add all the letters
        if char != '#':
            letters.append(char)
            # remove a letter for each #
        if char == '#' and len(letters) > 0:
            letters.pop()
    answer = ''.join(letters)
    print(answer)
    return answer
print(clean_string('abc####d##c#'))
```
### A clever solution in JavaScript
(From Day 47)

```javascript
function mineLocation(field){
    let mineLocation = [];
    let secondPlace;
    // I think the best way to do this is to compare values using a double loop to search the arrays
    for (let i = 0; i < field.length; i++) {
        // This tells me the second position of the mine
        secondPlace = field[i].indexOf(1);
        // I know the value that isn't -1 will contain the mine
        if (secondPlace >= 0) {
            console.log(i);
            mineLocation.unshift(i);
        }
           // console.log(secondPlace)
         if (secondPlace !== -1) {
             mineLocation.push(secondPlace);
        //     // console.log(mineLocation);
         }
    }

     console.log(mineLocation);
        return mineLocation;
}

mineLocation([[0, 0, 0], [0, 0, 1], [0, 0, 0] ]);
>>[1, 2]
```
### A working answer refactored in Python
(From Day 58)
```python
def parts_sums(ls):
# variable to store the answer
    answer = []
# I need to create a recursive loop that will add all the values
    while len(ls) >= 1:
# variable to store sum within each loop
        sum = 0
# Add the sum to the answer list
        for value in ls:
            sum += value
# put the sum into the answer list
        answer.append(sum)
        print(sum)
# remove the first value of the list and repeat the loop
        ls.pop(0)
        print(ls)
    if len(ls) == 0:
        answer.append(0)
# return the answer list
    print(answer)
    return answer

# parts_sums([])
# => [0]
# parts_sums([0, 1, 3, 6, 10])
# => [20, 20, 19, 16, 10, 0]
parts_sums([1, 2, 3, 4, 5, 6])
# => [21, 20, 18, 15, 11, 6, 0]

# The above solution works, but isn't efficient enough for the bigger value tests.
# Below is the refactored solution

def parts_sums(ls):
# variable to store the answer
    answer = []
# variable to store sum within each loop
    sum = 0
# Add the sum to the answer list
    for value in ls:
        sum += value
# put the sum into the answer list
    answer.append(sum)
# pointer variable to move on each iteration
    pointer = 0
# loop to iterate through the sums
    while pointer < len(ls):
        sum -= ls[pointer]
        answer.append(sum)
        pointer += 1
#         print(pointer)
    print(answer)
    return answer
```
### JavaScript Recursion
(From Day 85)
```javascript
function yesNo(arr){
    console.log(arr);
    // create a variables to hold the new order of the arrays
    let answer = [];
    let leftovers = arr;
    // loop through the original arr and add the even values to the circleArray
    function circleArray(array) {
        for (let i = 0; i < arr.length; i++) {
            if (i % 2 === 0) {
                answer.push(leftovers[i]);
            } else {
                // leftovers = [];
                leftovers.push(leftovers[i]);
            }
        }
    }
    circleArray(arr);
    // I think a recursive loop might work well, but I'm not sure how that will work since it is a different
    // sequence depending on the length of the original arr
    if (arr.length % 2 === 0) {
        circleArray(leftovers);
    }
    console.log(answer);
    return answer;
}
```
### Python Refactor (Top solution times out in tests)
(From Day 97)
```python
def simplify(number):
    number_list = []
    answer = []
# make the number into a string and put into a list
    for digit in str(number):
        number_list.append(digit)
# working from the back of the list, add the digit to answer list
    pointer = -1
    power_of_ten = 10
    while abs(pointer) <= len(number_list):
        if int(number_list[pointer]) != 0 and pointer == -1:
            answer.insert(0, number_list[pointer])
            pointer -= 1
# add the + character and the next digit multiplied by the unit value unless the digit is zero
        else:
            if pointer < -1 and int(number_list[pointer]) != 0:
                answer.insert(0, '+')
                answer.insert(0, str(power_of_ten))
                power_of_ten *= power_of_ten
                answer.insert(0, '*')
                answer.insert(0, number_list[pointer])
                pointer -= 1
            elif pointer < -1 and int(number_list[pointer]) == 0:
                power_of_ten *= power_of_ten
                pointer -= 1
# join the answer list and return it as a string
    print("".join(answer))
    return ''.join(answer)

# The above code works, but times out.
# try refactoring to use division and multiply by the number of digits in the number

def simplify(number):
    print(number)
# create necessary variables
    answer = []
    string_number = str(number)
    num_digits = len(string_number)
    index = 0
# using the num_digits, determine the formula
    while num_digits > 0 and index < len(string_number):
        if string_number[index] != '0' and index < len(string_number)-1:
            answer.append(string_number[index]+'*'+str(10**num_digits//10))
            index += 1
            num_digits -= 1
        else:
            index += 1
            num_digits -= 1
    if string_number[-1] != '0':
        answer.append(string_number[-1])

    print('+'.join(answer))
    return '+'.join(answer)



simplify(8964631) # "8*1000000+9*100000+6*10000+4*1000+6*100+3*10+1"
# simplify(56) #"5*10+6"
# simplify(999) #"9*100+9*10+9"
# simplify(11) # "1*10+1"
# simplify(991) # "9*100+9*10+1"
# simplify(47) # "4*10+7"
# simplify(234) # "2*100+3*10+4"
# simplify(196587) # "1*100000+9*10000+6*1000+5*100+8*10+7"
# simplify(660)
```
