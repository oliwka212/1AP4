/*
 * kalkulator.cpp
 */


#include <iostream>
using namespace std;

void dodaj(){
    int a, b;
    cout << "Podaj dwie liczby"  << endl;
    cin>> a>>b;
    cout<< "suma: "  <<a + b << endl;
    
}
void różnica(){
    int a, b;
    cout << "Podaj dwie liczby"  << endl;
    cin>> a>>b;
    cout<< "różnica: "  <<a - b << endl;
    
}
int main(int argc, char **argv)
{
	char operacja;
    cout << "Jakie działanie chce wykonać(+, -, *, /)?" << endl;
    cin >> operacja;
    switch(operacja) {
        case'+':
            dodaj();
        break;
        case '-':
        odejmij():
        break;
        default:
            cout<< "I don't know" << endl;
        break; 
    }
	return 0;
}

