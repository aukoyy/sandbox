// @ts-check

let ex1: string = 'hello';
let ex2: string | number = 'hello';

const arrayExample = [1, 2, 3, 4, 5]
let ex3 = arrayExample.reduce((num1, num2) => num1 + num2);

// Checking types: bear instanceOf Bear

// When you know better:
let definetlyNotAString: any = 'I am a string';
let strLength = (<string> definetlyNotAString).length;


const ex4: (number | boolean)[] = [1, 2, true];
const ex5 : boolean [][] = [[true, false], [false, true]];

// Tuples

const exampleTuple: [string, number] = ['hello world', 30];

// Enums

export enum Age {
    dylan = 30,
    mother = 21,
}

function totalAge(age1: Age, age2: Age) {
    return Age.dylan + age2;
}

function add(val1: number, val2: number): number {
    return val1 + val2;
}

function neverExample(): never {
    throw Error
}

// Interfaces
export interface Person {
    firstName: string;
    middleName: string;
    lastName: string;
}

