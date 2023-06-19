# Eminds
Question
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.Examples:

strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
Concatenate the consecutive strings of strarr by 2, we get:
treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".
In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return “” (return Nothing in Elm, “nothing” in Erlang).

Test cases:

1.z=0 ; None

2.z<0 ; None

3.z=1 ; abigail, largest length element in given array

4.arr empty array None

5.arr=["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], z = 2 ; folingtrashy

6.arr=["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], z=2 ; abigailtheta

