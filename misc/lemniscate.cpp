
//TODO: figure out why I coded this in the first place...
#include <iostream>
#include <stdio.h>
using namespace std;

int lemniscateCheck(int p) 
{
	int nSols = 0;
	//printf("Starting check for int %d-------------------\n", p);
	for (int i = 0; i < p; i++)
	for (int j = 0; j < p; j++){
		if ( ((i*i + j*j) *  (i*i + j*j)) % p == 
		          (p*p * p + (i*i - j*j)) % p) {
			//printf("%d, %d\n", i, j);
			nSols++;
		}
	}
	////printf("End of checking for int %d------------------\n", p);
	return nSols;
}

bool checkPrime(int n) 
{
	for (int i = 2; i * i <= n; i++) {
		if (n % i == 0)
			return false;
	}
	return true;
}

int primes[50000];
int nPrimes;
void genPrimes(int lim) 
{
	for (int i = 5; i <= lim; i++) {
		if (checkPrime(i)) {
			nPrimes++;
			primes[nPrimes] = i;
		}
	}
}

int main()
{
	//cout << lemniscateCheck(23);
	nPrimes = 2;
	primes[1] = 2;
	primes[2] = 3;

	genPrimes(600);
	for (int i = 1; i <= nPrimes; i++) {
		cout << primes[i] << " " << lemniscateCheck(primes[i]) << "\n";
	}
	cout << -1 % 3 << " " << -45 % 24 << "\n";
	return 0;
}
