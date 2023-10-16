package seminars.third.hw;

public class CheckNumberService {
    /**
     * является ли целое число, записанное в переменную n, чётным (true) либо нечётным (false)
     * @param number - число
     * @return boolean
     */
    public boolean isEven(int number) {
        return number % 2 == 0;
    }

    /**
     * проверяет, попадает ли переданное число в интервал (25;100)
     * и возвращает true, если попадает, и false, если нет
     * @param number - число
     * @return boolean
     */
    public boolean isInInterval(int number) {
        return number >= 25 && number <= 100;
    }
}

