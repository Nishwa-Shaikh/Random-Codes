#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    srand(time(0));
    int random = rand() % 100;
    int guess;
    printf("You have 5 chances\n");
    for (int i = 0; i <= 4; i++)
    {
        printf("Enter your guess: ");

        if (scanf("%d", &guess) != 1)
        {
            while (getchar() != '\n');
            printf("Please enter a valid integer.\n");
            i--; // Don't count this as a valid attempt
            continue;
        }
        else if (guess > random)
        {
            printf("Guess is high\n");
        }
        else if (guess < random)
        {
            printf("Guess is low\n");
        }
        else if (guess == random)
        {
            printf("%d is the correct answer:)", guess);
            break;
        }
        if (i == 4 && guess != random)
        {
            printf("No more chances left:(\nBetter luck next time:)");
        }
    }
}