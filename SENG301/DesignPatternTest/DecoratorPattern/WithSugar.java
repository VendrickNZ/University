package DecoratorPattern;

public class WithSugar extends CoffeeDecorator {
    public WithSugar(Coffee c) {
        super(c);
    }

    @Override
    public double getCost() {
        return super.getCost() + 0.2;
    }

    @Override
    public String getIngredients() {
        return super.getIngredients() + ", Sugar";
    }
}