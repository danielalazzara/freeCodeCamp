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

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Step 1
Start by setting up your HTML structure. Add a <!DOCTYPE> declaration and an html element with a lang attribute set to en. Within the html element, add a head element and a body element.

```html
<!DOCTYPE html>
<html lang="en">
  <head></head>
  <body></body>
</html>
```

# Step 2
Within your head element, add a meta tag with the charset attribute set to utf-8. Also add a title element with the text Picasso Painting.

```html
  <head>
    <meta charset="utf-8"></meta>
    <title>Picasso Painting</title>
  </head>
```

# Step 3
Go ahead and link your CSS file now, even though you have not written any CSS yet. Add a link element with a rel of stylesheet and an href of styles.css.

```html
  <head>
    <meta charset="utf-8">
    <title>Picasso Painting</title>
    <link rel="stylesheet" href="styles.css"/>
  </head>
```

# Step 4
FontAwesome is a library of SVG-powered icons, many of which are freely available to use. You will be using some of these icons in this project, so you will need to link the external stylesheet to your HTML. Add a link element with a rel of stylesheet and an href of https://use.fontawesome.com/releases/v5.8.2/css/all.css.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Picasso Painting</title>
    <link rel="stylesheet" href="./styles.css" />
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" />
  </head>
  <body>
  </body>
</html>
```

# Step 5
To get your painting started, give your body element a background-color of rgb(184, 132, 46).

```css
body {
  background-color: rgb(184, 132, 46);
}
```

# Step 6
Within your body tag, add a div element. Give it an id of back-wall.

```html
  <body>
    <div id="back-wall"></div>
  </body>
```

# Step 7
Use an id selector to give the element with the id back-wall a background-color of #8B4513.

```css
#back-wall {
  background-color: #8B4513;
}
```

# Step 8
Give the #back-wall element a width of 100% and a height of 60%.

```css
#back-wall {
  background-color: #8B4513;
  width: 100%;
  height: 60%;
}
```

# Step 9
Typically, HTML is rendered in a top-down manner. Elements at the top of the code are positioned at the top of the page. However, many times you may want to move the elements to different positions. You can do this with the position property. Set the position property for the #back-wall element to absolute. An absolute position takes the element out of that top-down document flow and allows you to adjust it relative to its container. When an element is manually positioned, you can shift its layout with top, left, right, and bottom. Set the #back-wall element to have a top value of 0, and a left value of 0.

```css
#back-wall {
  background-color: #8B4513;
  width: 100%;
  height: 60%;
  position: absolute; 
  top: 0;
  left: 0;
}
```

# Step 10
The z-index property is used to create "layers" for your HTML elements. If you are familiar with image editing tools, you may have worked with layers before. This is a similar concept. Elements with a higher z-index value will appear to be layered on top of elements with a lower z-index value. This can be combined with the positioning in the previous lesson to create unique effects. Since the back-wall element will need to appear "behind" the other elements you will be creating, give the back-wall element a z-index of -1.

```css
#back-wall {
  background-color: #8B4513;
  width: 100%;
  height: 60%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
```

# Step 11
Below your #back-wall element, create a div with a class of characters. This is where you will be creating your painting's characters.

```html
  <body>
    <div id="back-wall"></div>
    <div class="characters"></div>
  </body>
```

# Step 12
Inside that .characters element, create another div with an id of offwhite-character.

```html
  <body>
    <div id="back-wall"></div>
    <div class="characters">
      <div id="offwhite-character"></div>
    </div>
  </body>
```

# Step 13
Create four div elements inside your offwhite-character element. Give those div elements the following id values, in order: white-hat, black-mask, gray-instrument, tan-table.

```html
  <body>
    <div id="back-wall"></div>
    <div class="characters">
      <div id="offwhite-character">
        <div id="white-hat"></div>
        <div id="black-mask"></div>
        <div id="gray-instrument"></div>
        <div id="tan-table"></div>
      </div>
    </div>
  </body>
