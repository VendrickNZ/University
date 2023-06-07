package DecoratorPattern;

public class Main {
    public static void main(String[] args) {
        Coffee c = new SimpleCoffee();
        System.out.println("Cost: " + c.getCost() + "; Ingredients: " + c.getIngredients());

        c = new WithMilk(c);
        System.out.println("Cost: " + c.getCost() + "; Ingredients: " + c.getIngredients());

        c = new WithSugar(c);
        System.out.println("Cost: " + c.getCost() + "; Ingredients: " + c.getIngredients());
    }
}
