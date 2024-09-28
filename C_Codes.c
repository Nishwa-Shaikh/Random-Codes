// #include<stdio.h>
// int main(){
//     int Height;
//     int Width;
//     printf("Enter height:");
//     scanf("%d", &Height);
//     printf("Enter width:");
//     scanf("%d", &Width);
//     int Area=Height*Width;
//     printf("The area is: %d", Area);
//     return 0;
// }

// #include<stdio.h>
// int main(){
//     int num;
//     printf("Enter number: ");
//     scanf("%d", &num);
//     if(num%97==0){
//         printf("%d is divisible by 97", num);
//     }
//     else{
//         printf("%d is not divisible by 97", num);
//     }
// }

//To find if a character entered by user is Uppercase or lowercase

// #include<stdio.h>
// #include<ctype.h>
// int main(){
//     char CHAR;
//     printf("Please enter any character: ");
//     scanf("%c", &CHAR);
//     if(islower(CHAR)){
//         printf("%c is lower", CHAR);
//     }
//     else if(isupper(CHAR)){
//         printf("%c is capital", CHAR);
//     }
//     else{
//         printf("Please enter any letter");
//     }
//     return 0;
// }

//Finding greatest number:

// #include<stdio.h>
// int main(){
//     int num1, num2, num3, num4;
//     printf("Enter num1: ");
//     scanf("%d", &num1);
//     printf("Enter num2: ");
//     scanf("%d", &num2);
//     printf("Enter num3: ");
//     scanf("%d", &num3);
//     printf("Enter num4: ");
//     scanf("%d", &num4);
//     if (num1>num2 && num1>num3 && num1>num4){
//         printf("%d is greatest", num1);
//     }
//     else if(num2>num1 && num2>num3 && num2>num4){
//         printf("%d is greatest", num2);
//     }
//     else if(num3>num1 && num3>num2 && num3>num4){
//         printf("%d is greatest", num3);
//     }
//     else if(num4>num1 && num4>num2 && num4>num3){
//         printf("%d is greatest", num4);
//     }
//     else{
//         printf("Please enter any number");
//     }
// }

//Multiplication table

// #include<stdio.h>
// int main(){
//     int num;
//     printf("Enter any number: ");
//     scanf("%d", &num);
//     for (int i=1; i<=10; i++){
//         int result=(i*num);
//         printf("%d * %d = %d\n", num, i, result);
//     }
// }

//Multiplication table in revese order

// #include<stdio.h>
// int main(){
//     int num;
//     printf("Enter any number: ");
//     scanf("%d", &num);
//     for (int i=10; i>=1; i--){
//         int result=(i*num);
//         printf("%d * %d = %d\n", num, i, result);
//     }
// }

//sum of first 10 natural numbers by while loop

// #include <stdio.h>
// int main(){
//     int num=0;
//     int i=1;
//     while(i<=10){
//         num+=i;
//         i++;
//     }
//     printf("%d is sum of first 10 natural numbers", num);
//     return 0;
// }

//sum of first 10 natural numbers by do-while loop

// #include<stdio.h>
// int main(){
//     int sum=0;
//     int i=1;
//     do{
//         sum+=i;
//         i++;
//     }
//     while(i<=10);
//     printf("%d", sum);
//     return 0;
// }

//Print sum of all answers that come in table.
// #include <stdio.h>
// int main(){
//     int SUM=0;
//     int num;
//     printf("Please enter number: ");
//     scanf("%d", &num);
//     for (int i=1; i<=10; i++){
//         int result=i*num;
//         SUM+=result;
//     }
//     printf("%d", SUM);
//     return 0;
// }

//Find Average of 3 numbers using Functions (Inputs by default)
// #include<stdio.h>
// int Average(int, int, int);
// int Average(int a, int b, int c){
//     int result= (a+b+c)/3;
//     return result;
// }
// int main(){
//     int avg=Average(2,2,2);
//     printf("%d", avg);
//     return 0;
// }

//Finding average by user inputs
#include<stdio.h>
int Average();
int Average(){
    int Arr[3];
    int SUM=0;
    for (int i=0; i<=2; i++){
        printf("Enter number: ", i+1);
        scanf("%d", &Arr[i]);
        SUM+=Arr[i];
    }
    return SUM/3;
}
int main(){
    int avg=Average();
    printf("the average is: %d\n", avg);
    return 0;
}