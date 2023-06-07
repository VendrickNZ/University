package StrategyPattern;

import StrategyPattern.Strategies.PaymentByCreditCard;
import StrategyPattern.Strategies.PaymentByDebitCard;
import StrategyPattern.Strategies.PaymentByPayPal;

public class main {
    public static void main(String[] args) {
        PaymentService paymentService = new PaymentService();
        paymentService.setStrategy(new PaymentByDebitCard());
        paymentService.processOrder();
        paymentService.setStrategy(new PaymentByPayPal());
        paymentService.processOrder();
        paymentService.setStrategy(new PaymentByCreditCard());
        paymentService.processOrder();
    }
}


