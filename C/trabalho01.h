#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
//#include <gtk/gtk.h> | Estava truncando todo o código, removi tudo do gtk

typedef struct user{
  char *name;
  int *rating;
} User;

User *generateUser(char *buffer, int nRatings);
//void setRate(User *a, int itemID, int rate);
int defineColumnsConstant(int value);
int getUserItemRate(User *target, int itemID);
//int *getUserRates(User *target);
int findAmmountOfRatesByUser(User *target, int nElements);
int hasEvaluatedItem(User *target, int itemID);
float calcUserAverageRate(User *target, int nElements);
float calcPearsonCorrelation(User *a, User *b, int nElements);
float predictRateByUser(User *a, int itemID, FILE *source);
float predictRateByItem();
