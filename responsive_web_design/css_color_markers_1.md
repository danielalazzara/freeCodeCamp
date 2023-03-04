# Step 1
As you've seen in the previous projects, webpages should start with a DOCTYPE html declaration, followed by an html element.
Add a DOCTYPE html declaration at the top of the document, and an html element after that. Give the html element a lang attribute with en as its value.

```html
<!DOCTYPE html>
<html lang="en"></html>
```

# Step 2
Nest a head element within the html element. Just after the head element, add a body element.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
  </head>
  <body>
  </body>
</html>
```

# Step 3
Remember that the title element gives search engines extra information about the page. It also tells browsers what text to display in the title bar when the page is open, and on the tab for the page.
Within the head element, nest a title element with the text Colored Markers.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Colored Markers</title>
  </head>
  <body>
  </body>
</html>
```

# Step 4
To tell browsers how to encode characters on your page, set the charset to utf-8. utf-8 is a universal character set that includes almost every character from all human languages.
Inside the head element, nest a meta element with the attribute charset set to utf-8. Remember that meta elements are self-closing, and do not need a closing tag.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Colored Markers</title>
    <meta charset="utf-8">
  </head>
  <body>
  </body>
</html>
```

# Step 5
Add another self-closing meta element within the head. Give it a name attribute set to viewport and a content attribute set to width=device-width, initial-scale=1.0 so your page looks the same on all devices.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"
    <title>Colored Markers</title>
  </head>
  <body>
  </body>
</html>
```

# Step 6
Now you're ready to start adding content to the page.
Within the body, nest an h1 element with the text CSS Color Markers.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
  </head>
  <body>
    <h1>CSS Color Markers</h1>
  </body>
</html>
```

# Step 7
In this project you'll work with an external CSS file to style the page. We've already created a styles.css file for you. But before you can use it, you'll need to link it to the page.
Nest a link element within the head. Give it a rel attribute set to stylesheet and an href attribute set to styles.css.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet", href="styles.css"></link>
  </head>
  <body>
    <h1>CSS Color Markers</h1>
  </body>
</html>
```

# Step 8
Now that your external CSS file is set up, you can start styling the page.
As a reminder, here's how to target a paragraph element and align it to the right:

```css
p {
  text-align: right;
}
```

Create a new CSS rule that targets the h1 element, and set its text-align property to center.

```css
h1 {
  text-align: center;
}
```

# Step 9
Now you'll add some elements that you'll eventually style into color markers.
First, within the body, add a div element and set its class attribute to container. Make sure the div element is below the h1 element.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container"></div>
  </body>
</html>
```

# Step 10
Next, within the div, add another div element and give it a class of marker.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker">
      </div>
    </div>
  </body>
</html>
```

# Step 11
It's time to add some color to the marker. Remember that one way to add color to an element is to use a color keyword like black, cyan, or yellow.
As a reminder, here's how to target the class freecodecamp:

```css
.freecodecamp {

}
```
Create a new CSS rule that targets the class marker, and set its background-color property to red.
Note: You will not see any changes after adding the CSS.

```css
h1 {
  text-align: center;
}

.marker {
  background-color:red;
}
```

# Step 12
The background color was applied, but since the marker div element is empty, it doesn't have any height by default.
In your .marker CSS rule, set the height property to 25px and the width property to 200px

```css
h1 {
  text-align: center;
}

.marker {
  background-color: red;
  height:25px;
  width:200px;
}
```

# Step 13
Your marker would look better if it was centered on the page. An easy way to do that is with the margin shorthand property.
In the last project, you set the margin area of elements separately with properties like margin-top and margin-left. The margin shorthand property makes it easy to set multiple margin areas at the same time.
To center your marker on the page, set its margin property to auto. This sets margin-top, margin-right, margin-bottom, and margin-left all to auto.

```css
h1 {
  text-align: center;
}

.marker {
  width: 200px;
  height: 25px;
  background-color: red;
  margin:auto;
}
```

# Step 14
Now that you've got one marker centered with color, it's time to add the other markers.
In the container div, add two more div elements and give them each a class of marker.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker">
      </div>
      <div class="marker">
      </div>
      <div class="marker">
      </div>
    </div>
  </body>
</html>
```

# Step 15
While you have three separate marker div elements, they look like one big rectangle. You should add some space between them to make it easier to see each element.
When the shorthand margin property has two values, it sets margin-top and margin-bottom to the first value, and margin-left and margin-right to the second value.
In your .marker CSS rule, set the margin property to 10px auto.

```css
h1 {
  text-align: center;
}

.marker {
  width: 200px;
  height: 25px;
  background-color: red;
  margin: 10px auto;
}
```

# Step 16
To give the markers different colors, you will need to add a unique class to each one. Multiple classes can be added to an element by listing them in the class attribute and separating them with a space. For example, the following adds both the animal and dog classes to a div element.

```html
<div class="animal dog">
```

To begin, add the class one to the first marker div element.
 
```html  
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker one">
      </div>
      <div class="marker">
      </div>
      <div class="marker">
      </div>
    </div>
  </body>
</html>
```

# Step 17
Next, remove the background-color property and its value from the .marker CSS rule.

```css  
h1 {
  text-align: center;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}
```

# Step 18
Then, create a new CSS rule that targets the class one and set its background-color property to red.

```css  
h1 {
  text-align: center;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color:red;
}
```

# Step 19
Add the class two to the second marker div, and the class three to the third marker div.

```html  
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>CSS Color Markers</h1>
    <div class="container">
      <div class="marker one">
      </div>
      <div class="marker two">
      </div>
      <div class="marker three">
      </div>
    </div>
  </body>
