

interface ShapeProperties {
    color: string;
    x: number;
    y: number;
}

abstract class Shape {
    constructor(public properties: ShapeProperties) {}

    public abstract clone(): Shape
}

class Rectangle extends Shape {
    constructor(public width: number, public height: number, properties: ShapeProperties) {
        super(properties)
    }
    public clone(): Shape {
        const props: ShapeProperties = {
            color: this.properties.color,
            x: this.properties.x,
            y: this.properties.y
        }
        return new Rectangle(this.width, this.height, props)
        
    }
}

class Circle extends Shape {
    constructor(public radius: number, properties: ShapeProperties) {
        super(properties)
    }

    public clone(): Shape {
        const props: ShapeProperties = {
            color: this.properties.color,
            x: this.properties.x,
            y: this.properties.y
        }
        
        return new Circle(this.radius, props)
    }
}

const props: ShapeProperties = {
    color: 'red',
    x: 2,
    y: 3
}

const rect = new Rectangle(4, 5, props)

const rect2 = rect.clone()
rect2.properties.color = 'black'


console.log(rect === rect2)
console.log(rect)
console.log(rect2)