```

# Step 14
This character needs eyes. Create two div elements in the #black-mask element. Give them the classes eyes left and eyes right, in that order.

```html
  <body>
    <div id="back-wall"></div>
    <div class="characters">
      <div id="offwhite-character">
        <div id="white-hat"></div>
        <div id="black-mask">
          <div class="eyes left"></div>
          <div class="eyes right"></div>
        </div>
        <div id="gray-instrument"></div>
        <div id="tan-table"></div>
      </div>
    </div>
  </body>
```

# Step 15
Create some "dots" for the instrument. Add five div elements within your #gray-instrument element. Set the class of each to black-dot.

```html
        <div id="gray-instrument">
          <div class="black-dot"></div>
          <div class="black-dot"></div>
          <div class="black-dot"></div>
          <div class="black-dot"></div>
          <div class="black-dot"></div>
        </div>
```

# Step 16
Using an id selector, create a rule for the element with the id offwhite-character. Give it a width of 300px, a height of 550px, and a background-color of GhostWhite.

```css
#offwhite-character {
  width:300px;
  height: 550px;
  background-color: GhostWhite;
}
```

# Step 17
Move the #offwhite-character into place by giving it a position of absolute, a top value of 20%, and a left value of 17.5%.

```css
#offwhite-character {
  width: 300px;
  height: 550px;
  background-color: GhostWhite;
  position: absolute;
  top: 20%;
  left: 17.5%;
}
```

# Step 18
Using an id selector, style the element with the id white-hat. Give it a width and height of 0, and a border-style of solid.

```css
#white-hat {
  width: 0;
  height: 0;
  border-style: solid;
}
```

# Step 19
That does not look quite right. Set a border-width of 0 120px 140px 180px to size the hat properly.

```css
#white-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 120px 140px 180px;
}
```

# Step 20
Now you have a large box. Give it a border-top-color, border-right-color, and border-left-color of transparent. Set the border-bottom-color to GhostWhite. This will make it look more like a hat.

```css
#white-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 120px 140px 180px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-left-color: transparent;
  border-bottom-color: GhostWhite;
}
```

# Step 21
Give the hat a position of absolute, a top value of -140px, and a left value of 0.

```css
#white-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 120px 140px 180px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-left-color: transparent;
  border-bottom-color: GhostWhite;
  position: absolute;
  top: -140px;
  left: 0;
}
```

# Step 22
Using an id selector, create a rule for the element with the id black-mask. Give it a width of 100%, a height of 50px, and a background-color of rgb(45, 31, 19).

```css
#black-mask {
  width: 100%;
  height: 50px;
  background-color: rgb(45, 31, 19);
}
```

# Step 23
Give the mask a position of absolute, and a top and left value of 0

```css
#black-mask {
  width: 100%;
  height: 50px;
  background-color: rgb(45, 31, 19);
  position: absolute;
  top: 0;
  left: 0;
}
```

# Step 24
To ensure you can see the mask, give it a z-index of 1.

```css
#black-mask {
  width: 100%;
  height: 50px;
  background-color: rgb(45, 31, 19);
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}
```

# Step 25
Using an id selector, give the element with the id gray-instrument a width of 15%, a height of 40%, and a background-color of rgb(167, 162, 117).

```css
#gray-instrument {
  width: 15%;
  height: 40%;
  background-color: rgb(167, 162, 117);
}
```

# Step 26
Now move it into place with a position of absolute, a top value of 50px, and a left value of 125px.

```css
#gray-instrument {
  width: 15%;
  height: 40%;
  background-color: rgb(167, 162, 117);
  position: absolute; 
  top: 50px; 
  left: 125px;
}
```

# Step 27
Set the z-index to 1.

```css
#gray-instrument {
  width: 15%;
  height: 40%;
  background-color: rgb(167, 162, 117);
  position: absolute; 
  top: 50px; 
  left: 125px;
  z-index: 1;
}
```

# Step 28
Use a class selector to create a rule for the elements with black-dot class. Set the width to 10px, the height to 10px, and the background-color to rgb(45, 31, 19).

```css
.black-dot {
  width: 10px;
  height: 10px; 
  background-color: rgb(45, 31, 19);
}
```

# Step 29
These dots are just a little too square. Give the black-dot class a border-radius of 50% to fix it.

```css
.black-dot {
  width: 10px;
  height: 10px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
}
```

# Step 30
Move the dots into place by setting the display to block, the margin to auto, and the margin-top to 65%.

```css
.black-dot {
  width: 10px;
  height: 10px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
  display: block;
  margin: auto;
  margin-top: 65%;
}
```

# Step 31
Use an id selector to style the element with the id tan-table. Give it a width of 450px, a height of 140px, and a background-color of #D2691E.

```css
#tan-table {
  width: 450px;
  height: 140px;
  background-color: #D2691E;
}
```

# Step 32
Move the table into place by giving it a position of absolute, a top value of 275px, and a left value of 15px.

```css
#tan-table {
  width: 450px;
  height: 140px;
  background-color: #D2691E;
  position: absolute;
  top: 275px;
  left: 15px;
}
```

# Step 33
Give the table a z-index of 1.

```css
#tan-table {
  width: 450px;
  height: 140px;
  background-color: #D2691E;
  position: absolute;
  top: 275px;
  left: 15px;
  z-index: 1;
}
```

# Step 34
After your div#offwhite-character element, add a div with the id of black-character.

```html
      <div id="black-character"></div>
