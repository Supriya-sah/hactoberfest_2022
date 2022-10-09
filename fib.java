class Solution {
    public int fib(int n) {
        int [] dp = new int [31];
       if(n<=1)return n;
        
        if(dp[n]>0)return dp[n];
        
        dp[n]=fib(n-1)+fib(n-2);
        return dp[n];
    }
}
