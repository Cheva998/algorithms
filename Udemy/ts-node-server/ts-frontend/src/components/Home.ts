



export class Home {
    private container = document.createElement('div');

    render() {
        const pageLabel = document.createElement('label');
        pageLabel.innerText = "Welcome to Home page";
        this.container.append(pageLabel);
        return this.container;
    }
}