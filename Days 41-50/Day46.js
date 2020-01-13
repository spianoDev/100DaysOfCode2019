//6kyu on CodeWars: https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf/train/javascript

// You will be given a string (x) featuring a cat 'C', a dog 'D' and a mouse 'm'.
// The rest of the string will be made up of '.'.
//
// You need to find out if the cat can catch the mouse from it's current position.
// The cat can jump (j) characters.
//
// Also, the cat cannot jump over the dog.
//
// So:
//
// if j = 5:
//
// ..C.....m. returns 'Caught!' <-- not more than j characters between
//
// .....C............m...... returns 'Escaped!' <-- as there are more than j characters between the two, the cat can't jump far enough
//
// if j = 10:
//
// ...m.........C...D returns 'Caught!' <--Cat can jump far enough and jump is not over dog
//
// ...m....D....C....... returns 'Protected!' <-- Cat can jump far enough, but dog is in the way, protecting the mouse
//
// Finally, if all three animals are not present, return 'boring without all three'

function catMouse(x, j){
    // first I will check to be sure all dog, cat, and mouse exist (a return of -1 means the char is missing)
        if (x.indexOf('C') === -1 || x.indexOf('D') === -1 || x.indexOf('m') === -1) {
            console.log('boring without all three');
            return 'boring without all three';
        } else {
            // next I need variables to store the index of each element so I can compare with the jumping value
            let catIndex = x.indexOf('C');
            let dogIndex = x.indexOf('D');
            let mouseIndex = x.indexOf('m');
            // and now to compare the Dog, Cat, and mouse values (need the absolute value)
            let distanceToMouse = Math.abs(mouseIndex - catIndex);
            let distanceToDog = Math.abs(dogIndex - catIndex);
            console.log('The distance to the dog is ' + distanceToDog);
            console.log('The distance to the mouse is ' + distanceToMouse);
            if (distanceToMouse > j) {
                console.log('Escaped!');
                return 'Escaped!';
            } else if (mouseIndex < dogIndex && dogIndex < catIndex) {
                console.log('Protected!');
                return 'Protected!';
            } else if (mouseIndex > dogIndex && dogIndex > catIndex) {
                console.log('Protected!');
                return 'Protected!';
            } else if (distanceToMouse <= j)  {
                console.log('Caught!');
                return 'Caught!';
            } else if (dogIndex < catIndex) {
                console.log('Caught!');
                return 'Caught!';
            }
            else if (distanceToDog < distanceToMouse && dogIndex > catIndex) {
                console.log('Protected!');
                return 'Protected!';
            }
        }
}

catMouse('CD....m..............', 10);
