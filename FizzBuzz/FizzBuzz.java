import java.util.Scanner;

public class FizzBuzz {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in); //Constructs a scanner object.
        System.out.println("Enter the lowest number to be included in this Fizz Buzz program:");
        int lowestValue = scanner.nextInt(); //Stores the input in the variable.
        System.out.println("Enter the highest number to be included in this Fizz Buzz program:");
        int highestValue = scanner.nextInt(); //Stores the input in the variable.
        highestValue += 1; //Increments to ensure it's the same as the input.
        System.out.println("Enter the first multiple to indicate Fizz/Buzz/FizzBuzz:");
        int multipleOne = scanner.nextInt();
        System.out.println("Enter the second multiple to indicate Fizz/Buzz/FizzBuzz:");
        int multipleTwo = scanner.nextInt();

        for (int i = lowestValue; i < highestValue; i++) { //Loops through numbers from lowest value to highest value.
            if (i%multipleOne == 0 & i%multipleTwo == 0) { //If the number is a multiple of multipleOne and multipleTwo:
                System.out.println("Fizz Buzz"); //Return "Fizz Buzz".
            }
            else if (i%multipleOne == 0 & i%multipleTwo!=0){ //Otherwise if the number is a multiple of multipleOne but NOT multipleTwo:
                System.out.println("Fizz"); //Return "Fizz"
            }
            else if (i%multipleOne != 0 & i%multipleTwo==0){ //Otherwise if the number is only a multiple of multipleTwo
                System.out.println("Buzz"); //Output buzz
            }
            else{
                System.out.println(i); //Otherwise output the number.
            }
        }
    }
}
/*
Traditionally:
3&5 are used as multiples.
Numbers range from 1-100.
However I assigned these to variables to avoid hardcoding and give more freedom.
 */