```

# Step 35
Within your new #black-character element, add three div elements with the following id values, in order: black-hat, gray-mask, white-paper.

```html
      <div id="black-character">
        <div id="black-hat"></div>
        <div id="gray-mask"></div>
        <div id="white-paper"></div>
      </div>
```

# Step 36
The mask needs eyes. Within your #gray-mask element, add two div elements. The first should have the class set to eyes left, and the second should have the class set to eyes right. 

```html
      <div id="black-character">
        <div id="black-hat"></div>
        <div id="gray-mask">
          <div class="eyes left"></div>
          <div class="eyes right"></div>
        </div>
      </div>
```

# Step 37
Time to use some FontAwesome icons. The i element is used for idiomatic text, or text that is separate from the "normal" text content. This could be for italic text, such as scientific terms, or for icons like those provided by FontAwesome. Within your #white-paper element, add four i elements. Give them all a class value of fas fa-music. This special class is how FontAwesome determines which icon to load. fas indicates the category of icons (FontAwesome Solid, here), while fa-music selects the specific icon.

```html
        <div id="white-paper">
          <i class="fas fa-music"></i>
          <i class="fas fa-music"></i>
          <i class="fas fa-music"></i>
          <i class="fas fa-music"></i>
        </div>
```

# Step 38
Use an id selector to create a rule for the element with the id black-character. Set the width to 300px, the height to 500px, and the background-color to rgb(45, 31, 19).

```css
#black-character {
  width: 300px;
  height: 500px;
  background-color: rgb(45, 31, 19);
}
```

# Step 39
Move the #black-character element into place by setting the position to absolute, the top to 30%, and the left to 59%.

```css
#black-character {
  width: 300px;
  height: 500px;
  background-color: rgb(45, 31, 19);
  position: absolute;
  top: 30%;
  left: 59%;
}
```

# Step 40
Use an id selector to create a rule for the element with the id black-hat. Give it a width of 0, a height of 0, and a border-style of solid.

```css
#black-hat {
  width: 0;
  height: 0;
  border-style: solid;
}
```

# Step 41
Set the border-width of the #black-hat to 150px 0 0 300px.

```css
#black-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 150px 0 0 300px;
}
```

# Step 42
Just like with your #white-hat, you should style the border for the #black-hat element. Give it a border-top-color, border-right-color, and border-bottom-color of transparent. Set the border-left-color to rgb(45, 31, 19).

```css
#black-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 150px 0 0 300px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  border-left-color: rgb(45, 31, 19);
}
```

# Step 43
Now position the #black-hat element. Give it a position of absolute, with a top of -150px and a left of 0.

```css
#black-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 150px 0 0 300px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  border-left-color: rgb(45, 31, 19);
  position: absolute;
  top: -150px;
  left: 0;
}
```

# Step 44
Using an id selector, style the element with the id gray-mask. Give it a width of 150px, a height of 150px, and a background-color of rgb(167, 162, 117).

```css
#gray-mask {
  width: 150px;
  height: 150px;
  background-color: rgb(167, 162, 117);
}
```

# Step 45
Position the #gray-mask element by setting position to absolute, the top to -10px, and the left to 70px.

```css
#gray-mask {
  width: 150px;
  height: 150px;
  background-color: rgb(167, 162, 117);
  position: absolute;
  top: -10px;
  left: 70;
}
```

# Step 46
Using an id selector, create a rule for the id white-paper. Set the width to 400px, the height to 100px, and the background-color to GhostWhite.

```css
#white-paper {
  width: 400px;
  height: 100px;
  background-color: GhostWhite;
}
```

# Step 47
Give the #white-paper a position of absolute, a top of 250px, and a left of -150px to move it into place.

```css
#white-paper {
  width: 400px;
  height: 100px;
  background-color: GhostWhite;
  position: absolute;
  top: 250px;
  left: -150px;
}
```

# Step 48
Set the z-index of the #white-paper element to 1.

```css
#white-paper {
  width: 400px;
  height: 100px;
  background-color: GhostWhite;
  position: absolute;
  top: 250px;
  left: -150px;
  z-index: 1;
}
```

# Step 49
FontAwesome icons come with their own styling to define the icon. However, you can still set the styling yourself as well, to change things like the color and size. For now, use a class selector to target the icons with the class fa-music. Set the display to inline-block, the margin-top to 8%, and the margin-left to 13%.

```css
.fa-music {
  display: inline-block;
  margin-top:8%;
  margin-left: 13%;
}
```

# Step 50
Below your #black-character element, add two new div elements. These will be the shawl. Give both of them a class of blue. Then give the first one an id of blue-left, and the second an id of blue-right.

```html
      <div class="blue" id="blue-left"></div>
      <div class="blue" id="blue-right"></div>
