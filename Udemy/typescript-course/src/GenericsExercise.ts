


function returnKeys<T extends Object>(arg: T){
    console.log(Object.keys(arg))
    return arg;
}

const a = returnKeys({
    abc: 'def'
})


interface PersonGen <T>{
    name: string,
    age: number,
    special: T
}


const John: PersonGen<string> = {
    special: "Special prop",
    name: 'Sebas',
    age: 22
}


class Observable <T extends PersonGen<string>> {
    subscribe(arg: T){
        console.log(`Sub to ${arg.name}`)
    }
}

let obs = new Observable<typeof John>()
obs.subscribe(John)
console.log((obs as any).special)