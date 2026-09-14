# include <stdio.h>

int main(){

    int radius;

    # define PI 3.142

    printf("Enter radius: ");


    scanf("%d" , &radius);


    float area = PI * radius * radius;


    printf("area = \n %f" , area);

    float perimeter = 2 * PI * radius * radius ;


    printf("perimeter = \n %f" , perimeter);


    return 0;


}