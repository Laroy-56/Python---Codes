# include <stdio.h>

int main() {

    int age;

    printf("Enter age:  ");

    scanf("%d" , &age);

    if (age >= 18){

        printf("ADULT");


    } else {

        printf("MINOR");


    }

      return 0;
}