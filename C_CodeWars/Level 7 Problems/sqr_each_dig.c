#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

unsigned long long square_digits (unsigned n)
{
  if(n <= 0) return 0;
  
  int digits = floor (log10 (n)) + 1, count = digits - 1;
  char * nums[digits];
  char * concat = malloc(((digits * 2) +1) *sizeof(char));
 
   while(n != 0)
    { 
     char * num = malloc(3*sizeof(char));
     
     sprintf(num,"%d",((n%10) * (n%10)));
     
     n/= 10;
     
     nums[count] = num;
     
     count--;
    
    }
  
  for(int i = 0; i < digits; i++)
       strcat(concat,nums[i]);
  
    return strtol(concat,NULL,10);
}

int main(int argc, char const *argv[])
{
  
  return 0;
}