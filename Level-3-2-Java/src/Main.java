import java.util.Arrays;

public class Main {

    public static void main(String args[]){

    }

    public static void answer(int[][] matrix){
        int[] probabilities = new int[matrix[0].length];
        int denominator = 0;


    }

    public static int[] recursiveCalculate(int[][] matrix, int[] probabilities, int denominator, int rowNum){
        if(isAllZero(matrix[rowNum])){
            int[] temp = new int[matrix[0].length+1];
            for(int i=0; i<matrix[0].length; i++){
                temp[i] = matrix[rowNum][i];
            }
            temp[temp.length-1] = denominator;

            return temp;
        }

        else{
            int scaleCurrent = getDenominator(matrix[rowNum]);
            int scalePrevious = denominator;
            denominator *= scaleCurrent;

            probabilities = scaleArray(probabilities, scaleCurrent);
            probabilities = elementWiseCombine(probabilities, scaleArray(matrix[rowNum], scalePrevious));

            int[] result = new int[matrix[0].length+1];
            for(int i=0; i<matrix[rowNum].length; i++){
                result[i] = matrix[rowNum][i];
            }
            result[result.length-1] = denominator;

            for(int i=0; i<matrix[rowNum].length; i++){
                if(matrix[rowNum][i] != 0) {
                    result = elemwiseCombWithCommonDenom(
                            recursiveCalculate(matrix, probabilities, denominator, i),
                            result);
                }
            }

            // Eliminating zero probability from the result
        }
    }

    public static boolean isAllZero(int[] array){
        for(int i=0; i<array.length; i++){
            if(array[i] != 0)
                return false;
        }
        return true;
    }

    public static int[] eliminateZeros(int[] array){
        int numZeros = 0;
        for(int i : array){
            if(i == 0)
                numZeros++;
        }

        int[] result = new int[array.length-numZeros];
        int resultIndex = 0;
        for(int i : array){
            if(i == 0) {
                result[resultIndex] = i;
            }
        }
        return result;
    }

    public static int getDenominator(int[] array){
        int denominator = 0;
        for(int i : array){
            denominator += i;
        }
        return denominator;
    }

    public static int getCommonDivisor(int[] occurances, int num){
        int result = occurances[0];
        for(int i=1; i<num; i++)
            result = commonDivisor(occurances[i], result);
        return result;
    }

    public static int commonDivisor(int a, int b){
        if(a == 0)
            return b;
        return commonDivisor(b%a, a);
    }

    public static int[] scaleArray(int[] array, int scale){
        for(int i=0; i<array.length; i++){
            array[i] *= scale;
        }
        return array;
    }

    public static int[] elementWiseCombine(int[] arrayA, int[] arrayB){
        // Need to make sure that two array have the same dimension
        int[] result = new int[arrayA.length];
        for(int i=0; i<arrayA.length; i++){
            result[i] = arrayA[i]+arrayB[i];
        }
        return result;
    }

    public static int[] elemwiseCombWithCommonDenom(int[] arrayA, int[] arrayB){
        arrayA = scaleArray(arrayA, arrayB[arrayB.length-1]);
        arrayB = scaleArray(arrayB, arrayA[arrayA.length-1]);

        int[] result = new int[arrayA.length];
        result = elementWiseCombine(arrayA, arrayB);
        result[result.length-1] = arrayA[arrayA.length-1]*arrayB[arrayB.length-1];

        return result;
    }
}
