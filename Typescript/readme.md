## Reference
[Typescript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)

## cheat sheet
![Control flow](assets/TypeScript%20Control%20Flow%20Analysis.png)
![Types](assets/TypeScript%20Classes.png)
![Interface](assets/TypeScript%20Interfaces.png)
![Class](assets/TypeScript%20Classes.png)

## question mark
[question mark](https://www.becomebetterprogrammer.com/typescript-question-mark/)

## undefined error
You can either use ! (non-nullable assertion operator) to tell TypeScript that a property is not undefined or null (assuming you are 100% SURE), or check it and assign it if it's undefined.
```
<!-- Example 1: -->
<!-- if cannot be undefined -->
config.headers!.Authorization = `Bearer ${accessToken}`;

<!-- Example 2: -->
<!-- default it with an empty object -->
config.headers = config.headers ?? {};

<!-- Example 3: -->
if(!config.headers) config.headers =  {};
```

## difference between type aliases and interface
![difference between type aliases and interface](assets/types_vs_interface.png)

## function type expression
![function type expression](assets/function_type_expression.png)

## Tutorial
```javascript
// static coding
// mapout what your variable, function should look like, make your code more robost
/*
======================================================================================
*/
// basic types
let id: number = 5;
let company: string = 'maple';
let isPublished: boolean = true;
let x: any = 'hello';

// array
let ids: number[] = [1, 2, 3, 4, 5];
let arr: any[] = [1, 2, true, 'hello'];

// tuple
let person: [number, string, boolean] = [1, 'maple', true];

// tuple array
let employee: [number, string][] = [
  [1, 'maple'],
  [2, 'john'],
];

// union (or)
let pid: string | number;
pid = 23;

// enum
enum direction {
  up,
  down,
  left,
  right,
}
console.log(direction.up);

// objects
type User = {
  id: number;
  name: string;
};
const user: User = {
  id: 1,
  name: 'maple',
};
/*
======================================================================================
*/
// type assertion
let cid: any = 1;
// assign cid to customerId and specified the type
let customerId = <number>cid; // let customerId = cid as number
/*
======================================================================================
*/
// functions
function addNum(x: number, y: number): number {
  return x + y;
}

function log(msg: string | number): void {
  console.log(msg);
}
/*
======================================================================================
*/
// interfaces (define customer type)
interface UserInterface {
  readonly id: number; // a readonly property
  name: string;
  age?: number; // option
}
const user1: UserInterface = {
  id: 1,
  name: 'maple',
};
user1.age = 10;
/*
======================================================================================
*/
// interface for a function
interface mathFunc {
  (x: number, y: number): number;
}
const add: mathFunc = (x: number, y: number): number => {
  return x + y;
};
/*
======================================================================================
*/
// classes (available since es6)
interface PersonInterface {
  readonly id: number; // a readonly property
  name: string;
  age?: number; // option
  register(): string;
}

class Person implements PersonInterface {
  id: number; // only accessible within class
  name: string;

  // constructor will run when the class is initiated
  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  // define a method
  register() {
    return `${this.name} is now registered`;
  }
}
const p1 = new Person(1, 'maple');
console.log(p1.name);
console.log(p1.register());
/*
======================================================================================
*/
// extend a class
class Employee extends Person {
  postion: string;

  constructor(id: number, name: string, position: string) {
    super(id, name);
    this.postion = position;
  }
}

const p2 = new Employee(2, 'john', 'manager');
console.log(p2);
console.log(p2.register());
/*
======================================================================================
*/
// generic
// it is like setting type as a variable in a function
function getArray<Type>(items: Type[]): Type[] {
  // Type here is a placeholder/variable
  return new Array().concat(items);
}

let numArray = getArray([1, 2, 3, 4]);
let strArray = getArray(['a', 'b', 'c', 'd']);

```