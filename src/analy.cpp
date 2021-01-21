#include <stdio.h>

int main(int argc, char *argv[]) {

  // Check number of args
  if( argc == 2) {
    // Check if the arg is a `.mio` file
    if(false) {
      return 1;
    } else {
      printf("\033[31mERROR: Use a correct file format\033[30m\n");
      return 0;
    }
  } else {
    printf("\033[31mUSAGE: analy <file>\033[0m\n");
    return 0;
  }

  return 0;
}