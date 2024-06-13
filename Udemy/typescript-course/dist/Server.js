var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { Comp1 as someComp } from '@components/Comp1';
class BaseServer {
    constructor(port, address) {
        this.comp = new someComp();
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
    getData() {
        return __awaiter(this, void 0, void 0, function* () {
            return 'data';
        });
    }
}
;
const someServer = new Server(8080, 'localhost');
someServer.startServer();
someServer.stopServer();
const iServer = new InterfacedServer(8090, 'localhost');
iServer.startServer();
iServer.getData().then(value => console.log(value), reason => console.log(reason));
iServer.stopServer();
