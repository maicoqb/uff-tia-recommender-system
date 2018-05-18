#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
//#include <gtk/gtk.h> | Estava truncando todo o código, removi tudo do gtk

typedef struct user{
  char *name;
  float *rating;
} User;

User *generateUser(char *buffer, int nRatings);
int findAmmountOfRatesByUser(User *target, int nElements);
float calcUserAverageRate(User *target, int nElements);
float calcPearsonCorrelation(User *a, User *b, int nElements);
float predictRateByUser(User **array, int a_size, User *desired, int itemID, int nElements);
float predictRateByItem();
