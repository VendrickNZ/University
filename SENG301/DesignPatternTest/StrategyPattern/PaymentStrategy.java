package StrategyPattern;

public interface PaymentStrategy {
    void collectPaymentDetails();
    void pay(int amount);

    boolean validatePaymentDetails();
}
