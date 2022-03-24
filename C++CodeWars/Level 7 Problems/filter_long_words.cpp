
#include <vector>
#include <string>
#include <iostream>
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
  
  //create two variables: one that holds the number of characters in the original string
  //create one that stores the length of the original string
  int count = 0, end = sentence.length() - 1;
  
  //loop through each character in the sentence
  //make sure to declare the character 'c' as a reference so as to not work with the copy of each character
  //and since we don't intend on modyifing each character in the original string
  //make sure to declare the character 'c' as a constant reference.
  for (const auto & c : sentence)
  {

    //if the character is a space
    if(isspace(c))
    {
      //if the new string that we've been building in the past few iterations
      //is bigger than whatever n is. Add it to the vector.
      if(word.length() > n ) filtered.push_back(word);
      
      //clear the word for reuse
      word.clear();
    }
    
    //if the character isn't a space
    else
    { 
      //add the character to the new string
      word+=c;

      //if it turns out that the we are at the end of the orignal string
      //and the length of the newly built string is greater than n
      //add the new string to the vector.
      if(count == end && word.length() > n ) filtered.push_back(word);
    }
    
    count++;
  }
  
  return filtered;
}

int main()
{
  std::string sentence = "ich habe hunger heute und ich möchte heute Morgen in Berlin wandern ";

	std::vector<std::string> filtered_words = filter_long_words(sentence,5);

  for(const auto & word : filtered_words)
    std::cout << word << std::endl;
	return 0;
}