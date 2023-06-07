package StrategyPattern;

public class CreditCard {
    private int amount = 1000;
    private final String number;
    private final String date;

    private final String cvv;

    public CreditCard(int amount, String number, String date, String cvv) {
        this.amount = amount;
        this.number = number;
        this.date = date;
        this.cvv = cvv;
    }

    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public String getNumber() {
        return number;
    }

}
