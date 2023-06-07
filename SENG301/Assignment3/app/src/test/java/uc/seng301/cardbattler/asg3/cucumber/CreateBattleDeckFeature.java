package uc.seng301.cardbattler.asg3.cucumber;

import io.cucumber.cienvironment.internal.com.eclipsesource.json.JsonArray;
import io.cucumber.cienvironment.internal.com.eclipsesource.json.JsonObject;
import io.cucumber.java.Before;
import io.cucumber.java.en.And;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.core.util.Assert;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;
import org.mockito.Mockito;
import uc.seng301.cardbattler.asg3.accessor.DeckAccessor;
import uc.seng301.cardbattler.asg3.accessor.PlayerAccessor;
import uc.seng301.cardbattler.asg3.cards.CardService;
import uc.seng301.cardbattler.asg3.cards.CardType;
import uc.seng301.cardbattler.asg3.cli.CommandLineInterface;
import uc.seng301.cardbattler.asg3.game.Game;
import uc.seng301.cardbattler.asg3.model.*;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.logging.Level;
import java.util.stream.Collectors;

public class CreateBattleDeckFeature {

    private static Logger logger = LogManager.getLogger(CreateBattleDeckFeature.class);
    private SessionFactory sessionFactory;
    private PlayerAccessor playerAccessor;
    private DeckAccessor deckAccessor;
    private CardService cardGeneratorSpy;
    private static final Logger LOGGER = LogManager.getLogger(CreateBattleDeckFeature.class);


    private Player player;
    private Card card;
    private Deck deck;

    private Game game;
    private CommandLineInterface cli;

    @Before
    public void setup() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
        deckAccessor = new DeckAccessor(sessionFactory);
        cardGeneratorSpy = Mockito.spy(new CardService());
        cli = Mockito.mock(CommandLineInterface.class);

        Mockito.doAnswer((i) -> {
            System.out.println((String) i.getArgument(0));
            return null;
        }).when(cli).printLine(Mockito.anyString());

        game = new Game(cardGeneratorSpy, cli, sessionFactory);
    }

    private void addInputMocking(String... mockedInputs) {
        Iterator<String> toMock = Arrays.asList(mockedInputs).iterator();
        Mockito.when(cli.getNextLine()).thenAnswer(i -> toMock.next());
    }

    @Given("The player {string} exists")
    public void the_player_exists(String playerName) {
        player = playerAccessor.createPlayer(playerName);
        Long playerId = playerAccessor.persistPlayer(player);
        Assertions.assertNotNull(player);
        Assertions.assertNotNull(playerId);
        Assertions.assertSame(playerName, player.getName());
    }

    @And("There is no deck named {string}")
    public void there_is_no_deck_named(String deckName) {
        deck = deckAccessor.getDeckByName(deckName);
        Assertions.assertNull(deck);
    }

    @When("I create a battle deck named {string}")
    public void i_create_a_battle_deck_named(String deckName) {
        Mockito.doReturn(null).when(cardGeneratorSpy).getResponseFromAPI(Mockito.any());

        addInputMocking("random");
        game.battleDeck("battle_deck " + player.getName() + " " + deckName);
        deck = deckAccessor.getDeckByName(deckName);
    }

    @When("I create a battle deck named {string} with {int} monsters, {int} spells and {int} traps")
    public void i_create_a_battle_deck_named_with_monsters_spells_and_traps(String deckName, Integer numMonsters, Integer numSpells, Integer numTraps) {
        Mockito.doReturn(null).when(cardGeneratorSpy).getResponseFromAPI(Mockito.any());

        addInputMocking("choice", Integer.toString(numMonsters), Integer.toString(numSpells),
                Integer.toString(numTraps));
        game.battleDeck("battle_deck " + player.getName() + " " + deckName);
        deck = deckAccessor.getDeckByName(deckName);
        Assertions.assertNotNull(deck);
    }

    @Then("The battle deck must contain 20 cards exactly")
    public void the_battle_deck_must_contain_20_cards_exactly() {
        Assertions.assertEquals(20, deck.getCards().size());
    }

    @Then("The battle deck contains at least {int} monsters")
    public void the_battle_deck_contains_at_least_monsters(int minMonsters) {
        long numMonsters = deck.getCards().stream().filter(c -> c instanceof Monster).count();
        Assertions.assertTrue(numMonsters >= minMonsters);
    }

    @And("The battle deck contains at least {int} spells")
    public void the_battle_deck_contains_at_least_spells(int minSpells) {
        long numSpells = deck.getCards().stream().filter(c -> c instanceof Spell).count();
        Assertions.assertTrue(numSpells >= minSpells);
    }

    @And("The battle deck contains at least {int} traps")
    public void the_battle_deck_contains_at_least_traps(int minTraps) {
        long numTraps = deck.getCards().stream().filter(c -> c instanceof Trap).count();
        Assertions.assertTrue(numTraps >= minTraps);
    }

}
