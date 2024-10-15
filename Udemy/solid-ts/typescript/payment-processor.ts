

abstract class  PaymentMethod {
    abstract processPayment(amount: number): string
}

class CreditCard extends PaymentMethod {
    processPayment(amount: number): string {
        // implement logic
        return 'Credit card accepted';
    }
}

class DebitCard extends PaymentMethod {
    processPayment(amount: number): string {
        // implement logic
        return 'Debit card accepted'
    }
}

class Paypal extends PaymentMethod {
    processPayment(amount: number): string {
        // implement logic
        return 'Paypal accepted'
    }
}

/// client
function paymentProcessor(
    paymentMethod: PaymentMethod,
    amount: number
): string {
    return paymentMethod.processPayment(amount)
}

const methods = [new CreditCard(), new DebitCard, new Paypal()]
methods.forEach((method) => {
    console.log(paymentProcessor(method, 5))
})

