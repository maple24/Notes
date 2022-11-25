## Tutorial
```sh
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