



abstract class BaseServer {
    protected port: number;
    protected address: string;

    constructor(port: number, address: string) {
        this.port = port;
        this.address = address;
    }

    startServer() {
        console.log(`Starting server at: ${this.address}:${this.port}`)
    }

    abstract stopServer(): void
    
}

