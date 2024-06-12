
interface Person {
    firstName: string,
    lastName: string,
    job?: job,
    isVisitor?: boolean
}

type job = 'Engineer' | 'Programmer'

function generateEmail(input: Person, force?: boolean): string | undefined {
    if (input.isVisitor && !force) {
        return undefined
    } else {
        return `${input.firstName}.${input.lastName}@email.com`
    }
}

const abc: string | undefined = generateEmail({} as any);

function isPerson(potentialPerson: any): boolean {
    if ('firstName' in potentialPerson &&
        'lastName' in potentialPerson) {
            return true;
    } else {
        return false;
    }
}

function printEmailIfPerson(potentialPerson: any): void {
    if (isPerson(potentialPerson)) {
        console.log(generateEmail(potentialPerson));
    } else {
        console.log('Not a person');
    }
}


printEmailIfPerson({
    firstName: 'John',
    lastName: "Doe"
})

