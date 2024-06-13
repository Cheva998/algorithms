"use strict";
function returnKeys(arg) {
    console.log(Object.keys(arg));
    return arg;
}
const a = returnKeys({
    abc: 'def'
});
const John = {
    special: "Special prop",
    name: 'Sebas',
    age: 22
};
class Observable {
    subscribe(arg) {
        console.log(`Sub to ${arg.name}`);
    }
}
let obs = new Observable();
obs.subscribe(John);
console.log(obs.special);
