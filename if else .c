# include <stdio.h>

int main(){

    int laps;

    printf("Enter number of laps:  ");
    scanf("%d" , &laps);

    float distance = laps * 10;
    printf("distance  = %f\n" , distance);

    if (distance >= 50){

        printf("Enough laps");

    } else{

        printf("Do more laps");

    }

    return 0;


}