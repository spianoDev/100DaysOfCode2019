//  4kyu on CodeWars: https://www.codewars.com/kata/56fa9cd6da8ca623f9001233/train/javascript

// Each element in the periodic table has a symbol associated with it. For instance, the symbol for the element Yttrium is Y. A fun thing to do is see if we can form words using symbols of elements strung together. The symbol for Einsteinium is Es, so the symbols for Yttrium and Einsteinium together form:
//
//     Y + Es = YEs
//
// Yes! Ignoring capitalization, we can think of any string of letters formed by the concatenation of one or more element symbols as an elemental word -- per the above,yes is an elemental word. There is only one combination of element symbols that can form yes, but in general, there may be more than one combination of element symbols that can form a given elemental word. Let's call each different combination of element symbols that can form a given elemental word word an elemental form of word.
//
// Your task is to implement the function elementalForms(word), which takes one parameter (the string word), and returns an array (which we'll call forms). If word can be formed by combining element symbols from the periodic table, then forms should contain one or more sub-arrays, each consisting of strings of the form 'elementName (elementSymbol)', for each unique combination of elements that can form word.
//
// ###Example
//
// The word 'snack' can be formed by concatenating the symbols of 3 different combinations of elements:
//
//     ----------------------------------------------------
//     |       1        |       2        |       3        |
//     |---------------------------------------------------
//     | Sulfur    (S)  | Sulfur    (S)  | Tin       (Sn) |
//     | Nitrogen  (N)  | Sodium    (Na) | Actinium  (Ac) |
//     | Actinium  (Ac) | Carbon    (C)  | Potassium (K)  |
//     | Potassium (K)  | Potassium (K)  |                |
//     ----------------------------------------------------
//         So elementalForms('snack') should return the following array:
//
//     [
//         ['Sulfur (S)', 'Nitrogen (N)', 'Actinium (Ac)', 'Potassium (K)'],
//         ['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)'],
//         ['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)']
//     ]
// ###Guidelines
//
// Capitalization does not matter:
//     elementalForms('beach')
// // => [ ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)'] ]
// elementalForms('BEACH')
// // => [ ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)'] ]
// The order of the returned sub-arrays does not matter, but the order of the strings within each sub-array does matter -- they should be in the order that "spells out" word.
//     If word is not an elemental word (that is, no combination of element symbols can form word), return an empty array.
//     You do not need to check the type of word. It will always be a (possibly empty) string.
//     Finally, the helper object ELEMENTS has been provided, which is a map from each element symbol to its corresponding full name (e.g. ELEMENTS['Na'] === 'Sodium'). Have fun!

// the 'ELEMENTS' variable provided by the Kata
let ELEMENTS = { H: 'Hydrogen',
    He: 'Helium',
    Li: 'Lithium',
    Be: 'Beryllium',
    B: 'Boron',
    C: 'Carbon',
    N: 'Nitrogen',
    O: 'Oxygen',
    F: 'Fluorine',
    Ne: 'Neon',
    Na: 'Sodium',
    Mg: 'Magnesium',
    Al: 'Aluminium',
    Si: 'Silicon',
    P: 'Phosphorus',
    S: 'Sulfur',
    Cl: 'Chlorine',
    Ar: 'Argon',
    K: 'Potassium',
    Ca: 'Calcium',
    Sc: 'Scandium',
    Ti: 'Titanium',
    V: 'Vanadium',
    Cr: 'Chromium',
    Mn: 'Manganese',
    Fe: 'Iron',
    Co: 'Cobalt',
    Ni: 'Nickel',
    Cu: 'Copper',
    Zn: 'Zinc',
    Ga: 'Gallium',
    Ge: 'Germanium',
    As: 'Arsenic',
    Se: 'Selenium',
    Br: 'Bromine',
    Kr: 'Krypton',
    Rb: 'Rubidium',
    Sr: 'Strontium',
    Y: 'Yttrium',
    Zr: 'Zirconium',
    Nb: 'Niobium',
    Mo: 'Molybdenum',
    Tc: 'Technetium',
    Ru: 'Ruthenium',
    Rh: 'Rhodium',
    Pd: 'Palladium',
    Ag: 'Silver',
    Cd: 'Cadmium',
    In: 'Indium',
    Sn: 'Tin',
    Sb: 'Antimony',
    Te: 'Tellurium',
    I: 'Iodine',
    Xe: 'Xenon',
    Cs: 'Caesium',
    Ba: 'Barium',
    Hf: 'Hafnium',
    Ta: 'Tantalum',
    W: 'Tungsten',
    Re: 'Rhenium',
    Os: 'Osmium',
    Ir: 'Iridium',
    Pt: 'Platinum',
    Au: 'Gold',
    Hg: 'Mercury',
    Tl: 'Thallium',
    Pb: 'Lead',
    Bi: 'Bismuth',
    Po: 'Polonium',
    At: 'Astatine',
    Rn: 'Radon',
    Fr: 'Francium',
    Ra: 'Radium',
    Rf: 'Rutherfordium',
    Db: 'Dubnium',
    Sg: 'Seaborgium',
    Bh: 'Bohrium',
    Hs: 'Hassium',
    Mt: 'Meitnerium',
    Ds: 'Darmstadtium',
    Rg: 'Roentgenium',
    Cn: 'Copernicium',
    Uut: 'Ununtrium',
    Fl: 'Flerovium',
    Uup: 'Ununpentium',
    Lv: 'Livermorium',
    Uus: 'Ununseptium',
    Uuo: 'Ununoctium',
    La: 'Lanthanum',
    Ce: 'Cerium',
    Pr: 'Praseodymium',
    Nd: 'Neodymium',
    Pm: 'Promethium',
    Sm: 'Samarium',
    Eu: 'Europium',
    Gd: 'Gadolinium',
    Tb: 'Terbium',
    Dy: 'Dysprosium',
    Ho: 'Holmium',
    Er: 'Erbium',
    Tm: 'Thulium',
    Yb: 'Ytterbium',
    Lu: 'Lutetium',
    Ac: 'Actinium',
    Th: 'Thorium',
    Pa: 'Protactinium',
    U: 'Uranium',
    Np: 'Neptunium',
    Pu: 'Plutonium',
    Am: 'Americium',
    Cm: 'Curium',
    Bk: 'Berkelium',
    Cf: 'Californium',
    Es: 'Einsteinium',
    Fm: 'Fermium',
    Md: 'Mendelevium',
    No: 'Nobelium',
    Lr: 'Lawrencium' };

