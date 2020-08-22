#include <stdio.h>

int main(void) {
  int i; //For the loop later on.

  for(i = 1; i < 101; i++){ //Loops through all numbers up to 100.
    if(i%3==0 && i%5==0){ //If it's a multiple of both
      printf("FizzBuzz\n"); //Output FizzBuzz.
    }
    else if(i%3==0 && i%5!=0){ //If it's a multiple of 3.
      printf("Fizz\n"); //Output Fizz.
    }
    else if(i%3!=0 && i%5==0){ //If it's a multiple of 5.
      printf("Buzz\n"); //Output Buzz.
    }
    else{
      printf("%d\n",i); //%d indicates integer value.
    }
  }
  return 0;
}

/*
Traditionally:
3&5 are used as multiples.
Numbers range from 1-100.
However I assigned these to variables to avoid hardcoding and give more freedom.

Ref: https://faq.cprogramming.com/cgi-bin/smartfaq.cgi?answer=1043372399&id=1043284385 
 */