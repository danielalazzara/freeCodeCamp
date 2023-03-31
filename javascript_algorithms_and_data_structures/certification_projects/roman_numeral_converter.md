# Roman Numeral Converter

Convert the given number into a roman numeral.

Roman numerals	Arabic numerals
M	1000
CM	900
D	500
CD	400
C	100
XC	90
L	50
XL	40
X	10
IX	9
V	5
IV	4
I	1

All roman numerals answers should be provided in upper-case.

```
function convertToRoman(num) {
  let conversion = {M:1000, CM:900, D:500, CD:400, C:100, XC:90, L:50, XL:40, X:10, IX:9, V:5, IV:4, I:1};
  let roman = "";
  let i = 0;

  for (i in conversion) {
    while ( num >= conversion[i] ) {
      roman += i;
      num -= conversion[i];
    }
  }
  return roman;
 }

convertToRoman(36);
```