```

# Step 51
Use a class selector to target the new elements with the class blue. Set the background-color to #1E90FF.

```css
.blue {
  background-color: #1E90FF;
}
```

# Step 52
Select the element with the id blue-left using an id selector. Give it a width of 500px and a height of 300px.

```css
#blue-left {
  width: 500px;
  height: 300px;
}
```

# Step 53
Now set the position to absolute, the top to 20%, and the left to 20%.

```css
#blue-left {
  width: 500px;
  height: 300px;
  position: absolute;
  top: 20%;
  left: 20%;
}
```

# Step 54
Next, target the element with the id blue-right using an id selector. Set the width to 400px and the height to 300px.

```css
#blue-right {
  width: 400px;
  height: 300px;
}

#blue-right {
  width: 400px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 40%;
}
```

# Step 56
Below your .blue elements, add another div. Give it the id value of orange-character.

```html
        <div id="orange-character"></div>
```

# Step 57
Within that #orange-character element, add four div elements. Give them the id values of black-round-hat, eyes-div, triangles, and guitar, in order.

```html
      <div id="orange-character">
        <div id="black-round-hat"></div>
        <div id="eyes-div"></div>
        <div id="triangles"></div>
        <div id="guitar"></div>
      </div>
```

# Step 58
The #eyes-div element should hold some eyes. Add two div elements inside. Give the first a class of eyes left, and give the second a class of eyes right.

```html
        <div id="eyes-div">
          <div class="eyes left"></div>
          <div class="eyes right"></div>
        </div>
```

# Step 59
Within the #triangles div, you will need to add the elements that will become your triangles. Create thirty div elements and give each of them the class triangle.

```html
        <div id="triangles">
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
        </div>
```

# Step 60
Within the #guitar element, create three div elements. Give the first two a class value of guitar. Then give the first an id of guitar-left, and the second an id of guitar-right. Add an id to the third div with the value guitar-neck. The third div should not have the guitar class.

```html
        <div id="guitar">
          <div class="guitar" id="guitar-left"></div>
          <div class="guitar" id="guitar-right"></div>
          <div id="guitar-neck"></div>
        </div>
```

# Step 61
Use another FontAwesome icon for your .guitar. Inside both the #guitar-left and #guitar-right elements, add an i element and give it a class of fas fa-bars.

```html
          <div class="guitar" id="guitar-left">
            <i class="fas fa-bars"></i>
          </div>
          <div class="guitar" id="guitar-right">
            <i class="fas fa-bars"></i>
          </div>
