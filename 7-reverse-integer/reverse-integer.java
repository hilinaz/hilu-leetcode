class Solution {
    public int reverse(int  x) {
    int temp;
     long rev=0;
    
        while  (x!=0){
        
temp=(int)x%10;
rev=rev*10+temp;
x=x /10;
        }
      if(rev<Integer.MIN_VALUE ||rev>Integer.MAX_VALUE)  {
        return 0;
      }
   else{
    return (int) rev; 
   }
       
    }
}