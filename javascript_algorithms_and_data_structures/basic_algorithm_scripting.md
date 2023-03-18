# Convert Celsius to Fahrenheit

The formula to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.

You are given a variable celsius representing a temperature in Celsius. Use the variable fahrenheit already defined and assign it the Fahrenheit temperature equivalent to the given Celsius temperature. Use the formula mentioned above to help convert the Celsius temperature to Fahrenheit.

```
function convertCtoF(celsius) {
  let fahrenheit = celsius * 9 / 5 + 32;
  return fahrenheit;
}

convertCtoF(30);
```

# Reverse a String

Reverse the provided string and return the reversed string.

For example, "hello" should become "olleh".

```
function reverseString(str) {
  return str.split("").reverse().join("");
}

reverseString("hello");
```

# Factorialize a Number

Return the factorial of the provided integer.

If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.

Factorials are often represented with the shorthand notation ```n```!

For example: ```5! = 1 * 2 * 3 * 4 * 5 = 120```

Only integers greater than or equal to zero will be supplied to the function.

```
function factorialize(num) {
  let product = 1;
  for (let i = 2; i <= num; i++) {
    product *= i;
  }
  return product;
}

factorialize(5);
```

# Find the Longest Word in a String

Return the length of the longest word in the provided sentence.

Your response should be a number.

```
function findLongestWordLength(str) {
  let words = str.split(" ");
  let maxLength = 0;

  for (let i = 0; i < words.length; i++) {
    if (words[i].length > maxLength) {
      maxLength = words[i].length;
    }
  }
  return maxLength;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");
```

# Return Largest Numbers in Arrays

Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays.

Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].

```
function largestOfFour(arr) {
  let num = [] 
  for (let i = 0; i < arr.length; i++) {
    num[i] = Math.max.apply(null, arr[i]); 
  }
  return num;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

# Confirm the Ending

Check if a string (first argument, str) ends with the given target string (second argument, target).

This challenge can be solved with the .endsWith() method, which was introduced in ES2015. But for the purpose of this challenge, we would like you to use one of the JavaScript substring methods instead.

```
function confirmEnding(str, target) {
  return str.slice(str.length - target.length) === target;
}

confirmEnding("Bastian", "n");
```

# Repeat a String Repeat a String

Repeat a given string str (first argument) for num times (second argument). Return an empty string if num is not a positive number. For the purpose of this challenge, do not use the built-in ```.repeat()``` method.

```
function repeatStringNumTimes(str, num) {
  if (num <=0) {
    return ""
  } else {
    return str + repeatStringNumTimes(str, num - 1);
  }
}

repeatStringNumTimes("abc", 3);
```

# Truncate a String

Truncate a string (first argument) if it is longer than the given maximum string length (second argument). Return the truncated string with a ... ending.

```
function truncateString(str, num) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}

truncateString("A-tisket a-tasket A green and yellow basket", 8);
```

# Finders Keepers

Create a function that looks through an array arr and returns the first element in it that passes a 'truth test'. This means that given an element x, the 'truth test' is passed if func(x) is true. If no element passes the test, return undefined.

```
function findElement(arr, func) {
  let num = 0;

  for (let i = 0; i < arr.length; i++) {
    num = arr[i];
    if (func(num)) {
      return num;
    }
  } 
}

findElement([1, 2, 3, 4], num => num % 2 === 0);
```

# Boo who

Check if a value is classified as a boolean primitive. Return true or false.

Boolean primitives are true and false.

```
function booWho(bool) {
  if (bool === true | bool === false) {
    return true; 
  } else {
    return false;
  }
}

booWho(null);
```

# Title Case a Sentence

Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

For the purpose of this exercise, you should also capitalize connecting words like the and of.

```
function titleCase(str) {
  const newString = str.split(" ");
  const updatedString = [];
  for (let s in newString) {
    updatedString[s] = newString[s][0].toUpperCase() + newString[s].slice(1).toLowerCase();
  }
  return updatedString.join(" ");
}

titleCase("I'm a little tea pot");
```

# Slice and Splice

You are given two arrays and an index.

Copy each element of the first array into the second array, in order.

Begin inserting elements at index n of the second array.

Return the resulting array. The input arrays should remain the same after the function runs.

```
function frankenSplice(arr1, arr2, n) {
  let arrTwo = arr2.slice();
  for (let i= 0; i <arr1.length; i++) {
    arrTwo.splice(n, 0, arr1[i]);
    n++;
  }
  return arrTwo;
}

frankenSplice([1, 2, 3], [4, 5, 6], 1);
```

# Falsy Bouncer

Remove all falsy values from an array. Return a new array; do not mutate the original array.

Falsy values in JavaScript are false, null, 0, "", undefined, and NaN.

Hint: Try converting each value to a Boolean.

```
function bouncer(arr) {
  let newArr = [];
  for (let i= 0; i <arr.length; i++) {
    if (arr[i]) newArr.push(arr[i]);
  }
  return newArr;
}

bouncer([7, "ate", "", false, 9]);
```

# Where do I Belong

Return the lowest index at which a value (second argument) should be inserted into an array (first argument) once it has been sorted. The returned value should be a number.

For example, ```getIndexToIns([1,2,3,4], 1.5)``` should return ```1``` because it is greater than 1 (index 0), but less than 2 (index 1).

Likewise, ```getIndexToIns([20,3,5], 19)``` should return ```2``` because once the array has been sorted it will look like ```[3,5,20]``` and ```19``` is less than 20 (index 2) and greater than 5 (index 1).

```

function getIndexToIns(arr, num) {
  arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= num) {
      return i;
    }
  }
  return arr.length;
}
```

# Mutations

Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array.

For example, ["hello", "Hello"], should return true because all of the letters in the second string are present in the first, ignoring case.

The arguments ["hello", "hey"] should return false because the string hello does not contain a y.

Lastly, ["Alien", "line"], should return true because all of the letters in line are present in Alien.

```
function mutation(arr) {
  let a = arr[1].toLowerCase();
  let b = arr[0].toLowerCase();
  for (let i = 0; i< a.length; i++) {
    if (b.indexOf(a[i]) < 0) {
      return false;
    }
  }
  return true;
}

mutation(["hello", "hey"]);
```

# Chunky Monkey

Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.

```
function chunkArrayInGroups(arr, size) {
  let newArr = [];
  for (let i = 0; i < arr.length; i+= size) {
    newArr.push(arr.slice(i, i + size));
  }
  return newArr;
}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
```
