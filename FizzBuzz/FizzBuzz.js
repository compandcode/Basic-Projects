var i; //Declares the variable for the loop.
for(i = 0; i<101; i++){ //Loops through the numbers 0-100.
    if (i%3 == 0 & i%5 == 0){ //If it's a multiple of both:
        console.log("FizzBuzz") //Outputs "FizzBuzz"
    }
    else if (i%3 == 0 & i%5 !=0){ //If it's a multiple of 3:
        console.log("Fizz") //Output "Fizz".
    }
    else if (i%3 != 0 & i%5 ==0){ //If it's a multiple of 5:
        console.log("Buzz") //Output "Buzz"
    }
    else{
        console.log(i); //Otherwise output the number.
    }
}