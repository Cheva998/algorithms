


let var1 = undefined;

const var2 = null;

function getData(): string | undefined {
    return '';
};

const data = getData();

if (data) {
    const someData = data;
} 


let userInput: unknown;
userInput = 'some input';

let otherInput: string;


if (typeof userInput === 'string') {
    otherInput = userInput;
}

console.log(otherInput!)


function doTasks(tasks: number): void | never {
    if (tasks > 3) {
        throw new Error('Too many tasks');
    }
}

const stuff = doTasks(2);