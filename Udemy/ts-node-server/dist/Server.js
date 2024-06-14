"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Server = void 0;
const http_1 = require("http");
class Server {
    startServer() {
        (0, http_1.createServer)((req, res) => {
            console.log(`Got request from ${req.headers['user-agent']} for ${req.url}`);
            res.write('Hello from TS server');
            res.end();
        }).listen(8080);
        console.log('server started');
    }
}
exports.Server = Server;
//# sourceMappingURL=Server.js.map