```

# Step 62
Select your orange-character element with an id selector. Give it a width of 250px, a height of 550px, and a background-color of rgb(240, 78, 42).

```css
#orange-character {
  width: 250px;
  height: 550px;
  background-color: rgb(240, 78, 42);
}
```

# Step 63
Give the #orange-character element a position of absolute, a top of 25%, and a left of 40%.

```css
#orange-character {
  width: 250px;
  height: 550px;
  background-color: rgb(240, 78, 42);
  position: absolute;
  top: 25%;
  left: 40%;
}
```

# Step 64
Style the element with the id black-round-hat using an id selector. Set the width to 180px, the height to 150px, and the background-color to rgb(45, 31, 19).

```css
#black-round-hat {
  width: 180px;
  height: 150px; 
  background-color: rgb(45, 31, 19);
}
```

# Step 65
The #black-round-hat element should probably be round. Give it a border-radius of 50% to fix this.

```css
#black-round-hat {
  width: 180px;
  height: 150px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
}
```

# Step 66
Move the #black-round-hat element into place with a position of absolute, a top of -100px, and a left of 5px.

```css
#black-round-hat {
  width: 180px;
  height: 150px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
  position: absolute;
  top: -100px;
  left: 5px;
}
```

# Step 67
Put the #black-round-hat element on the correct layer with a z-index of -1.

```css
#black-round-hat {
  width: 180px;
  height: 150px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
  position: absolute;
  top: -100px;
  left: 5px;
  z-index: -1;
}
```

# Step 68
Use an id selector to create a rule for the element with the id eyes-div. Set the width to 180px and the height to 50px.

```css
#eyes-div {
  width: 180px;
  height: 50px;
}
```

# Step 69
Now move the #eyes-div element into position with position set to absolute, top set to -40px, and left set to 20px.

```css
#eyes-div {
  width: 180px;
  height: 50px;
  position: absolute;
  top: -40px;
  left: 20px;
}
```

# Step 70
Give the #eyes-div element a z-index of 3.

```css
#eyes-div {
  width: 180px;
  height: 50px;
  position: absolute;
  top: -40px;
  left: 20px;
  z-index: 3;
}
```

# Step 71
Target the element with the id triangles using an id selector. Set the width to 250px and the height to 550px.

```css
#triangles {
  width: 250;
  height: 550;
}
```

# Step 72
Create a class selector for the elements with the triangle class. Set the width to 0 and the height to 0.

```css
.triangle {
  width: 0;
  height: 0;
}
```

# Step 73
Style the border of your .triangle elements. Set the border-style to solid and the border-width to 42px 45px 45px 0.

```css
.triangle {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 42px 45px 45px 0;
}
```

# Step 74
Give your .triangle elements the correct color. Set the border-top-color, border-bottom-color, and border-left-color to transparent. Set the border-right-color to Gold.

```css
.triangle {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 42px 45px 45px 0;
  border-top-color: transparent;
  border-bottom-color: transparent;  
  border-left-color: transparent;
  border-right-color: Gold;
}
```

# Step 75
Adjust the layout of the .triangle elements with a display of inline-block.

```css
.triangle {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 42px 45px 45px 0;
  border-top-color: transparent;
  border-right-color: Gold;
  border-bottom-color: transparent;
  border-left-color: transparent;
  display: inline-block;
}
```

# Step 76
Now use an id selector for guitar. Set the width to 100%, and the height to 100px.

```css
#guitar {
  width: 100%;
  height: 100px;
}
```

# Step 77
In the same #guitar selector, set the position to absolute, the top to 120px, and the left to 0px.

```css
#guitar {
  width: 100%;
  height: 100px;
  position: absolute;  
  top: 120px; 
  left: 0px;
}
```

# Step 78
Give the #guitar rule a z-index of 3.

```css
#guitar {
  width: 100%;
  height: 100px;
  position: absolute;
  top: 120px;
  left: 0px;
  z-index: 3;
}
```

# Step 79
Now use a class selector to target guitar. This will style the two "halves" of your guitar. Set the width to 150px, the height to 120px, the background-color to Goldenrod, and the border-radius to 50%.

```css
.guitar {
  width: 150px;
  height: 120px;
  background-color: Goldenrod;
  border-radius: 50%;
}
```

# Step 80
Select the id with value guitar-left, and set the position to absolute and the left to 0px.

```css
#guitar-left {
  position: absolute;
  left: 0px;
}
```

# Step 81
Select the id with value guitar-right, and also set position to absolute. This time, set left to 100px.

```css
#guitar-right {
  position: absolute;
  left: 100px;
}
```

# Step 82
Now you need to move the bar icons into place. Create a class selector for the fa-bars class. Set the display to block, the margin-top to 30%, and the margin-left to 40%.

```css
.fa-bars {
  display: block;
  margin-top: 30%;
  margin-left: 40%;
}
```

# Step 83
Use an id selector to create a rule for the id guitar-neck. Set the width to 200px, the height to 30px, and the background-color to #D2691E.

```css
#guitar-neck {
  width: 200px;
  height: 30px;
  background-color: #D2691E;
}
```

# Step 84
Now move the #guitar-neck element with a position of absolute, a top value of 45px, and a left value of 200px.

```css
#guitar-neck {
  width: 200px;
  height: 30px;
  background-color: #D2691E;
  position: absolute; 
  top: 45px;
  left: 200px;
}
```

# Step 85
Give the #guitar-neck element a z-index of 3.

```css
#guitar-neck {
  width: 200px;
  height: 30px;
  background-color: #D2691E;
  position: absolute;
  top: 45px;
  left: 200px;
  z-index: 3;
}
```

# Step 86
Time to style the elements with the eyes class. Use a class selector to set the width to 35px, the height to 20px, the background-color to #8B4513, and the border-radius to 20px 50%.

```css
.eyes {
  width: 35px;
  height: 20px; 
  background-color: #8B4513;
  border-radius: 20px 50%;
}
```

# Step 87
Target the class with value right and set the position to absolute, top to 15px, and right to 30px.

```css
.right {
  position: absolute;
  top: 15px;
  right: 30px;
}
```

# Step 88
For the class with value left, create the selector and set the position to absolute, the top to 15px, and the left to 30px.

```css
.left {
  position: absolute;
  top: 15px;
  left: 30px;
}
```

# Step 89
One last step. The FontAwesome icons are a little too small. Target all of them with a class selector for fas, and set the font-size to 30px. With that, your Picasso painting is complete!

```css
body {
  background-color: rgb(184, 132, 46);
}

