

class Product {
    private id: string
    protected price: number
    protected description: string
    constructor(id: string, price: number, description: string) {
        this.id = id
        this.price = price
        this.description = description
    }
    public display(): void {
        console.log('--------------')
        console.log(`Product id: ${this.id}\n${this.description}\nCost: ${this.price}`)
    }
}

class Book extends Product {
    private author
    private title
    constructor(id: string, price: number, description: string, author: string, title: string) {
        super(id, price, description)
        this.author = author
        this.title = title
    }
    public display(): void {
        super.display()
        console.log(`Author: ${this.author}\nTitle: ${this.title}`)
    }
}

class Electronic extends Product {
    private brand: string
    private model: string
    constructor(id: string, price: number, description: string, brand: string, model: string) {
        super(id, price, description)
        this.brand = brand
        this.model = model
    }
    public display(): void {
        super.display()
        console.log(`Brand: ${this.brand}\nModel: ${this.model}`)
    }
}

const chair = new Product('1', 10, 'Four legs chair')
chair.display()

const book = new Book('2', 15, 'Novel', 'Shakespeare', 'Hamlet')
book.display()

const cellphone = new Electronic('3', 100, 'Smartphone', 'T', 'T-120')
cellphone.display()