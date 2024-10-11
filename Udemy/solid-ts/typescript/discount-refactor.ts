// regular - 10
// premium - 20
// gold  - 30

interface Customer {
    giveDiscount(): number;
    addLoyaltyPoints(amountSpent: number): number;
}
  
class RegularCustomer implements Customer {
    giveDiscount(): number {
        return 10;
    }
    addLoyaltyPoints(amountSpent: number): number {
        return amountSpent;
    }
}

class PremiumCustomer implements Customer {
    giveDiscount(): number {
        return 20;
    }
    addLoyaltyPoints(amountSpent: number): number {
        return amountSpent * 2;
    }
}

class GoldCustomer implements Customer {
    giveDiscount(): number {
        return 30;
    }
    addLoyaltyPoints(amountSpent: number): number {
        return amountSpent * 3;
    }
}

class Discount {
    giveDiscount(customer: Customer): number {
        return customer.giveDiscount();
    }
}

let premiumCustomer: PremiumCustomer = new PremiumCustomer();
let discount: Discount = new Discount();

let finalValue = discount.giveDiscount(premiumCustomer);
console.log(finalValue);

let goldCustomer: GoldCustomer = new GoldCustomer();
console.log(discount.giveDiscount(goldCustomer))