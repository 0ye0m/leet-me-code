class Solution {
public:
    int mirrorDistance(int n) {
        int revNo = 0;
        int n1 = n;
        while(n1>0){
            int lastDig = n1%10;
            revNo = revNo*10 + lastDig;
            n1 = n1/10;
        }
        if((n-revNo) > 0){
            return (n - revNo);
        }else{
        return(-1)*(n-revNo);}

        return -1;
    }
};