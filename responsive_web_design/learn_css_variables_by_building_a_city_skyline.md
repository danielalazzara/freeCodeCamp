<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Table of Contents</summary>

- [Step 1](#step-1)
- [Step 2](#step-2)
- [Step 3](#step-3)
- [Step 4](#step-4)
- [Step 5](#step-5)
- [Step 6](#step-6)
- [Step 7](#step-7)
- [Step 8](#step-8)
- [Step 9](#step-9)
- [Step 10](#step-10)
- [Step 11](#step-11)
- [Step 12](#step-12)
- [Step 13](#step-13)
- [Step 14](#step-14)
- [Step 15](#step-15)
- [Step 16](#step-16)
- [Step 17](#step-17)
- [Step 18](#step-18)
- [Step 19](#step-19)
- [Step 20](#step-20)
- [Step 21](#step-21)
- [Step 22](#step-22)
- [Step 23](#step-23)
- [Step 24](#step-24)
- [Step 25](#step-25)
- [Step 26](#step-26)
- [Step 27](#step-27)
- [Step 28](#step-28)
- [Step 29](#step-29)
- [Step 30](#step-30)
- [Step 31](#step-31)
- [Step 32](#step-32)
- [Step 33](#step-33)
- [Step 34](#step-34)
- [Step 35](#step-35)
- [Step 36](#step-36)
- [Step 37](#step-37)
- [Step 38](#step-38)
- [Step 39](#step-39)
- [Step 40](#step-40)
- [Step 41](#step-41)
- [Step 42](#step-42)
- [Step 43](#step-43)
- [Step 44](#step-44)
- [Step 45](#step-45)
- [Step 46](#step-46)
- [Step 47](#step-47)
- [Step 48](#step-48)
- [Step 49](#step-49)
- [Step 50](#step-50)
- [Step 51](#step-51)
- [Step 52](#step-52)
- [Step 53](#step-53)
- [Step 54](#step-54)
- [Step 55](#step-55)
- [Step 56](#step-56)
- [Step 57](#step-57)
- [Step 58](#step-58)
- [Step 59](#step-59)
- [Step 60](#step-60)
- [Step 61](#step-61)
- [Step 62](#step-62)
- [Step 63](#step-63)
- [Step 64](#step-64)
- [Step 65](#step-65)
- [Step 66](#step-66)
- [Step 67](#step-67)
- [Step 68](#step-68)
- [Step 69](#step-69)
- [Step 70](#step-70)
- [Step 71](#step-71)
- [Step 72](#step-72)
- [Step 73](#step-73)
- [Step 74](#step-74)
- [Step 75](#step-75)
- [Step 76](#step-76)
- [Step 77](#step-77)
- [Step 78](#step-78)
- [Step 79](#step-79)
- [Step 80](#step-80)
- [Step 81](#step-81)
- [Step 82](#step-82)
- [Step 83](#step-83)
- [Step 84](#step-84)
- [Step 85](#step-85)
- [Step 86](#step-86)
- [Step 87](#step-87)
- [Step 88](#step-88)
- [Step 89](#step-89)
- [Step 90](#step-90)
- [Step 91](#step-91)
- [Step 92](#step-92)
- [Step 93](#step-93)
- [Step 94](#step-94)
- [Step 95](#step-95)
- [Step 96](#step-96)
- [Step 97](#step-97)
- [Step 98](#step-98)
- [Step 99](#step-99)
- [Step 100](#step-100)
- [Step 101](#step-101)
- [Step 102](#step-102)
- [Step 103](#step-103)
- [Step 104](#step-104)
- [Step 105](#step-105)
- [Step 106](#step-106)
- [Step 107](#step-107)
- [Step 108](#step-108)
- [Step 109](#step-109)
- [Step 110](#step-110)
- [Step 111](#step-111)
- [Step 112](#step-112)
- [Step 113](#step-113)
- [Step 114](#step-114)
- [Step 115](#step-115)
- [Step 116](#step-116)
- [Step 117](#step-117)
- [Step 118](#step-118)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Step 1
Welcome to the CSS Variables Skyline project! Start by adding the !DOCTYPE html declaration at the top of the document so the browser knows what type of document it's reading.

```html
<!DOCTYPE html>
```

# Step 2
Add opening and closing html tags below the DOCTYPE so you have a place to start putting some code. Be sure to set the language to English.

```html
<html lang="en"></html>
```

# Step 3
Next, add opening and closing head and body tags within the html element.

```html
<!DOCTYPE html>
<html lang="en">
  <head></head>
  <body></body>
</html>
```

# Step 4
Within the head, nest a meta element with a charset of UTF-8, a title element with a title of City Skyline, and a link element that links your styles.css file.

```html
<!DOCTYPE html>
<html lang="en">    
  <head>
    <meta charset="UTF-8">
    <title>City Skyline</title>
    <link href="styles.css" rel="stylesheet" />
  </head>

  <body>
  </body>
</html>
```

# Step 5
In CSS, you can target everything with an asterisk. Add a border to everything by using the * selector, and giving it a border of 1px solid black. This is a trick that helps visualize where elements are and their size. You will remove this later.

```css
* {
  border: 1px solid black;
}
```

# Step 6
Also add a box-sizing of border-box to everything. This will make it so the border you added doesn't add any size to your elements.

```css
* {
  border: 1px solid black;
  box-sizing: border-box;
}
```

# Step 7
You can see the body (it's the inner-most box on your page); the box around it is the html element. Make your body fill the whole viewport by giving it a height of 100vh. Remove the default margin from the body by setting the margin to 0. Finally, set the overflow property to hidden to hide any scroll bars that appear when something extends past the viewport.

```css
body {
  height: 100vh;
  margin: 0;
  overflow: hidden;
}
```

# Step 8
Create a div element in the body with a class of background-buildings. This will be a container for a group of buildings.

```html
  <body>
    <div class="background-buildings"></div
  </body>
```

# Step 9
Give your .background-buildings element a width and height of 100% to make it the full width and height of its parent, the body.

```css
.background-buildings {
  width: 100%;
  height: 100%;
}
```

# Step 10
Nest a div with a class of bb1 in the background buildings container. Open your styles.css file, and give .bb1 a width of 10% and height of 70%. "bb" stands for "background building", this will be your first building.

```html
    <div class="background-buildings">
      <div class="bb1"></div>
    </div>
```

```css
.bb1 {
  width: 10%;
  height: 70%;
}
```

# Step 11
Nest four div elements in the .bb1 container. Give them the classes bb1a, bb1b, bb1c, and bb1d in that order. This building will have four sections.
      
```html
      <div class="bb1">
        <div class="bb1a"></div>
        <div class="bb1b"></div>
        <div class="bb1c"></div>
        <div class="bb1d"></div>
      </div>
```

# Step 12
Give the parts of your building width and height properties with these values: 70% and 10% to .bb1a, 80% and 10% to .bb1b, 90% and 10% to .bb1c, and 100% and 70% to .bb1d. Remember that these percentages are relative to the parent and note that the heights will add up to 100% - vertically filling the container.

```css
.bb1a {
  width: 70%;
  height: 10%;
}
.bb1b {
  width: 80%;
  height: 10%;
}
.bb1c {
  width: 90%;
  height: 10%;
}
.bb1d {
  width: 100%;
  height: 70%;
}
```

# Step 13
Center the parts of your building by turning the .bb1 element into a flexbox parent. Use the flex-direction and align-items properties to center the children.

```css
.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
```
     
# Step 14
Now you have something that is resembling a building. You are ready to create your first variable. Variable declarations begin with two dashes (-) and are given a name and a value like this: --variable-name: value;. In the rule for the bb1 class, create a variable named --building-color1 and give it a value of #999.

```css
.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  --building-color1: #999;
}
```

# Step 15
To use a variable, put the variable name in parentheses with var in front of them like this: var(--variable-name). Whatever value you gave the variable will be applied to whatever property you use it on. Add the variable --building-color1 you created in the previous step as the value of the background-color property of the .bb1a class.      

```css
.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1)
}
```

# Step 16
Use the same variable as the background-color of the .bb1b, .bb1c, and .bb1d classes to fill in the rest of the building.      

```css
.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1)
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1)
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1)
}      
```

# Step 17
Change the value of your variable from #999 to #aa80ff and you can see how it gets applied everywhere you used the variable. This is the main advantage of using variables, being able to quickly change many values in your stylesheet by just changing the value of a variable.

```css
  --building-color1: #aa80ff;      
```

# Step 18
Your first building looks pretty good now. Nest three new div elements in the .background-buildings container and give them the classes of bb2, bb3, and bb4 in that order. These will be three more buildings for the background.

```html
      <div class="bb2"></div>
      <div class="bb3"></div>
      <div class="bb4"></div>
```

# Step 19
Give the new buildings width and height properties of: 10% and 50% for .bb2, 10% and 55% for .bb3, and 11% and 58% for .bb4. You will be using almost all percent based units and some flexbox for this project, so everything will be completely responsive.
 
```css 
.bb2 {
  width: 10%;
  height: 50%;
}
.bb3 {
  width: 10%;
  height: 55%;
}
.bb4 {
  width: 11%;
  height: 58%;
}
```

# Step 20
The buildings are currently stacked on top of each other. Align the buildings by turning the .background-buildings element into a flexbox parent. Use the align-items and justify-content properties to evenly space the buildings across the bottom of the element.

```css
.background-buildings {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
}
```

# Step 21
The buildings are too spaced out. Squeeze them together by adding two empty div elements to the top of the .background-buildings element, two more at the bottom of it, and one more in between .bb3 and .bb4. These will be added as evenly-spaced elements across the container, effectively moving the buildings closer to the center.

```html
    <div class="background-buildings">
      <div></div>
      <div></div>
      <div class="bb1">
        <div class="bb1a"></div>
        <div class="bb1b"></div>
        <div class="bb1c"></div>
        <div class="bb1d"></div>
      </div>
      <div class="bb2"></div>
      <div class="bb3"></div>
      <div></div>
      <div class="bb4"></div>
      <div></div>
      <div></div>
    </div>
```     

# Step 22
Create a new variable below your --building-color1 variable. Name your new variable --building-color2 and give it a value of #66cc99. Then set it as the background-color of .bb2.

```css
.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
}

.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2);
}
```

# Step 23
That didn't work. You should add a fallback value to a variable by putting it as the second value of where you use the variable like this: var(--variable-name, fallback-value). The property will use the fallback value when there's a problem with the variable. Add a fallback value of green to the background-color of .bb2.

```css
.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2, green);
}      
```

# Step 24
Create a new variable below the other ones named --building-color3 and give it a value of #cc6699. Then use it as the background-color of the .bb3 class and give it a fallback value of pink. 

```css
.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
}

.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2, green);
}

.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3, pink);
}
```

# Step 25
That didn't work, because the variables you declared in .bb1 do not cascade to the .bb2 and .bb3 sibling elements. That's just how CSS works. Because of this, variables are often declared in the :root selector. This is the highest level selector in CSS; putting your variables there will make them usable everywhere. Add the :root selector to the top of your stylesheet, and move all your variable declarations there.

```css
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
}

* {
  border: 1px solid black;
  box-sizing: border-box;
}

body {
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

.background-buildings {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
}

.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2, green);
}

.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3, pink);
}

.bb4 {
  width: 11%;
  height: 58%;
}
```

# Step 26
Now that you've worked the bugs out and the buildings are the right colors, you can remove the fallback values in the two places they were used. Go ahead and do that now.
      
```css      
.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2);
}

.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3);
}
```

# Step 27
Create another variable named --building-color4 and give it a value of #538cc6. Make sure it's in the :root selector this time. Then use it to fill in the last building.

```css
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
}

* {
  border: 1px solid black;
  box-sizing: border-box;
}

body {
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

.background-buildings {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
}

.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2);
}

.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3);
}

.bb4 {
  width: 11%;
  height: 58%;
  background-color: var(--building-color4);
}
```

# Step 28
The background buildings are starting to look pretty good. Create a new div below the .background-buildings element and give it a class of foreground-buildings. This will be another container for more buildings.      

```html
    <div class="foreground-buildings"></div>
```
      
# Step 29
You want the .foreground-buildings container to sit directly on top of the .background-buildings element. Give it a width and height of 100%, set the position to absolute, and the top to 0. This will make it the same size as the body and move the start of it to the top left corner.      

```css
.foreground-buildings {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
}      
```

# Step 30
Nest six div elements within .foreground-buildings and give them the classes of fb1 through fb6 in that order. "fb" stands for "foreground building". These will be six more buildings for the foreground.      

```html
    <div class="foreground-buildings">
      <div class="fb1"></div>
      <div class="fb2"></div>
      <div class="fb3"></div>
      <div class="fb4"></div>
      <div class="fb5"></div>
      <div class="fb6"></div>
    </div>      
```

# Step 31
Give the six new elements these width and height values: 10% and 60% to .fb1, 10% and 40% to .fb2, 10% and 35% to .fb3, 8% and 45% to .fb4, 10% and 33% to .fb5, and 9% and 38% to .fb6.      

```css
.fb1 {
  width: 10%;
  height: 60%;
}

.fb2 {
  width: 10%;
  height: 40%;
}

.fb3 {
  width: 10%;
  height: 35%;
}

.fb4 {
  width: 8%;
  height: 45%;
}

.fb5 {
  width: 10%;
  height: 33%;
}

.fb6 {
  width: 9%;
  height: 38%;
}
```

# Step 32
Add the same display, align-items, and justify-content properties and values to .foreground-buildings that you used on .background-buildings. Again, this will use Flexbox to evenly space the buildings across the bottom of their container.

```css
.foreground-buildings {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
}
      
.background-buildings, .foreground-buildings {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
  position: absolute;
  top: 0;
}
```

# Step 33
You should optimize your code. Move the position and top properties and values from .foreground-buildings to .background-buildings. Then select both .background-buildings and .foreground-buildings there, effectively applying those styles to both of the elements. You can use a comma (,) to separate selectors like this: selector1, selector2.      

```css
.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2);
}

.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3);
}

.bb4 {
  width: 11%;
  height: 58%;
  background-color: var(--building-color4);
}

.foreground-buildings {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
}      
```

# Step 34
Now that you did that, you can delete the old .foreground-buildings declaration and all of its properties since they aren't needed anymore.

# Step 35
The skyline is coming together. Fill in the background-color property of the foreground buildings. Use your --building-color1 variable to fill in .fb3 and .fb4, --building-color2 for .fb5, --building-color3 for .fb2 and .fb6, and --building-color4 for .fb1.

```css
.fb1 {
  width: 10%;
  height: 60%;
  background-color: var(--building-color4);
}

.fb2 {
  width: 10%;
  height: 40%;
  background-color: var(--building-color3);
}

.fb3 {
  width: 10%;
  height: 35%;
  background-color: var(--building-color1);
}

.fb4 {
  width: 8%;
  height: 45%;
  background-color: var(--building-color1);
}

.fb5 {
  width: 10%;
  height: 33%;
  background-color: var(--building-color2);
}

.fb6 {
  width: 9%;
  height: 38%;
  background-color: var(--building-color3);
}
```

# Step 36
Squeeze the buildings together again by adding two empty div elements within both the top and bottom of the .foreground-buildings element, and one more in between .fb2 and .fb3.

```html
    <div class="foreground-buildings">
      <div></div>
      <div></div>
      <div class="fb1"></div>
      <div class="fb2"></div>
      <div></div>
      <div class="fb3"></div>
      <div class="fb4"></div>
      <div class="fb5"></div>
      <div class="fb6"></div>
      <div></div>
      <div></div>
    </div>
```

# Step 37
Move the position of .fb4 relative to where it is now by adding a position of relative and left of 10% to it. Do the same for .fb5 but use right instead of left. This will cover up the remaining white space in between the buildings.

```css
.fb4 {
  width: 8%;
  height: 45%;
  background-color: var(--building-color1);
  position: relative;
  left: 10%;
}

.fb5 {
  width: 10%;
  height: 33%;
  background-color: var(--building-color2);
  position: relative;
  right: 10%;
}
```

# Step 38
Your code is starting to get quite long. Add a comment above the .fb1 class that says FOREGROUND BUILDINGS - "fb" stands for "foreground building" to help people understand your code. Above the .bb1 class add another comment that says BACKGROUND BUILDINGS - "bb" stands for "background building". If you don't remember, comments in CSS look like this: /* Comment here */.

```css
/*BACKGROUND BUILDINGS - "bb" stands for "background building"*/
.bb1 {
  width: 10%;
  height: 70%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb2 {
  width: 10%;
  height: 50%;
  background-color: var(--building-color2);
}

.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3);
}

.bb4 {
  width: 11%;
  height: 58%;
  background-color: var(--building-color4);
}

/*FOREGROUND BUILDINGS - "fb" stands for "foreground building"*/
.fb1 {
  width: 10%;
  height: 60%;
  background-color: var(--building-color4);
}
```

# Step 39
Create a new variable in :root called --window-color1 and give it a value of black. This will be a secondary color for the purple buildings.

```css
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
  --window-color1: black;
}
```

# Step 40
Gradients in CSS are a way to transition between colors across the distance of an element. They are applied to the background property and the syntax looks like this:

```css
gradient-type(
  color1,
  color2
);
```

In the example, color1 is solid at the top, color2 is solid at the bottom, and in between it transitions evenly from one to the next. In .bb1a, add a background property below the background-color property. Set it as a gradient of type linear-gradient that uses --building-color1 as the first color and --window-color1 as the second.

```css
.bb1a {
  width: 70%;
  height: 10%;
  background-color: var(--building-color1);
  background: linear-gradient(var(--building-color1), var(--window-color1));
}
```

# Step 41
You want to add the same gradient to the next two sections. Instead of doing that, create a new class selector called bb1-window, and move the height and background properties and values from .bb1a to the new class selector.

```css
.bb1a {
  width: 70%;
  background-color: var(--building-color1);
}

.bb1b {
  width: 80%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1c {
  width: 90%;
  height: 10%;
  background-color: var(--building-color1);
}

.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
}

.bb1-window {
  height: 10%;
  background: linear-gradient(
      var(--building-color1),
      var(--window-color1)
    );
}
```

# Step 42
Add the new bb1-window class to the .bb1a, .bb1b, and .bb1c elements. This will apply the gradient to them.

```html
      <div class="bb1">
        <div class="bb1a bb1-window"></div>
        <div class="bb1b bb1-window"></div>
        <div class="bb1c bb1-window"></div>
        <div class="bb1d"></div>
      </div>
```

# Step 43
You don't need the height or background-color properties in .bb1a, .bb1b or .bb1c anymore, so go ahead and remove them.

```css
.bb1a {
  width: 70%;
}

.bb1b {
  width: 80%;
}

.bb1c {
  width: 90%;
}
```

# Step 44
Gradients can use as many colors as you want like this:

```css
gradient-type(
  color1,
  color2,
  color3
);
```

Add a linear-gradient to .bb1d with orange as the first color, --building-color1 as the second, and --window-color1 as the third. Remember to use the gradient on the background property.

```css
.bb1d {
  width: 100%;
  height: 70%;
  background-color: var(--building-color1);
  background: linear-gradient(orange, var(--building-color1),
      var(--window-color1));
}
```

# Step 45
It's a little hidden behind the foreground buildings, but you can see the three color gradient there. Since you are using that now, remove the background-color property from .bb1d.

```css
.bb1d {
  width: 100%;
  height: 70%;
  background: linear-gradient(
      orange,
      var(--building-color1),
      var(--window-color1)
    );
}
```

# Step 46
You can specify where you want a gradient transition to complete by adding it to the color like this:

```css
gradient-type(
  color1,
  color2 20%,
  color3
);
```

Here, it will transition from color1 to color2 between 0% and 20% of the element and then transition to color3 for the rest. Add 80% to the --building-color1 color of the .bb1d gradient so you can see it in action.

```css
.bb1d {
  width: 100%;
  height: 70%;
  background: linear-gradient(
      orange,
      var(--building-color1) 80%,
      var(--window-color1)
    );
}
```

# Step 47
Remove orange from the .bb1d gradient and change the 80% to 50%. This will make --building-color1 solid for the top half, and then transition to --window-color1 for the bottom half.

```css
.bb1d {
  width: 100%;
  height: 70%;
  background: linear-gradient(
      var(--building-color1) 50%,
      var(--window-color1)
    );
}
```

# Step 48
Nest two new div elements within .bb2, give them the classes of bb2a and bb2b, in that order. These will be two sections for this building.

```html
      <div class="bb2">
        <div class="bb2a"></div>
        <div class="bb2b"></div>
      </div>
```

# Step 49
Give .bb2b a width and height of 100% to make it fill the building container. You will add something on the top a little later.

```css
.bb2b {
  width: 100%;
  height: 100%;
}
```

# Step 50
Create a new variable in :root named window-color2 with a value of #8cd9b3. This will be used as the secondary color for this building.

```css
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
  --window-color1: black;
  --window-color2: #8cd9b3;
}
```

# Step 51
Gradient transitions often gradually change from one color to another. You can make the change a solid line like this:

```css
linear-gradient(
  var(--first-color) 0%,
  var(--first-color) 40%,
  var(--second-color) 40%,
  var(--second-color) 80%
);
```

Add a linear-gradient to .bb2b that uses --building-color2 from 0% to 6% and --window-color2 from 6% to 9%.

```css
.bb2b {
  width: 100%;
  height: 100%;
  background: linear-gradient(
      var(--building-color2),
      var(--building-color2) 6%,
      var(--window-color2) 6%,
      var(--window-color2) 9%
    );
}
```

# Step 52
You can see the hard color change at the top of the section. Change the gradient type from linear-gradient to repeating-linear-gradient for this section. This will make the four colors of your gradient repeat until it gets to the bottom of the element; giving you some stripes, and saving you from having to add a bunch of elements to create them.

```css
.bb2b {
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
      var(--building-color2),
      var(--building-color2) 6%,
      var(--window-color2) 6%,
      var(--window-color2) 9%
    );
}
```

# Step 53
In the next few steps, you are going to use some tricks with CSS borders to turn the .bb2a section into a triangle at the top of the building. First, remove the background-color from .bb2 since you don't need it anymore.

```css
.bb2 {
  width: 10%;
  height: 50%;
}
```

# Step 54
Add these properties to .bb2a:
margin: auto;
width: 5vw;
height: 5vw;
border-top: 1vw solid #000;
border-bottom: 1vw solid #000;
border-left: 1vw solid #999;
border-right: 1vw solid #999;
After you add these, you can see how a thick border on an element gives you some angles where two sides meet. You are going to use that bottom border as the top of the building.

```css
.bb2a {margin: auto;
  width: 5vw;
  height: 5vw;
  border-top: 1vw solid #000;
  border-bottom: 1vw solid #000;
  border-left: 1vw solid #999;
  border-right: 1vw solid #999;
}
```

# Step 55
Next, remove the width and height from .bb2a, and change the border-left and border-right to use 5vw instead of 1vw. The element will now have zero size and the borders will come together in the middle.

```css
.bb2a {
  margin: auto;
  border-top: 1vw solid #000;
  border-bottom: 1vw solid #000;
  border-left: 5vw solid #999;
  border-right: 5vw solid #999;
}
```

# Step 56
Next, change the two #999 of .bb2a to transparent. This will make the left and right borders invisible.

```css
.bb2a {
  margin: auto;
  border-top: 1vw solid #000;
  border-bottom: 1vw solid #000;
  border-left: 5vw solid transparent;
  border-right: 5vw solid transparent;
}
```

# Step 57
Remove the margin and border-top properties and values from .bb2a to turn it into a triangle for the top of the building.

```css
.bb2a {
  border-bottom: 1vw solid #000;
  border-left: 5vw solid transparent;
  border-right: 5vw solid transparent;
}
```

# Step 58
Finally, on the border-bottom property of .bb2a, change the 1vw to 5vh and change the #000 color to your --building-color2 variable. There you go, now it looks good! At any time throughout this project, you can comment out or remove the border property you added to everything at the beginning to see what the buildings will look like when that gets removed at the end.

```css
.bb2a {
  border-bottom: 5vh solid var(--building-color2);
  border-left: 5vw solid transparent;
  border-right: 5vw solid transparent;
}
```

# Step 59
On to the next building! Create a new variable called --window-color3 in :root and give it a value of #d98cb3. This will be the secondary color for the pink buildings.

```css
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
  --window-color1: black;
  --window-color2: #8cd9b3;
  --window-color3: #d98cb3;
}
```

# Step 60
So far, all the gradients you created have gone from top to bottom, that's the default direction. You can specify another direction by adding it before your colors like this:

```css
gradient-type(
  direction,
  color1,
  color2
);
```

Fill in .bb3 with a repeating-linear-gradient. Use 90deg for the direction, your building-color3 for the first two colors, and window-color3 at 15% for the third. When you don't specify a distance for a color, it will use the values that makes sense. In this case, the first two colors will default to 0% and 7.5% because it starts at 0%, and 7.5% is half of the 15%.

```css
.bb3 {
  width: 10%;
  height: 55%;
  background-color: var(--building-color3);
  background: repeating-linear-gradient(
      90deg,
      var(--building-color3),
      var(--building-color3),
      var(--window-color3) 15%
    );
}
```

# Step 61
Remove the background-color property and value from .bb3 since you are using the gradient as the background now.

```css
.bb3 {
  width: 10%;
  height: 55%;
  background: repeating-linear-gradient(
      90deg,
      var(--building-color3),
      var(--building-color3),
      var(--window-color3) 15%
    );
}
```

# Step 62
The next building will have three sections. Nest three div elements within .bb4. Give them the classes of bb4a, bb4b and bb4c in that order.

```html
      <div class="bb4">
        <div class="bb4a"></div>
        <div class="bb4b"></div>
        <div class="bb4c"></div>
      </div>
```

# Step 63
Give the new div elements these width and height values: 3% and 10% to .bb4a, 80% and 5% to .bb4b, and 100% and 85% to .bb4c.

```css
.bb4a {
  width: 3%;
  height: 10%;
}

.bb4b {
  width: 80%;
  height: 5%;
}

.bb4c {
  width: 100%;
  height: 85%;
}
```

# Step 64
Remove the background-color property and value from .bb4, and add it to the three new sections .bb4a, .bb4b, and .bb4c, so only the sections are filled.

```css
.bb4 {
  width: 11%;
  height: 58%;
}

.bb4a {
  width: 3%;
  height: 10%;
  background-color: var(--building-color4);
}

.bb4b {
  width: 80%;
  height: 5%;
  background-color: var(--building-color4);
}
  
.bb4c {
  width: 100%;
  height: 85%;
  background-color: var(--building-color4);
}
```

# Step 65
You want .bb4 to share the properties of .bb1 that center the sections. Instead of duplicating that code, create a new class above the background building comment called building-wrap. Leave it empty for now; this class will be used in a few places to save you some coding.

```css
.building-wrap {
  
}
```

# Step 66
Move the display, flex-direction, and align-items properties and values from .bb1 to the new building-wrap class.

```css
.building-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* BACKGROUND BUILDINGS - "bb" stands for "background building" */
.bb1 {
  width: 10%;
  height: 70%;
}
```

# Step 67
Add the new building-wrap class to the .bb1 and .bb4 elements. This will apply the centering properties to the buildings that need it.

```html
      <div class="bb1 building-wrap">
        <div class="bb1a bb1-window"></div>
        <div class="bb1b bb1-window"></div>
        <div class="bb1c bb1-window"></div>
        <div class="bb1d"></div>
      </div>
      <div class="bb2">
        <div class="bb2a"></div>
        <div class="bb2b"></div>
      </div>
      <div class="bb3"></div>
      <div></div>
      <div class="bb4 building-wrap">
```

# Step 68
Create a new variable called --window-color4 in :root and give it a value of #8cb3d9. This will be the secondary color for the last background building.
  
```css  
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
  --window-color1: black;
  --window-color2: #8cd9b3;
  --window-color3: #d98cb3;
  --window-color4: #8cb3d9;
}
```

# Step 69
Nest four new div elements within .bb4c, give them all the class of bb4-window. These will be windows for this building.        

```html
        <div class="bb4c">
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
        </div>
```

# Step 70
Give the bb4-window class a width of 18%, a height of 90%, and add your --window-color4 variable as the background-color.

```css
.bb4-window {
  width: 18%;
  height: 90%;
  background-color: var(--window-color4);
}
```

# Step 71
The windows are stacked on top of each other at the left of the section, behind the purple building. Add a new class below .building-wrap called window-wrap. Make .window-wrap a flexbox container, and use the align-items and justify-content properties to center its child elements vertically and evenly space them in their parent, respectively.

```css
.window-wrap {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}
```

# Step 72
Add the new window-wrap class to the .bb4c element.

```html
        <div class="bb4c window-wrap">
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
        </div>
```

# Step 73
Looks good! On to the foreground buildings! Turn the .fb1 building into three sections by nesting three new div elements within it. Give them the classes of fb1a, fb1b and fb1c, in that order.

```html
      <div class="fb1">
        <div class="fb1a"></div>
        <div class="fb1b"></div>
        <div class="fb1c"></div>
      </div>
```

# Step 74
Give .fb1b a width of 60% and height of 10%, and .fb1c a width of 100% and height of 80%.

```css
.fb1b {
  width: 60%;
  height: 10%;
}

.fb1c {
  width: 100%;
  height: 80%;
}
```

# Step 75
Add the building-wrap class to the .fb1 element to center the sections.

```html
      <div class="fb1 building-wrap">
        <div class="fb1a"></div>
        <div class="fb1b"></div>
        <div class="fb1c"></div>
      </div>
```

# Step 76
Move the background-color property and value from .fb1 to .fb1b.

```css
.fb1 {
  width: 10%;
  height: 60%;
}

.fb1b {
  width: 60%;
  height: 10%;
  background-color: var(--building-color4);
}
```

# Step 77
Don't worry about the space at the bottom, everything will get moved down later when you add some height to the element at the top of the building. Add a repeating-linear-gradient to .fb1c with a 90deg angle, your --building-color4 from 0% to 10% and transparent from 10% to 15%.

```css
.fb1c {
  width: 100%;
  height: 80%;
  background: repeating-linear-gradient(
    90deg,
    var(--building-color4),
    var(--building-color4) 10%,
    transparent 10%,
    transparent 15%
  )
}
```

# Step 78
You can add multiple gradients to an element by separating them with a comma (,) like this:

```css
gradient1(
  colors
),
gradient2(
  colors
);
```

Add a repeating-linear-gradient to .fb1c below the one that's there; use your --building-color4 from 0% to 10% and --window-color4 from 10% and 90%. This will fill in behind the gradient you added last.

```css
.fb1c {
  width: 100%;
  height: 80%;
  background: repeating-linear-gradient(
      90deg,
      var(--building-color4),
      var(--building-color4) 10%,
      transparent 10%,
      transparent 15%
    ),
              repeating-linear-gradient(
    var(--building-color4),
    var(--building-color4) 10%,
    var( --window-color4) 10%,
    var( --window-color4) 90%
  )
}
```

# Step 79
You're going to use some more border tricks for the top section. Add a border-bottom with a value of 7vh solid var(--building-color4) to .fb1a. This will put a 7vh height border on the bottom. But since the element has zero size, it only shows up as a 2px wide line from the 1px border that is on all the elements.

```css
.fb1a {
  border-bottom: 7vh solid var(--building-color4);
}
```

# Step 80
When you increase the size of the left and right borders, the border on the bottom will expand to be the width of the combined left and right border widths. Add 2vw solid transparent as the value of the border-left and border-right properties of .fb1a. They will be invisible, but it will make the border on the bottom 4vw wide.

```css
.fb1a {
  border-bottom: 7vh solid var(--building-color4);
  border-left: 2vw solid transparent;
  border-right: 2vw solid transparent
}
```

# Step 81
On to the next building! Nest two div elements within .fb2 and give them classes of fb2a and fb2b, in that order.

```html
      <div class="fb2">
        <div class="fb2a"></div>
        <div class="fb2b"></div>
      </div>
```

# Step 82
Give .fb2a a width of 100% and .fb2b a width of 100% and height of 75%.

```css
.fb2a {
  width: 100%;
  height: 75%;
}

.fb2b {
  width: 100%;
  height: 75%;
}
```

# Step 83
Nest three div elements within .fb2b and give them a class of fb2-window. These will be windows for this section of the building.

```html
        <div class="fb2b">
          <div class="fb2-window"></div>
          <div class="fb2-window"></div>
          <div class="fb2-window"></div>
        </div>
```

# Step 84
Add your window-wrap class to .fb2b to position the new window elements.

```html
        <div class="fb2b  window-wrap">
          <div class="fb2-window"></div>
          <div class="fb2-window"></div>
          <div class="fb2-window"></div>
        </div>
```

# Step 85
Give the .fb2-window elements a width of 22%, height of 100%, and a background-color of your --window-color3 variable.

```css
.fb2-window {
  width: 22%;
  height: 100%;
  background-color: var(--window-color3);
}
```

# Step 86
Move the background-color property and value from .fb2 to .fb2b to just color the section and not the container.

```css
.fb2 {
  width: 10%;
  height: 40%;
}

.fb2a {
  width: 100%;
}

.fb2b {
  width: 100%;
  height: 75%;
  background-color: var(--building-color3);
}
```

# Step 87
For .fb2a, add a border-bottom of 10vh solid var(--building-color3), and a border-left and border-right of 1vw solid transparent. This time the border trick will create a trapezoid shape.

```css
.fb2a {
  width: 100%;
  border-bottom: 10vh solid var(--building-color3);
  border-left: 1vw solid transparent;
  border-right: 1vw solid transparent;
}
```

# Step 88
For the next building, nest four div elements within .fb3 with classes of fb3a, fb3b, fb3a again, and fb3b again, in that order. This building will have four sections, and the top two will be almost the same as the bottom two.

```html
      <div class="fb3">
        <div class="fb3a"></div>
        <div class="fb3b"></div>
        <div class="fb3a"></div>
        <div class="fb3b"></div>
      </div>
```

# Step 89
Give the .fb3a element a width of 80% and height of 15%. Then give the .fb3b element a width of 100% and height of 35%.

```css
.fb3a {
  width: 80%;
  height: 15%;
}

.fb3b {
  width: 100%;
  height: 35%;
}
```

# Step 90
Remove the background-color property and value from .fb3, and add them to .fb3a and .fb3b.

```css
.fb3 {
  width: 10%;
  height: 35%;
}

.fb3a {
  width: 80%;
  height: 15%;
  background-color: var(--building-color1);
}
  
.fb3b {
  width: 100%;
  height: 35%;
  background-color: var(--building-color1);
}
```

# Step 91
Add your building-wrap class to the .fb3 element to center the sections.

```html
      <div class="fb3 building-wrap">
        <div class="fb3a"></div>
        <div class="fb3b"></div>
        <div class="fb3a"></div>
        <div class="fb3b"></div>
      </div>
```

# Step 92
Nest three new div elements in the first .fb3a element. Give them each a class of fb3-window. These will be windows for this section.

```html
        <div class="fb3a">
          <div class="fb3-window"></div>
          <div class="fb3-window"></div>
          <div class="fb3-window"></div>
        </div>
```

# Step 93
Give the .fb3-window elements a width of 25%, a height of 80%, and use your --window-color1 variable as the background-color value.

```css
.fb3-window {
  width: 25%;
  height: 80%;
  background-color: var(--window-color1);
}
```

# Step 94
Add your window-wrap class to the .fb3a element to center and space the windows.

```html
        <div class="fb3a window-wrap">
          <div class="fb3-window"></div>
          <div class="fb3-window"></div>
          <div class="fb3-window"></div>
        </div>
```

# Step 95
With CSS variables you can change values without searching everywhere in the stylesheet. Change the --window-color1 value to #bb99ff.

```css
:root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
  --window-color1: #bb99ff;
  --window-color2: #8cd9b3;
  --window-color3: #d98cb3;
  --window-color4: #8cb3d9;
}
```

# Step 96
Only three more buildings to go. Nest two new div elements within the .fb4 element and give them the classes of fb4a and fb4b, in that order. Remember that you sort of flipped the location of .fb4 and .fb5, so it's the rightmost purple building you are working on now.

```html
      <div class="fb4">
        <div class="fb4a"></div>
        <div class="fb4b"></div>
      </div>
```

# Step 97
Give .fb4b a width of 100% and height of 89%.

```css
.fb4b {
  width: 100%;
  height: 89%;
}
```

# Step 98
Add your --building-color1 variable as value of the background-color property of .fb4b. Then, remove the background-color from .fb4.

```css
.fb4 {
  width: 8%;
  height: 45%;
  position: relative;
  left: 10%;
}

.fb4b {
  width: 100%;
  height: 89%;
  background-color: var(--building-color1);
}
```

# Step 99
Nest six div elements within .fb4b and give them all a class of fb4-window.

```html
        <div class="fb4b">
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
        </div>
```

# Step 100
Give the .fb4-window elements a width of 30%, height of 10%, and border-radius of 50%. These will make some circular windows for this building.

```css
.fb4-window {
  width: 30%;
  height: 10%;
  border-radius: 50%;
}
```

# Step 101
Fill in the windows with your secondary color for this building. Also add a margin of 10% to give the windows some space.

```css
.fb4-window {
  width: 30%;
  height: 10%;
  border-radius: 50%;
  margin: 10%;
  background-color: var(--window-color1);
}
```

# Step 102
The windows are stacked on top of each other on the rightmost purple building. Turn the building into a flexbox parent, and use the flex-wrap property to put the windows side by side, and push them down to a new row when they don't fit.

```css
.fb4b {
  width: 100%;
  height: 89%;
  background-color: var(--building-color1);
  display: flex;
  flex-wrap: wrap;
}
```

# Step 103
This building is going to have another triangle on top. Give the top section a border-top of 5vh solid transparent, and a border-left that is 8vw, solid, and uses your building color variable as the color.

```css
.fb4a {
   border-top: 5vh solid transparent;
   border-left: 8vw solid var(--building-color1);
 }
```

# Step 104
On to the next building! It's the green one in the foreground. Give it a repeating-linear-gradient with your building color from 0% to 5%, and transparent from 5% to 10%.

```css
.fb5 {
  width: 10%;
  height: 33%;
  background-color: var(--building-color2);
  position: relative;
  right: 10%;
  background: repeating-linear-gradient(
    var(--building-color2),
    var(--building-color2) 5%,
    transparent 5%,
    transparent 10%
  )
}
```

# Step 105
Add another repeating-linear-gradient below the one you just added. Give it a 90deg direction, use your building color from 0% to 12% and window color 12% to 44%. This will make a bunch of rectangle windows.

```css
.fb5 {
  width: 10%;
  height: 33%;
  background-color: var(--building-color2);
  position: relative;
  right: 10%;
  background: repeating-linear-gradient(
      var(--building-color2),
      var(--building-color2) 5%,
      transparent 5%,
      transparent 10%
    ),
              repeating-linear-gradient(
      90deg,          
      var(--building-color2),
      var(--building-color2) 12%,
      var(--window-color2) 12%,
      var(--window-color2) 44%
    )
}
```

# Step 106
You don't need the background-color for this building anymore so you can remove that property.

```css
.fb5 {
  width: 10%;
  height: 33%;
  position: relative;
  right: 10%;
  background: repeating-linear-gradient(
      var(--building-color2),
      var(--building-color2) 5%,
      transparent 5%,
      transparent 10%
    ),
    repeating-linear-gradient(
      90deg,
      var(--building-color2),
      var(--building-color2) 12%,
      var(--window-color2) 12%,
      var(--window-color2) 44%
    );
}
```

# Step 107
Finally! You made it to the last building! Add a repeating gradient to it with a 90deg direction. Use the building color from 0% to 10% and transparent from 10% to 30%.

```css
.fb6 {
  width: 9%;
  height: 38%;
  background-color: var(--building-color3);
  background: repeating-linear-gradient(
      90deg,
      var(--building-color3),
      var(--building-color3) 10%,
      transparent 10%,
      transparent 30%
    )
}
```

# Step 108
Add another repeating gradient to this building; make it the same as the one you just added, except don't add the 90deg direction and use your window color instead of the two transparent colors.

```css
.fb6 {
  width: 9%;
  height: 38%;
  background-color: var(--building-color3);
  background: repeating-linear-gradient(
    90deg,
    var(--building-color3),
    var(--building-color3) 10%,
    transparent 10%,
    transparent 30%
  ),
              repeating-linear-gradient(
      var(--building-color3),
      var(--building-color3) 10%,
      var(--window-color3) 10%,
      var(--window-color3) 30%
    );
}
```

# Step 109
You can remove the background-color for this building now, since it isn't needed.

```css
.fb6 {
  width: 9%;
  height: 38%;
  background: repeating-linear-gradient(
      90deg,
      var(--building-color3),
      var(--building-color3) 10%,
      transparent 10%,
      transparent 30%
    ),
    repeating-linear-gradient(
      var(--building-color3),
      var(--building-color3) 10%,
      var(--window-color3) 10%,
      var(--window-color3) 30%
    );
}
```

# Step 110
Okay, the buildings are done. Go back to the * selector and remove the border you applied to everything at the beginning and the buildings will come together.

```css
* {
  box-sizing: border-box;
}
```

# Step 111
Add sky as a second class to the .background-buildings element. You are going to make a background for the skyline.

```html
    <div class="background-buildings sky">
```

# Step 112
Give the sky class a radial-gradient. Use #ffcf33 from 0% to 20%, #ffff66 at 21%, and #bbeeff at 100%. This will add circular gradient to the background that will be your sun.

```css
.sky {
  background: radial-gradient(
    #ffcf33,
    #ffcf33 20%,
    #ffff66 21%,
    #bbeeff 100%
  )
}
```

# Step 113
At the top of the sky gradient color list, where you would put a direction for the gradient; add circle closest-corner at 15% 15%,. This will move the start of the gradient to 15% from the top and left. It will make it end at the closest-corner and it will maintain a circle shape. These are some keywords built into gradients to describe how it behaves.

```css
.sky {
  background: radial-gradient(
      circle closest-corner at 15% 15%,
      #ffcf33,
      #ffcf33 20%,
      #ffff66 21%,
      #bbeeff 100%
    );
}
```

# Step 114
A media query can be used to change styles based on certain conditions, and they look like this:

```css
@media (condition) {
 
}  
```

Add an empty media query at the bottom of your stylesheet with a condition of max-width: 1000px. Styles added in here will take effect when the document size is 1000px wide or less.

```css
@media (max-width: 1000px) {
  
}
```

# Step 115
Copy and paste your whole sky class along with all of its properties and values into the media query. You are going to make another color scheme for the skyline that changes it from day to night. Note: You are going to need to scroll past the editable region to copy the class.

```css
@media (max-width: 1000px) {
  .sky {
    background: radial-gradient(
  closest-corner circle at 15% 15%,
  #ffcf33,
  #ffcf33 20%,
  #ffff66 21%,
  #bbeeff 100%
);
  }
}
```

# Step 116
In the sky class of the media query, change the two #ffcf33 color values to #ccc, the #ffff66 to #445, and the #bbeeff to #223. Then you can resize your window to see the background change colors.

```css
  .sky {
    background: radial-gradient(
  closest-corner circle at 15% 15%,
  #ccc,
  #ccc 20%,
  #445 21%,
  #223 100%
);
  }
```
      
# Step 117
Add a :root selector to the top of your media query. Then redefine all four of the --building-color variables to use the value #000 there.      

```css
:root {
  --building-color1: #000;
  --building-color2: #000;
  --building-color3: #000;
  --building-color4: #000;
}
```

# Step 118
Lastly, in the :root selector of the media query, redefine all four of the --window-color variables to use #777. When you're done, resize the window and watch it go from day to night.
Variables are primarily used with colors, and that's how you used them here. But they can be given any value and used on any property. Your project looks great!

```css
  :root {
    --building-color1: #000;
    --building-color2: #000;
    --building-color3: #000;
    --building-color4: #000;
    --window-color1: #777;
    --window-color2: #777;
    --window-color3: #777;
    --window-color4: #777;
  }
      
 :root {
  --building-color1: #aa80ff;
  --building-color2: #66cc99;
  --building-color3: #cc6699;
  --building-color4: #538cc6;
  --window-color1: #bb99ff;
  --window-color2: #8cd9b3;
  --window-color3: #d98cb3;
  --window-color4: #8cb3d9;
}

* {
  box-sizing: border-box;
}

body {
  height: 100vh;
  margin: 0;
  overflow: hidden;
}

.background-buildings, .foreground-buildings {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-evenly;
  position: absolute;
  top: 0;
}

.building-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.window-wrap {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

.sky {
  background: radial-gradient(
      closest-corner circle at 15% 15%,
      #ffcf33,
      #ffcf33 20%,
      #ffff66 21%,
      #bbeeff 100%
    );
}

/* BACKGROUND BUILDINGS - "bb" stands for "background building" */
.bb1 {
  width: 10%;
  height: 70%;
}

.bb1a {
  width: 70%;
}
  
.bb1b {
  width: 80%;
}
  
.bb1c {
  width: 90%;
}

.bb1d {
  width: 100%;
  height: 70%;
  background: linear-gradient(
      var(--building-color1) 50%,
      var(--window-color1)
    );
}

.bb1-window {
  height: 10%;
  background: linear-gradient(
      var(--building-color1),
      var(--window-color1)
    );
}

.bb2 {
  width: 10%;
  height: 50%;
}

.bb2a {
  border-bottom: 5vh solid var(--building-color2);
  border-left: 5vw solid transparent;
  border-right: 5vw solid transparent;
}

.bb2b {
  width: 100%;
  height: 100%;
  background: repeating-linear-gradient(
      var(--building-color2),
      var(--building-color2) 6%,
      var(--window-color2) 6%,
      var(--window-color2) 9%
    );
}

.bb3 {
  width: 10%;
  height: 55%;
  background: repeating-linear-gradient(
      90deg,
      var(--building-color3),
      var(--building-color3),
      var(--window-color3) 15%
    );
}

.bb4 {
  width: 11%;
  height: 58%;
}

.bb4a {
  width: 3%;
  height: 10%;
  background-color: var(--building-color4);
}

.bb4b {
  width: 80%;
  height: 5%;
  background-color: var(--building-color4);
}
  
.bb4c {
  width: 100%;
  height: 85%;
  background-color: var(--building-color4);
}

.bb4-window {
  width: 18%;
  height: 90%;
  background-color: var(--window-color4);
}

/* FOREGROUND BUILDINGS - "fb" stands for "foreground building" */
.fb1 {
  width: 10%;
  height: 60%;
}

.fb1a {
  border-bottom: 7vh solid var(--building-color4);
  border-left: 2vw solid transparent;
  border-right: 2vw solid transparent;
}

.fb1b {
  width: 60%;
  height: 10%;
  background-color: var(--building-color4);
}
  
.fb1c {
  width: 100%;
  height: 80%;
  background: repeating-linear-gradient(
      90deg,
      var(--building-color4),
      var(--building-color4) 10%,
      transparent 10%,
      transparent 15%
    ),
    repeating-linear-gradient(
      var(--building-color4),
      var(--building-color4) 10%,
      var(--window-color4) 10%,
      var(--window-color4) 90%
    );
}

.fb2 {
  width: 10%;
  height: 40%;
}

.fb2a {
  width: 100%;
  border-bottom: 10vh solid var(--building-color3);
  border-left: 1vw solid transparent;
  border-right: 1vw solid transparent;
}

.fb2b {
  width: 100%;
  height: 75%;
  background-color: var(--building-color3);
}

.fb2-window {
  width: 22%;
  height: 100%;
  background-color: var(--window-color3);
}

.fb3 {
  width: 10%;
  height: 35%;
}
  
.fb3a {
  width: 80%;
  height: 15%;
  background-color: var(--building-color1);
}
  
.fb3b {
  width: 100%;
  height: 35%;
  background-color: var(--building-color1);
}

.fb3-window {
  width: 25%;
  height: 80%;
  background-color: var(--window-color1);
}

.fb4 {
  width: 8%;
  height: 45%;
  position: relative;
  left: 10%;
}

.fb4a {
  border-top: 5vh solid transparent;
  border-left: 8vw solid var(--building-color1);
}

.fb4b {
  width: 100%;
  height: 89%;
  background-color: var(--building-color1);
  display: flex;
  flex-wrap: wrap;
}

.fb4-window {
  width: 30%;
  height: 10%;
  border-radius: 50%;
  background-color: var(--window-color1);
  margin: 10%;
}

.fb5 {
  width: 10%;
  height: 33%;
  position: relative;
  right: 10%;
  background: repeating-linear-gradient(
      var(--building-color2),
      var(--building-color2) 5%,
      transparent 5%,
      transparent 10%
    ),
    repeating-linear-gradient(
      90deg,
      var(--building-color2),
      var(--building-color2) 12%,
      var(--window-color2) 12%,
      var(--window-color2) 44%
    );
}

.fb6 {
  width: 9%;
  height: 38%;
  background: repeating-linear-gradient(
      90deg,
      var(--building-color3),
      var(--building-color3) 10%,
      transparent 10%,
      transparent 30%
    ),
    repeating-linear-gradient(
      var(--building-color3),
      var(--building-color3) 10%,
      var(--window-color3) 10%,
      var(--window-color3) 30%
    );
}

@media (max-width: 1000px) {
  :root {
    --building-color1: #000;
    --building-color2: #000;
    --building-color3: #000;
    --building-color4: #000;
    --window-color1: #777;
    --window-color2: #777;
    --window-color3: #777;
    --window-color4: #777;
  }
  .sky {
    background: radial-gradient(
        closest-corner circle at 15% 15%,
        #ccc,
        #ccc 20%,
        #445 21%,
        #223 100%
      );
  }
}
```    
   
```html   
<!DOCTYPE html>
<html lang="en">    
  <head>
    <meta charset="UTF-8">
    <title>City Skyline</title>
    <link href="styles.css" rel="stylesheet" />   
  </head>

  <body>
    <div class="background-buildings sky">
      <div></div>
      <div></div>
      <div class="bb1 building-wrap">
        <div class="bb1a bb1-window"></div>
        <div class="bb1b bb1-window"></div>
        <div class="bb1c bb1-window"></div>
        <div class="bb1d"></div>
      </div>
      <div class="bb2">
        <div class="bb2a"></div>
        <div class="bb2b"></div>
      </div>
      <div class="bb3"></div>
      <div></div>
      <div class="bb4 building-wrap">
        <div class="bb4a"></div>
        <div class="bb4b"></div>
        <div class="bb4c window-wrap">
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
          <div class="bb4-window"></div>
        </div>
      </div>
      <div></div>
      <div></div>
    </div>

    <div class="foreground-buildings">
      <div></div>
      <div></div>
      <div class="fb1 building-wrap">
        <div class="fb1a"></div>
        <div class="fb1b"></div>
        <div class="fb1c"></div>
      </div>
      <div class="fb2">
        <div class="fb2a"></div>
        <div class="fb2b window-wrap">
          <div class="fb2-window"></div>
          <div class="fb2-window"></div>
          <div class="fb2-window"></div>
        </div>
      </div>
      <div></div>
      <div class="fb3 building-wrap">
        <div class="fb3a window-wrap">
          <div class="fb3-window"></div>
          <div class="fb3-window"></div>
          <div class="fb3-window"></div>
        </div>
        <div class="fb3b"></div>
        <div class="fb3a"></div>
        <div class="fb3b"></div>
      </div>
      <div class="fb4">
        <div class="fb4a"></div>
        <div class="fb4b">
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
          <div class="fb4-window"></div>
        </div>
      </div>
      <div class="fb5"></div>
      <div class="fb6"></div>
      <div></div>
      <div></div>
    </div>
  </body>
</html>
```
