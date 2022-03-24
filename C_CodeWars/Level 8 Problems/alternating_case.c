
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char * to_alternating_case(const char * s);

char *to_alternating_case(const char *s) {
  
  //create a new pointer to char
  char * str = malloc((strlen(s) + 1) * sizeof(char));
  
  //start a counter
  int count = 0;
  
  //loop through each character in the string until we reach the null terminator
  while(*s != '\0')
  {
     //if the current character is uppercase, take that character, lowercase it and store it in the new char array
     if(isupper(*s)) str[count] = tolower(*s);

     //if the current character isn't uppercase, take that character, uppercase it and store it in the new char array
     else str[count] = toupper(*s);

     count++;

     //move on to the new character
     s++; 
  }  
   
   //add the null terminator
  str[count] = '\0';
    
  return str; 
}

int main(int argc, char const *argv[])
{
  const char * s = "tHis is A HIGh WaY SO pLeAsE aVoId ThIS aReA";

  char * str = to_alternating_case(s);

   printf("Original String: %s\n", s);

   printf("Alternating String: %s\n", str);
   
  return 0;
}