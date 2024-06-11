

abstract class BaseServer {
    protected port: number;
    protected address: string;

    constructor(port: number, address: string) {
        this.port = port;
        this.address = address;
    };

    abstract startServer(): void;

    abstract stopServer(): void;
};

class Server extends BaseServer {
    constructor(port: number, address: string) {
        super(port, address);
        console.log('Instatiating server');
    };

    startServer(): void {
        console.log(`Starting server at: ${this.address}:${this.port}`);        
    };

    stopServer(): void {
        console.log(`Stoping server: ${this.address}`);
    };
};


interface IServer {
    startServer(): void
    stopServer(): void
}

class InterfacedServer implements IServer {
    public port: number;
    public address: string;

    constructor(port: number, address: string) {
        this.port = port;
        this.address = address;
    };

    startServer(): void {
        console.log(`Starting interfaced server @${this.address}:${this.port}`);
    };

    stopServer(): void {
        console.log(`Stoping interfaced server ... ${this.address}`)
    };
};

const someServer = new Server(8080, 'localhost');
someServer.startServer();
someServer.stopServer();

const iServer: IServer = new InterfacedServer(8090, 'localhost');
iServer.startServer();
iServer.stopServer();
