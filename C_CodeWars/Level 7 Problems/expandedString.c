/**

**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *accum(const char *source)
{  
  size_t sourceLen = strlen(source), concatLen = ((sourceLen * (sourceLen + 1))/2) + (sourceLen - 1) + 1; 
  char * concat = malloc(concatLen*sizeof(char));
  
  size_t j = 0;
  for(size_t i = 0; i < sourceLen ; i++)
  {
    size_t count = 0;
    
    while(count < (i + 1))
    {    
      concat[j] = count == 0 ? toupper(source[i]) : tolower(source[i]);
      count++;
      j++;
    }

    if(i < sourceLen - 1)
    {
      concat[j] = '-';
      
      j++;
    }
  }

  concat[j] = '\0';
  return concat;
}

int main(int argc, char const *argv[])
{
  char * str = "kLoASsamdadDAD";
  
  printf("%s\n",accum(str));
  return 0;
}