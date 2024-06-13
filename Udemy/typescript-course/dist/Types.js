"use strict";
let var1 = undefined;
const var2 = null;
function getData() {
    return '';
}
;
const data = getData();
if (data) {
    const someData = data;
}
let userInput;
userInput = 'some input';
let otherInput;
if (typeof userInput === 'string') {
    otherInput = userInput;
}
console.log(otherInput);
function doTasks(tasks) {
    if (tasks > 3) {
        throw new Error('Too many tasks');
    }
}
const stuff = doTasks(2);
