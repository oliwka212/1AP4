/*
 * srednia.cpp
 
 */


#include <iostream>
using namespace std;
void pobierz0ceny(int tb[], int n) {
    int ocena = 0;
    for (int i=0; i<n; i++){
	cout<< "Podaj ocene:";
    cin>>ocena;
    
    while (n > 0);
    
    if(ocena > 0 && ocena < 7){
     tb[i]= ocena;
     i++;
     n--;
     
     
    }
  }      
}
float liczsrednia(int[], int n){
    int suma = 0;
    for (int i=0; i<n; i++){
    cout<<tb[i]<<"";
    suma= suma + tb[i];
    
    
    
    
   } 
    
    
    
}




void drukuj(int tb[], int n) {
    for (int i=0; i<n; i++){
    cout<<tb[i]<<"";
   } 
}






int main(int argc, char **argv){
{
    
    int n;
	
    cout<< "Podaj liczbe ocen:";
    cin>>n;
    int oceny[n];
    pobierz0ceny(oceny, n);
    drukuj(oceny,n);
    
   }
	return 0;
}
