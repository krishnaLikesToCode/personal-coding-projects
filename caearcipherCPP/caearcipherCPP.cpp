
#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
using namespace std;

int getNum(char val, vector<char> alphabet) {
	for (int j = 0; j < 26; j++) {
		if (val == alphabet[j]) { return j; }
		if (j == 26) { return -1; }

	}
}

vector<char> encryption(int key, string plain, vector<char> alphabet, string uInput) {
	int length = plain.length();
	vector<char> encryptedWord(length);
	for (int i = 0; i < length; i++) {
		int val = getNum(plain[i], alphabet);
		if (val == -1) { encryptedWord[i] = uInput[i]; continue; }
		int newVal = (val + key) % 26;
		for (int l = 0; l <= newVal; l++) {
			if (l == newVal) { encryptedWord[i] = alphabet[l]; }
		}
	
	}
	return encryptedWord;

}

int main()
{
	vector<char>alphabet = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v', 'w', 'x', 'y', 'z'};
	string uInput = "";
	cout << "Enter the plaintext, no spaces cause im stupid \t";
	getline(cin,uInput);
	string keyInput = "";
	cout << "Enter the key \t";
	getline(cin, keyInput);
	int key = stoi(keyInput);
	vector<char> encrypt= encryption(key, uInput, alphabet, uInput);
	int len = uInput.length();
	for (int i = 0; i < len; i++) {
		cout << encrypt[i];
	}

	return 0;
}
