

class Logger {
    private static _instance: Logger;

    private constructor() {}

    public static getInstance(): Logger {
        if (!this._instance) {
            this._instance = new Logger()
            return this._instance
        }       
        return this._instance

    }
    public log(text: string): void {
        console.log(text)
    }
}

const log1 = Logger.getInstance()
const log2 = Logger.getInstance()

log1.log('some text')
log2.log('log 2 text')
console.log(log1 === log2)