// It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
//  You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* remove_char(char* dst, const char* src)
{
   size_t j = 0;
  
   for(size_t i = 0 ; i <= strlen(src); i++)
   {        
     if(i != 0 && i != strlen(src) - 1 )
     {
       dst[j] = src[i];
       j++;
     }
   }
  return dst;
}

int main(int argc, char const *argv[])
{

	char * src = "johnny";
	char * dst = "#####";
	
    char* d = remove_char(dst,src);
	/* code */
	return 0;
}