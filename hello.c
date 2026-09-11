# include <stdio.h>

int main () {

    int age ;

    printf("Enter age: ");

    scanf("%d" , &age);

    if (age >= 18) {

        printf("Adult");

    } else {

        printf("Minor");


    }

     return 0;
}