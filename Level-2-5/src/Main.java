public class Main {
    public static int[] answer(int[] l, int t){
        return consecutiveForward(l ,t);
    }

    public static int[] consecutiveForward(int[] list, int target){
        for(int pos=0; pos<list.length; pos++) {
            // Loop for increasing length at current position
            for (int j = 1; j < list.length-pos+1; j++) {
                int segmentSum = 0;

                for (int i = pos; i < pos + j; i++) {
                    segmentSum += list[i];
                }

                if (segmentSum == target) {
                    // Start position and the length for the segment
                    return new int[]{pos, pos+j-1};
                }
            }
        }
        return new int[]{-1,-1};
    }

    public static void main(String args[]){
        int[] a = new int[]{4, 3, 5, 7, 8};
        int t = 12;

        int[] temp = consecutiveForward(a, t);
        for(int i=0; i<temp.length; i++){
            System.out.print(temp[i] + ",");
        }
    }
}
