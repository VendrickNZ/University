package StrategyPattern.Strategies;

import StrategyPattern.PaymentStrategy;

public class PaymentByPayPal implements PaymentStrategy {
    private String email;
    private String password;
    @Override
    public void collectPaymentDetails() {
        email = "...";
        password = "...";
    }

    @Override
    public void pay(int amount) {
        System.out.println("Paying with PayPal...");
    }

    @Override
    public boolean validatePaymentDetails() {
        return true;
    }
}
