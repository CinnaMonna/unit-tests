import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import seminars.third.hw.CheckNumberService;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class CheckNumberServiceTest {
    CheckNumberService service;
    @BeforeEach
    void setUp() {
        service = new CheckNumberService();
    }
    @ParameterizedTest
    @ValueSource(ints = {-10, 0, 8})
    void isEvenTrueTest(int number) {
        assertTrue(service.isEven(number));
    }
    @ParameterizedTest
    @ValueSource(ints = {-9, 7})
    void isEvenFalseTest(int number) {
        assertFalse(service.isEven(number));
    }

    @ParameterizedTest
    @ValueSource(ints = {25, 50, 100})
    void isInIntervalTest(int number){
        assertTrue(service.isInInterval(number));
    }
    @ParameterizedTest
    @ValueSource(ints = {0, 110})
    void isNotInIntervalTest(int number){
        assertFalse(service.isInInterval(number));
    }

}
