#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.
**/

void high_and_low (const char *strnum, char *result)
{
  char * cpy = malloc((strlen(strnum) + 1)*sizeof(char));
  strcpy(cpy,strnum);
  char *token = strtok(cpy, " ");  
  
   int min = strtol(token,NULL,10) ,max = strtol(token,NULL,10);
  
   while( token != NULL )
   {  
      int num = strtol(token,NULL, 10);
      
      if(num < min) min = num;
      if(num > max) max = num;

      token = strtok(NULL, " ");
   }
  sprintf(result,"%d %d",max,min); 

  printf("%s\n",result );
}

int main(int argc, char const *argv[])
{
  char * nums = "1 2 3 4 53 -90 89 900 -90000";
  
  char result[128];

  high_and_low(nums,result);

  return 0;
}