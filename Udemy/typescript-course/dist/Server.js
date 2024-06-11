"use strict";
class BaseServer {
    constructor(port, address) {
        this.port = port;
        this.address = address;
    }
    ;
}
;
class Server extends BaseServer {
    constructor(port, address) {
        super(port, address);
        console.log('Instatiating server');
    }
    ;
    startServer() {
        console.log(`Starting server at: ${this.address}:${this.port}`);
    }
    ;
    stopServer() {
        console.log(`Stoping server: ${this.address}`);
    }
    ;
}
;
class InterfacedServer {
    constructor(port, address) {
        this.port = port;
        this.address = address;
    }
    ;
    startServer() {
        console.log(`Starting interfaced server @${this.address}:${this.port}`);
    }
    ;
    stopServer() {
        console.log(`Stoping interfaced server ... ${this.address}`);
    }
    ;
}
;
const someServer = new Server(8080, 'localhost');
someServer.startServer();
someServer.stopServer();
const iServer = new InterfacedServer(8090, 'localhost');
iServer.startServer();
iServer.stopServer();
