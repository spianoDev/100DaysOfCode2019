// 7kyu on CodeWars: https://www.codewars.com/kata/fuel-economy-converter-mpg-l-slash-100-km/train/javascript
//Background
// While mpg (miles per gallon) is a common unit of measurement for fuel economy in North America, for Europe the standard unit of measurement is generally liter per 100 km. Conversion between these units is somewhat hard to calculate in your head, so your task here is to implement a simple convertor in both directions.
//
// Functions
// mpg2lp100km() converts from miles per gallon to liter per 100 km.
// lp100km2mpg() converts in the opposite direction.
// Output
// The output of both functions should be a number rounded to 2 decimal places.
//
// Examples
// mpg2lp100km(42) returns 5.6
// lp100km2mpg( 9) returns 26.13
// Reference
// For this kata, use U.S. gallon, not imperial gallon.
//
// 1 gallon = 3.785411784 liters
// 1 mile = 1.609344 kilometers

// the first function converts gallons to liters
let kilometers = 1.609344;
let liters = 3.785411784;

function mpg2lp100km(miles){
    // The big piece of this for me is figuring out exactly what I need to convert.
    // I will start by translating the miles into kilometers on one gallon of gas
    let convertToKilometers = miles * 1.609344;
    console.log(convertToKilometers + ' kilometers traveled');
    // next I will convert the miles traveled for each liter of gas.
    let milesPerLiter = miles / 3.785411784;
    console.log(milesPerLiter + ' miles for each liter of gas');
    // final conversion: 100 km / (number of km traveled/liters)
    let answer = 100/(convertToKilometers/liters);
    // Round to hundredths place:
    answer = Math.round(answer * 100)/100;
    console.log(answer);
    return answer;

}
mpg2lp100km(42);

function lp100km2mpg(numberOFLiters){
    // Now for the reverse. First I'm going to see how many km are traveled for each liter of gas.
    let kmPerLiter = 100 / numberOFLiters;
    console.log(kmPerLiter + ' km traveled for each liter of gas');
    // Next convert the liters into gallons
    let kmPerGallon = kmPerLiter * liters;
    // final conversion into miles.
    let mpg = kmPerGallon/kilometers;
    mpg = Math.round(mpg * 100)/100;
    console.log(mpg);
    return mpg;
}

lp100km2mpg(9);
