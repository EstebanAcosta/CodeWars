#include <string>
#include <iostream>
#include <cctype>

std::string solve(const std::string & eq)
{
  std::string rev;
  int end = eq.length();
  
  for(int i = end; i >= 0 ; i--)
  {
    if(isalpha(eq[i]) || ispunct(eq[i])) rev+=eq[i];
    else 
    {      
            std::string num;
      
            while(isdigit(eq[i]))
            {
              num = eq[i] + num;
              i--;
            }
            
            rev+=num;
              
            if(i >= 0) rev+=eq[i];
    }
  }

  return rev;
  
}


int main()
{

  return 0;
}