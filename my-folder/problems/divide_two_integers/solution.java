class Solution {

    private static int HALF_INT_MIN = -1073741824;
    public int divide(int dividend, int divisor) {
        if (dividend==Integer.MIN_VALUE && divisor==-1){
            return Integer.MAX_VALUE;
        }
        int negatives=2;
        if (dividend>0){
            negatives--;
            dividend =-dividend;
        }
        if (divisor>0){
            negatives--;
            divisor=-divisor;
        }
        int out=0;
        while (divisor >= dividend){
            int powertwo=-1;
            int value = divisor;
            while ( value > HALF_INT_MIN && value + value >= dividend ){
                value+=value;
                powertwo+=powertwo;
            }
            out+=powertwo;
            dividend-=value;
        }
        if (negatives!=1){
            return -out;
        }
        return out;

    }
}