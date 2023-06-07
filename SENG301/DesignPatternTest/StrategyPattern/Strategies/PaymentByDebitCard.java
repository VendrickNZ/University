package StrategyPattern.Strategies;

import StrategyPattern.PaymentStrategy;

public class PaymentByDebitCard implements PaymentStrategy {

    String passcode; //just to differentiate from credit card

    public void pay(int amount) {
        System.out.println("Paying with debit card...");
    }

    public void collectPaymentDetails() {
        passcode = "...";
    }

    public boolean validatePaymentDetails() {
        return true;
    }
}
