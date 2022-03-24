#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
 */

bool solution(const char *string, const char *ending)
{ 
    if(strlen(ending) > strlen(string)) return false;
    
    size_t j = 0;
    for(size_t i = strlen(string) - strlen(ending) ; i < strlen(string); i++)
    {
         if(string[i] != ending[j])  return false;
         j++;
    }  
    return true;
}

int main(int argc, char const *argv[])
{
    char * string = "abcdefg";
    char * ending = "g";
    bool confirm = solution(string,ending);
    printf("%d\n",confirm );
    return 0;
}