#back-wall {
  background-color: #8B4513;
  width: 100%;
  height: 60%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}

#offwhite-character {
  width: 300px;
  height: 550px;
  background-color: GhostWhite;
  position: absolute;
  top: 20%;
  left: 17.5%;
}

#white-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 120px 140px 180px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: GhostWhite;
  border-left-color: transparent;
  position: absolute;
  top: -140px;
  left: 0;
}

#black-mask {
  width: 100%;
  height: 50px;
  background-color: rgb(45, 31, 19);
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

#gray-instrument {
  width: 15%;
  height: 40%;
  background-color: rgb(167, 162, 117);
  position: absolute;
  top: 50px;
  left: 125px;
  z-index: 1;
}

.black-dot {
  width: 10px;
  height: 10px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
  display: block;
  margin: auto;
  margin-top: 65%;
}

#tan-table {
  width: 450px;
  height: 140px;
  background-color: #D2691E;
  position: absolute;
  top: 275px;
  left: 15px;
  z-index: 1;
}

#black-character {
  width: 300px;
  height: 500px;
  background-color: rgb(45, 31, 19);
  position: absolute;
  top: 30%;
  left: 59%;
}

#black-hat {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 150px 0 0 300px;
  border-top-color: transparent;
  border-right-color: transparent;
  border-bottom-color: transparent;
  border-left-color: rgb(45, 31, 19);
  position: absolute;
  top: -150px;
  left: 0;
}