</html>
```

# Step 20
Create a CSS rule that targets the class two and set its background-color property to green. Also, create a separate CSS rule that targets the class three and set its background-color to blue.

```css 
h1 {
  text-align: center;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: red;
}

.two {
  background-color:green;
}
.three {
  background-color:blue;
}
```

# Step 21
There are two main color models: the additive RGB (red, green, blue) model used in electronic devices, and the subtractive CMYK (cyan, magenta, yellow, black) model used in print.
In this project, you'll work with the RGB model. This means that colors begin as black, and change as different levels of red, green, and blue are introduced. An easy way to see this is with the CSS rgb function.
Create a new CSS rule that targets the class container and set its background-color to black with rgb(0, 0, 0).

```css  
h1 {
  text-align: center;
}

.container {
  background-color: rgb(0, 0, 0);
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: red;
}

.two {
  background-color: green;
}

.three {
  background-color: blue;
}
```

# Step 22
A function is a piece of code that can take an input and perform a specific action. The CSS rgb function accepts values, or arguments, for red, green, and blue, and produces a color:

```css
rgb(red, green, blue);
```

Each red, green, and blue value is a number from 0 to 255. 0 means that there's 0% of that color, and is black. 255 means that there's 100% of that color. In the .one CSS rule, replace the color keyword red with the rgb function. For the rgb function, set the value for red to 255, the value for green to 0, and the value for blue to 0.
  
```css 
h1 {
  text-align: center;
}

.container {
  background-color: rgb(0, 0, 0);
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: green;
}

.three {
  background-color: blue;
}
```

# Step 23
Notice that the background-color for your marker is still red. This is because you set the red value of the rgb function to the max of 255, or 100% red, and set both the green and blue values to 0.
Now use the rgb function to set the other colors.
In the .two CSS rule, use the rgb function to set the background-color to the max value for green, and 0 for the other values. And in the .three CSS rule, use the rgb function to set the background-color to the max value for blue, and 0 for the other values.

```css
h1 {
  text-align: center;
}

.container {
  background-color: rgb(0, 0, 0);
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 255, 0);
}

.three {
  background-color: rgb(0, 0, 255);
}
```

# Step 24
While the red and blue markers look the same, the green one is much lighter than it was before. This is because the green color keyword is actually a darker shade, and is about halfway between black and the maximum value for green.
In the .two CSS rule, set the green value in the rgb function to 127 to lower its intensity.

```css
.two {
  background-color: rgb(0, 127, 0);
}
```

# Step 25
Now add a little more vertical space between your markers and the edge of the container element they're in.
In the .container CSS rule, use the shorthand padding property to add 10px of top and bottom padding, and set the left and right padding to 0. This works similarly to the shorthand margin property you used earlier.

```css
h1 {
  text-align: center;
}

.container {
  background-color: rgb(0, 0, 0);
  padding:10px 0px;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 127, 0);
}

.three {
  background-color: rgb(0, 0, 255);
}
```

# Step 26
In the additive RGB color model, primary colors are colors that, when combined, create pure white. But for this to happen, each color needs to be at its highest intensity.
Before you combine colors, set your green marker back to pure green. For the rgb function in the .two CSS rule, set green back to the max value of 255.

```css
h1 {
  text-align: center;
}

.container {
  background-color: rgb(0, 0, 0);
  padding: 10px 0;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 255, 0);
}

.three {
  background-color: rgb(0, 0, 255);
}
```

# Step 27
Now that you have the primary RGB colors, it's time to combine them.
For the rgb function in the .container rule, set the red, green, and blue values to the max of 255.
  
```css
h1 {
  text-align: center;
}

.container {
  background-color: rgb(255, 255, 255);
  padding: 10px 0;
}

.marker {
  width: 200px;
  height: 25px;
  margin: 10px auto;
}

.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 255, 0);
}

.three {
  background-color: rgb(0, 0, 255);
}
```

# Step 28
Secondary colors are the colors you get when you combine primary colors. You might have noticed some secondary colors in the last step as you changed the red, green, and blue values.
To create the first secondary color, yellow, update the rgb function in the .one CSS rule to combine pure red and pure green.
  
```css
.one {
  background-color: rgb(255, 255, 0);
}
```

# Step 29
To create the next secondary color, cyan, update the rgb function in the .two CSS rule to combine pure green and pure blue.

```html
.two {
  background-color: rgb(0, 255, 255);
}
```

# Step 30
To create the final secondary color, magenta, update the rgb function in the .three CSS rule to combine pure blue and pure red.
  
```html
.three {
  background-color: rgb(255, 0, 255);
}
```

# Step 31
Now that you're familiar with secondary colors, you'll learn how to create tertiary colors. Tertiary colors are created by combining a primary with a nearby secondary color.
To create the tertiary color orange, update the rgb function in the .one CSS rule so that red is at the max value, and set green to 127.

```html
.one {
  background-color: rgb(255, 127, 0);
}
```

# Step 32
Notice that, to create orange, you had to increase the intensity of red and decrease the intensity of the green rgb values. This is because orange is the combination of red and yellow, and falls between the two colors on the color wheel.
To create the tertiary color spring green, combine cyan with green. Update the rgb function in the .two CSS rule so that green is at the max value, and set blue to 127.

```html
.two {
  background-color: rgb(0, 255, 127);
}
```

# Step 33
And to create the tertiary color violet, combine magenta with blue. Update the rgb function in the .three CSS rule so that blue is at the max value, and set red to 127.
  
```html  
.three {
  background-color: rgb(127, 0, 255);
}
```