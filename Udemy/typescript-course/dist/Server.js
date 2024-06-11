"use strict";
class BaseServer {
    constructor(port, address) {
        this.port = port;
        this.address = address;
    }
    startServer() {
        console.log(`Starting server at: ${this.address}:${this.port}`);
    }
}