#gray-mask {
  width: 150px;
  height: 150px;
  background-color: rgb(167, 162, 117);
  position: absolute;
  top: -10px;
  left: 70px;
}

#white-paper {
  width: 400px;
  height: 100px;
  background-color: GhostWhite;
  position: absolute;
  top: 250px;
  left: -150px;
  z-index: 1;
}

.fa-music {
  display: inline-block;
  margin-top: 8%;
  margin-left: 13%;
}

.blue {
  background-color: #1E90FF;
}

#blue-left {
  width: 500px;
  height: 300px;
  position: absolute;
  top: 20%;
  left: 20%;
}

#blue-right {
  width: 400px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 40%;
}

#orange-character {
  width: 250px;
  height: 550px;
  background-color: rgb(240, 78, 42);
  position: absolute;
  top: 25%;
  left: 40%;
}

#black-round-hat {
  width: 180px;
  height: 150px;
  background-color: rgb(45, 31, 19);
  border-radius: 50%;
  position: absolute;
  top: -100px;
  left: 5px;
  z-index: -1;
}

#eyes-div {
  width: 180px;
  height: 50px;
  position: absolute;
  top: -40px;
  left: 20px;
  z-index: 3;
}

#triangles {
  width: 250px;
  height: 550px;
}

.triangle {
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 42px 45px 45px 0;
  border-top-color: transparent;
  border-right-color: Gold; /* yellow */
  border-bottom-color: transparent;
  border-left-color: transparent;
  display: inline-block;
}

#guitar {
  width: 100%;
  height: 100px;
  position: absolute;
  top: 120px;
  left: 0px;
  z-index: 3;
}

.guitar {
  width: 150px;
  height: 120px;
  background-color: Goldenrod;
  border-radius: 50%;
}

#guitar-left {
  position: absolute;
  left: 0px;
}

#guitar-right {
  position: absolute;
  left: 100px;
}

.fa-bars {
  display: block;
  margin-top: 30%;
  margin-left: 40%;
}

#guitar-neck {
  width: 200px;
  height: 30px;
  background-color: #D2691E;
  position: absolute;
  top: 45px;
  left: 200px;
  z-index: 3;
}

.eyes {
  width: 35px;
  height: 20px;
  background-color: #8B4513;
  border-radius: 20px 50%;
}

.right {
  position: absolute;
  top: 15px;
  right: 30px;
}

.left {
  position: absolute;
  top: 15px;
  left: 30px;
}

.fas {
  font-size: 30px;
}
```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Picasso Painting</title>
    <link rel="stylesheet" href="./styles.css" />
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
  </head>
  <body>
    <div id="back-wall"></div>
    <div class="characters">
      <div id="offwhite-character">
        <div id="white-hat"></div>
        <div id="black-mask">
          <div class="eyes left"></div>
          <div class="eyes right"></div>
        </div>
        <div id="gray-instrument">
          <div class="black-dot"></div>
          <div class="black-dot"></div>
          <div class="black-dot"></div>
          <div class="black-dot"></div>
          <div class="black-dot"></div>
        </div>
        <div id="tan-table"></div>
      </div>
      <div id="black-character">
        <div id="black-hat"></div>
        <div id="gray-mask">
          <div class="eyes left"></div>
          <div class="eyes right"></div>
        </div>
        <div id="white-paper">
          <i class="fas fa-music"></i>
          <i class="fas fa-music"></i>
          <i class="fas fa-music"></i>
          <i class="fas fa-music"></i>
        </div>
      </div>
      <div class="blue" id="blue-left"></div>
      <div class="blue" id="blue-right"></div>
      <div id="orange-character">
        <div id="black-round-hat"></div>
        <div id="eyes-div">
          <div class="eyes left"></div>
          <div class="eyes right"></div>
        </div>
        <div id="triangles">
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
          <div class="triangle"></div>
        </div>
        <div id="guitar">
          <div class="guitar" id="guitar-left">
            <i class="fas fa-bars"></i>
          </div>
          <div class="guitar" id="guitar-right">
            <i class="fas fa-bars"></i>
          </div>
          <div id="guitar-neck"></div>
        </div>
      </div>
    </div>
  </body>
</html>
```