function elementalForms(word) {
    // first I used this console.log to collect the provided key //console.log(ELEMENTS);
    // in looking at the elements, there are a handful of three letter options, none of which form words, so I can
    // focus on the two letter and one letter key/value pairs for the solution
    // Make an array of all the keys in elements and word case insensitive
    word = word.toLowerCase();
    let elementKeys = [];
    for (let element of Object.keys(ELEMENTS)) {
        elementKeys.push(element.toLowerCase());
    }
    // console.log(elementKeys);
    // need a variable to house the double matching keys and single matching keys with the characters in word
    let doubleMatches = [];
    let singleMatches = [];
    // compare each character of the word to the elementKeys
    for (let c = 0; c < word.length; c++) {
        let multiChar = [];
        multiChar.push(word[c] + word[c + 1]);
        // console.log(multiChar);
        // search for double characters first
        for (let i = 0; i < elementKeys.length; i++) {
            for (let m = 0; m < multiChar.length; m++) {
                if (elementKeys[i] === multiChar[m]) {
                    console.log('matching doubles at ' + elementKeys[i]);
                    doubleMatches.push(elementKeys[i]);
                    console.log('matches so far ' + doubleMatches);
                }
            }
        }
    }
        let answer = doubleMatches.join('');
        if (answer === word) {
            console.log('got it');
        } else {
            // loop through the elementKeys again looking for the single options
            for (let c = 0; c < word.length; c++) {
                for (let i = 0; i < elementKeys.length; i++) {
                    if (elementKeys[i] === word[c]) {
                                console.log('these also match ' + elementKeys[i]);
                                singleMatches.push(elementKeys[i]);
                    }
                    }
                }
            }
        // loop through the answer and if there is a match, remove that value from the singleMatches array
        for (let char of answer) {
            for (let s = 0; s < singleMatches.length; s++) {
                if (char === singleMatches[s]) {
                    console.log(singleMatches[s]);
                    singleMatches.splice(s, 1);
                }
                    }
        }
        // need to remove any possible extra entries
        for (let v = 0; v < doubleMatches.length; v++) {
            while ((v+2) <= doubleMatches.length - 1) {
                if (doubleMatches[v][1] === doubleMatches[v + 1][0] && doubleMatches[v + 1][1] === doubleMatches[v + 2][0]) {
                    doubleMatches.splice(v + 1, 1);
                }
            }
        }
        console.log('double matches: ' +doubleMatches);
        console.log('single matches: ' +singleMatches);
        // now I need to put together those matches and create the final return
        let elementalWord = [];
        let index = 0;
        while (singleMatches.length >= 1 || doubleMatches.length >= 1) {
            if (singleMatches[0] === word[index]) {
                console.log('it is a single first');
                let elementKey = singleMatches[0].toUpperCase();
                console.log(elementKey);
                elementalWord.push(ELEMENTS[elementKey] + ' (' + elementKey + ')');
                singleMatches.splice(0, 1);
                index += 1;
            } else {
                console.log('doubles then');
                let elementKey = doubleMatches[0][0].toUpperCase() + doubleMatches[0][1];
                console.log(elementKey);
                elementalWord.push(ELEMENTS[elementKey] + ' (' + elementKey + ')');
                doubleMatches.splice(0, 1);
                index += 2;
                console.log('index is ' +index);
            }
        }
        console.log(elementalWord);
        return elementalWord;
}

// elementalForms('yes'); // ['Yttrium (Y)', 'Einsteinium (Es)']
elementalForms('beach'); // ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']
// elementalForms('BEACH'); // ['Beryllium (Be)', 'Actinium (Ac)', 'Hydrogen (H)']
// elementalForms('snack'); //  ['Tin (Sn)', 'Actinium (Ac)', 'Potassium (K)'], or ['Sulfur (S)', 'Nitrogen (N)',
// 'Actinium (Ac)', 'Potassium (K)'], or ['Sulfur (S)', 'Sodium (Na)', 'Carbon (C)', 'Potassium (K)']

// Well I gave this one my best shot, but it is a bit more complicated than I anticipated.
