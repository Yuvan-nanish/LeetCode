class Solution {
    public static void callPlusOne() {
        int[] digits = {1, 2, 3};
        int[] result = plusOne(digits); // Call the plusOne method
        System.out.print("Input: [1, 2, 3] | Result:  [");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) System.out.print(", ");
        }
        System.out.println("]");
    }

    public static int[] plusOne(int[] digits) {
        // Traverse the array from the end to the beginning
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++; // Increment the digit if it's less than 9
                return digits; // Return the updated array
            }
            digits[i] = 0; // Set to 0 if the digit is 9
        }

        // If all digits were 9, create a new array with an extra digit
        int[] newDigits = new int[digits.length + 1];
        newDigits[0] = 1; // The first digit will be 1, the rest are 0 by default
        return newDigits;
    }

    public static void main(String[] args) {
        callPlusOne(); // Example usage
    }
}
