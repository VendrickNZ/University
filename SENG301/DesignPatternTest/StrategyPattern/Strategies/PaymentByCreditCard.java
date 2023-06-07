package StrategyPattern.Strategies;

import StrategyPattern.PaymentStrategy;

public class PaymentByCreditCard implements PaymentStrategy {
    private String card;

    public void pay(int amount) {
        System.out.println("Paying with credit card...");
    }

    public void collectPaymentDetails() {
        card = "ahh monkey";
    }

    public boolean validatePaymentDetails() {
        return true;
    }
}
