public class Ver2Failed {
    public static void main(String args[]){
        int[][] temp = new int[6][6];
        temp[0] = new int[]{0,1,0,0,0,1};
        temp[1] = new int[]{4,0,0,3,2,0};
        temp[2] = new int[]{0,0,0,0,0,0};
        temp[3] = new int[]{0,0,0,0,0,0};
        temp[4] = new int[]{0,0,0,0,0,0};
        temp[5] = new int[]{0,0,0,0,0,0};

        int[] result = answer(temp);
        for(int i=0; i<result.length; i++){
            System.out.print(result[i] + ",");
        }
    }

    public static int[] answer(int[][] matrix){
        int[][] probabilities = new int[matrix[0].length][matrix[0].length];
        for(int i=0; i<probabilities.length; i++){
            for(int j=0; j<probabilities.length; j++)
                probabilities[i][j] = 1;
        }
        int[][] result = recursiveCalculate(matrix, probabilities, 0);

        int[] finalResult = new int[result[0].length+1];
        for(int i=0; i<result[0].length; i++){
            finalResult[i] = result[0][i];
        }
        finalResult[finalResult.length-1] = result[1][1];

        return finalResult;
    }

    private static int[][] recursiveCalculate(int[][] matrix, int[][] probabilities, int rowNum){
        if(isAllZero(matrix[rowNum])){
            return probabilities;
        }
        else{
            for(int i=0; i<matrix[rowNum].length; i++){
                int denominator = sumArray(matrix[rowNum]);
                int base = probabilities[1][1]*denominator;

                for(int j=0; j<probabilities[1].length; j++){
                    probabilities[1][j] = base;
                }

                if(matrix[rowNum][i] != 0){
                    probabilities[0][i] *= matrix[rowNum][i];
                    probabilities[0] = elementWiseCombine(probabilities[0], recursiveCalculate(matrix, probabilities, i)[0]);
                }
            }

            return probabilities;
        }
    }

    private static boolean isAllZero(int[] array){
        for(int i : array){
            if(i != 0)
                return false;
        }
        return true;
    }

    private static int[] elementWiseCombine(int[] arrayA, int[] arrayB){
        // Need to make sure that two array have the same dimension
        int[] result = new int[arrayA.length];
        for (int i = 0; i < arrayA.length; i++) {
            result[i] = arrayA[i] + arrayB[i];
        }
        return result;
    }

    private static void commonDenominator(int[][] array){
        int denominator = getCommonDivisor(array[1], array[1].length);

        for(int i=0; i<array[0].length; i++){
            int scale = denominator/array[1][i];
            array[0][i] *= scale;
        }
    }

    private static int getCommonDivisor(int[] occurances, int num){
        int result = occurances[0];
        for(int i=1; i<num; i++)
            result = commonDivisor(occurances[i], result);
        return result;
    }

    private static int commonDivisor(int a, int b){
        if(a == 0)
            return b;
        return commonDivisor(b%a, a);
    }

    private static void scaleArray(int[] array, int scale, String operation){
        if(operation.equals("down")) {
            for (int i = 0; i < array.length; i++) {
                array[i] *= scale;
            }
        }
        else if (operation.equals("up")){
            for (int i = 0; i < array.length; i++) {
                array[i] /= scale;
            }
        }
    }

    public static int sumArray(int[] array){
        int denominator = 0;
        for(int i : array){
            denominator += i;
        }
        return denominator;
    }
}
