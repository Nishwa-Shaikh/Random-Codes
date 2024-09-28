#include<stdio.h>
int SUM(int, int); //Function Prototype
//function def:
int SUM(int x, int y){
    printf("The sum is: %d\n", x+y);
    return x+y;
}
int main(){
    //calling function
    SUM(2,3);
}