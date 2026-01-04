
#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

std::vector<char> wrapForLength(int length, std::string wordToWrap) {
	std::vector<char> wrappedWord(length);
	for (int i = 0; i < length; i++) {
		wrappedWord[i] = wordToWrap[i % wordToWrap.size()];
	}
	return wrappedWord;
}



int cipher(char keyWordLetter, char plainLetter) {

	return 0;
}
int getNumberInAlphabet(char letter,const std::vector<char> alpha) {
	int i = 0;
	while (i < 26) {
		if (letter == alpha[i]) { return i; }
		i++;
	}
	return -1;

}
char getLetterInAlphabet(int num, const std::vector<char> alpha) {
	if (num == -1) {return '~'; }
	return alpha[num];
}

std::vector<int> joinAndEncrypt(std::vector<int> plain, std::vector<int> keyword)
{
	std::vector<int> NUMLIST(plain.size());

	for(int i = 0; i < plain.size(); i++) {
		if (plain[i] == -1) { NUMLIST[i] = -1; continue; }
		NUMLIST[i] = (keyword[i] + plain[i])%26;
	}
	
	return NUMLIST;
}


int main()
{
	std::vector<char> alphabet = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };

	std::string mainWord;
	printf("Enter your plaintext:\t");
	std::getline(std::cin, mainWord);
	std::vector<int> plainTextNumbersEncrypted(mainWord.size());//init list for plaintext numerical vals

	std::string tempKeyword;
	printf("Enter a keyword to encrypt with:\t");
	std::getline(std::cin, tempKeyword);//input container
	std::vector<int> keywordNumbersEncrypted(mainWord.size());//init list for keyword numerical vals
	std::vector<char> keyWordList= wrapForLength(mainWord.size(), tempKeyword);// wrap the keyword and store in char type list

	std::vector<int> encryptedNumbers(mainWord.size());

	std::vector<char> encrypt(mainWord.size());//init list for encrpyted vals
	int value;

	for (char& c : mainWord)
		c = std::tolower(c);
	for (char& c : tempKeyword)
		c = std::tolower(c);

	for (int i = 0; i < keywordNumbersEncrypted.size(); i++) {
		keywordNumbersEncrypted[i] = getNumberInAlphabet(keyWordList[i], alphabet);
	}
	for (int i = 0; i < plainTextNumbersEncrypted.size(); i++) {
		plainTextNumbersEncrypted[i] = getNumberInAlphabet(mainWord[i], alphabet);
	}
	encryptedNumbers = joinAndEncrypt(plainTextNumbersEncrypted, keywordNumbersEncrypted);
	for (int i = 0; i < keywordNumbersEncrypted.size(); i++) {
		if (encryptedNumbers[i] == -1) {
			encrypt[i] = mainWord[i];
			
		}
		else
			encrypt[i] = getLetterInAlphabet(encryptedNumbers[i], alphabet);
		std::cout << encrypt[i];

	}



	



	
	

}


