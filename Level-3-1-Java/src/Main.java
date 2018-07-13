import java.math.BigInteger;

public class Main {
    public static final BigInteger ZERO = new BigInteger("0");
    public static final BigInteger ONE = new BigInteger("1");
    public static final BigInteger TWO = new BigInteger("2");
    public static final BigInteger THREE = new BigInteger("3");

    public static void main(String args[]) {
        System.out.print(recursivePropagate(new BigInteger("15").toString(2)));
    }

    public static int recursivePropagate(String num) {
        BigInteger number = new BigInteger(num, 2);

        if(number.equals(ONE)){
            return 0;
        }

        else if(number.equals(THREE)){
            return 2;
        }

        else if(number.mod(TWO).equals(ZERO)){
            String result = num.substring(0, num.length()-1);
            return 1+recursivePropagate(result);
        }

        else if(num.charAt(num.length()-2) == '1'){
            String result = number.add(ONE).toString(2);
            return 1+recursivePropagate(result);
        }

        else{
            String result = number.subtract(ONE).toString(2);
            return 1+recursivePropagate(result);
        }
    }
}
