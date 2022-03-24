
#include <vector>
#include <string>


/***
 * 
 * 
 * Write a function that takes a string and an an integer n as parameters and returns a list of all words that are longer than n.
 * 
 */

#include <vector>
#include <string>
#include <cctype>

std::vector<std::string> filter_long_words(const std::string& sentence, int n) {
  
  std::vector<std::string> filtered;
  std::string word;
  
  int count = 0, end = sentence.length() - 1;
  
  for (const auto & c : sentence)
  {

    if(isspace(c))
    {
      if(word.length() > n ) filtered.push_back(word);
      
      word.clear();
    }
    
    else
    { 
      word+=c;
      if(count == end && word.length() > n ) filtered.push_back(word);
    }
    
    count++;
  }
  
  return filtered;
}

int main()
{
  std::string sentence = "a dog told me once that I was not a man";
  
	filter_long_words(sentence,3);
	return 0;
}