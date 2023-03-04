# Step 34
There are three more tertiary colors: chartreuse green (green + yellow), azure (blue + cyan), and rose (red + magenta).
To create chartreuse green, update the rgb function in the .one rule so that red is at 127, and set green to the max value.
For azure, update the rgb function in the .two rule so that green is at 127 and blue is at the max value. And for rose, which is sometimes called bright pink, update the rgb function in the .three rule so that blue is at 127 and red is at the max value.

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
  background-color: rgb(127, 255, 0);
}

.two {
  background-color: rgb(0, 127, 255);
}

.three {
  background-color: rgb(255, 0, 127);
}
```

# Step 35
Now that you've gone through all the primary, secondary, and tertiary colors on a color wheel, it'll be easier to understand other color theory concepts and how they impact design.
First, in the rules .one, .two, and .three, adjust the values in the rgb function so that the background-color of each element is set to pure black. Remember that the rgb function uses the additive color model, where colors start as black and change as the values of red, green, and blue increase.

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
  background-color: rgb(0, 0, 0);
}

.two {
  background-color: rgb(0, 0, 0);
}

.three {
  background-color: rgb(0, 0, 0);
}
```

# Step 36
A color wheel is a circle where similar colors, or hues, are near each other, and different ones are further apart. For example, pure red is between the hues rose and orange.
Two colors that are opposite from each other on the color wheel are called complementary colors. If two complementary colors are combined, they produce gray. But when they are placed side-by-side, these colors produce strong visual contrast and appear brighter.
In the rgb function for the .one CSS rule, set the red value to the max of 255 to produce pure red. In the rgb function for .two CSS rule, set the values for green and blue to the max of 255 to produce cyan.

```css
.one {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 255, 255);
}
```

# Step 37
Notice that the red and cyan colors are very bright right next to each other. This contrast can be distracting if it's overused on a website, and can make text hard to read if it's placed on a complementary-colored background. It's better practice to choose one color as the dominant color, and use its complementary color as an accent to bring attention to certain content on the page.
First, in the h1 rule, use the rgb function to set its background color to cyan.

```css
h1 {
  text-align: center;
  background-color: rgb(0, 255, 255)
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
  background-color: rgb(0, 255, 255);
}

.three {
  background-color: rgb(0, 0, 0);
}
```

# Step 38
Next, in the .one rule, use the rgb function to set the background-color to black. And in the .two rule, use the rgb function to set the background-color to red.

```css
.one {
  background-color: rgb(0, 0, 0);
}

.two {
  background-color: rgb(255, 0, 0);
}
```

# Step 39
Notice how your eyes are naturally drawn to the red color in the center? When designing a site, you can use this effect to draw attention to important headings, buttons, or links.
There are several other important color combinations outside of complementary colors, but you'll learn those a bit later. For now, use the rgb function in the .two rule to set the background-color to black.

```css
.two {
  background-color: rgb(0, 0, 0);
}
```

# Step 40
And in the h1 rule, remove the background-color property and value to go back to the default white color.

```css
h1 {
  text-align: center;
}
```

# Step 41
Now it's time to add other details to the markers, starting with the first one.
In the first marker div element, change the class one to red.

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
      <div class="marker red">
      </div>
      <div class="marker two">
      </div>
      <div class="marker three">
      </div>
    </div>
  </body>
</html>
```

# Step 42
Update the .one class selector to target the new red class.

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

.red {
  background-color: rgb(0, 0, 0);
}

.two {
  background-color: rgb(0, 0, 0);
}

.three {
  background-color: rgb(0, 0, 0);
}

# Step 43
# And update the rgb function in the .red rule so that the red value is at the max.

.red {
  background-color: rgb(255, 0, 0);
}

.two {
  background-color: rgb(0, 0, 0);
}

.three {
  background-color: rgb(0, 0, 0);
}
```

# Step 44
Next, change the class two to green in the second marker div, and the class three to blue in the third marker div.

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
      <div class="marker red">
      </div>
      <div class="marker green">
      </div>
      <div class="marker blue">
      </div>
    </div>
  </body>
</html>
```

# Step 45
Update the CSS class selector .two so it targets the new green class. And update the .three selector so it targets the new blue class.

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

.red {
  background-color: rgb(255, 0, 0);
}

.green {
  background-color: rgb(0, 0, 0);
}

.blue {
  background-color: rgb(0, 0, 0);
}
```

# Step 46
A very common way to apply color to an element with CSS is with hexadecimal or hex values. While hex values sound complicated, they're really just another form of RGB values.
Hex color values start with a # character and take six characters from 0-9 and A-F. The first pair of characters represent red, the second pair represent green, and the third pair represent blue. For example, #4B5320.
In the .green CSS rule, set the background-color property to a hex color code with the values 00 for red, FF for green, and 00 blue.

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

.red {
  background-color: rgb(255, 0, 0);
}

.green {
  background-color: #00FF00;
}

.blue {
  background-color: rgb(0, 0, 0);
}
```

# Step 47
You may already be familiar with decimal, or base 10 values, which go from 0 - 9. Hexadecimal, or base 16 values, go from 0 - 9, then A - F: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F With hex colors, 00 is 0% of that color, and FF is 100%. So #00FF00 translates to 0% red, 100% green, and 0% blue, and is the same as rgb(0, 255, 0).
Lower the intensity of green by setting green value of the hex color to 7F.

```css
.green {
  background-color: #007F00;
}
```

# Step 48

The HSL color model, or hue, saturation, and lightness, is another way to represent colors. The CSS hsl function accepts 3 values: a number from 0 to 360 for hue, a percentage from 0 to 100 for saturation, and a percentage from 0 to 100 for lightness. If you imagine a color wheel, the hue red is at 0 degrees, green is at 120 degrees, and blue is at 240 degrees.
Saturation is the intensity of a color from 0%, or gray, to 100% for pure color. Lightness is how bright a color appears, from 0%, or complete black, to 100%, complete white, with 50% being neutral.
In the .blue CSS rule, use the hsl function to change the background-color property to pure blue. Set the hue to 240, the saturation to 100%, and the lightness to 50%.

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

.red {
  background-color: rgb(255, 0, 0);
}

.green {
  background-color: #007F00;
}

.blue {
  background-color: hsl(240, 100%, 50%);
}
```

# Step 49
You've learned a few ways to set flat colors in CSS, but you can also use a color transition, or gradient, on an element. A gradient is when one color transitions into another. The CSS linear-gradient function lets you control the direction of the transition along a line, and which colors are used.
One thing to remember is that the linear-gradient function actually creates an image element, and is usually paired with the background property which can accept an image as a value.
In the .red CSS rule, change the background-color property to background.

```css
.red {
  background: rgb(255, 0, 0);
}
```

# Step 50
The linear-gradient function is very flexible -- here is the basic syntax you'll use in this tutorial: linear-gradient(gradientDirection, color1, color2, ...);
gradientDirection is the direction of the line used for the transition. color1 and color2 are color arguments, which are the colors that will be used in the transition itself. These can be any type of color, including color keywords, hex, rgb, or hsl.
Now you'll apply a red-to-green gradient along a 90 degree line to the first marker. First, in the .red CSS rule, set the background property to linear-gradient(), and pass it the value 90deg as the gradientDirection.

```css
.red {
  background: linear-gradient(90deg)
}
```

# Step 51
You'll use the rgb function for the colors of this gradient. In the linear-gradient function, use the rgb function to set the first color argument to pure red.

```css
.red {
  background: linear-gradient(90deg, rgb(255, 0, 0));
}
```

# Step 52
You won't see gradient yet because the linear-gradient function needs at least two color arguments to work. In the same linear-gradient function, use the rgb function to set the second color argument to pure green.

```css
.red {
  background: linear-gradient(90deg, rgb(255, 0, 0), rgb(0, 255, 0));
}
```

# Step 53
As you can see, the linear-gradient function produced a smooth red-green gradient. While the linear-gradient function needs a minimum of two color arguments to work, it can accept many color arguments.
Use the rgb function to add pure blue as the third color argument to the linear-gradient function.

```css
.red {
  background: linear-gradient(90deg, rgb(255, 0, 0), rgb(0, 255, 0), rgb(0, 0, 255));
}
```

# Step 54
Color-stops allow you to fine-tune where colors are placed along the gradient line. They are a length unit like px or percentages that follow a color in the linear-gradient function. For example, in this red-black gradient, the transition from red to black takes place at the 90% point along the gradient line, so red takes up most of the available space:

```css
linear-gradient(90deg, red 90%, black);
```

In the linear-gradient function, add a 75% color stop after the first red color argument. Do not add color stops to the other colors arguments.

```css
.red {
  background: linear-gradient(90deg, rgb(255, 0, 0) 75%, rgb(0, 255, 0), rgb(0, 0, 255));
}
```

# Step 55
Now that you know the basics of how the linear-gradient function and color-stops work, you can use them to make the markers look more realistic. In the linear-gradient function, set gradientDirection to 180deg.

```css
.red {
  background: linear-gradient(180deg, rgb(255, 0, 0) 75%, rgb(0, 255, 0), rgb(0, 0, 255));
}
```

# Step 56
Next, set the color-stop for red to 0%, the color-stop for green to 50%, and the color-stop for blue to 100%.

```css
red {
  background: linear-gradient(180deg, rgb(255, 0, 0) 0%, rgb(0, 255, 0) 50%, rgb(0, 0, 255) 100%);
}
```

# Step 57
Now that the color-stops are set, you'll apply different shades of red to each color argument in the linear-gradient function. The shades on the top and bottom edges of the marker will be darker, while the one in the middle will be lighter, as if there's a light above it.
For the first color argument, which is currently pure red, update the rgb function so the value for red is 122, the value for green is 74, and the value for blue is 14.

```css
.red {
  background: linear-gradient(180deg, rgb(122, 74, 14) 0%, rgb(0, 255, 0) 50%, rgb(0, 0, 255) 100%);
}
```

# Step 58
Now modify the second color argument in the linear-gradient function, which is currently pure green. Update the rgb function so the value for red is 245, the value of green is 62, and the value of blue is 113.

```css
.red {
  background: linear-gradient(180deg, rgb(122, 74, 14) 0%, rgb(245, 62, 113) 50%, rgb(0, 0, 255) 100%);
}
```

# Step 59
Finally, modify the third color argument in the linear-gradient function, which is currently pure blue. Update the rgb function so the value for red is 162, the value of green is 27, and the value of blue is 27.

```css
.red {
  background: linear-gradient(180deg, rgb(122, 74, 14) 0%, rgb(245, 62, 113) 50%, rgb(162, 27, 27) 100%);
}
```

# Step 60
The red marker is looking much more realistic. Now you'll do the same for the green marker, using a combination of the linear-gradient function and hex colors.
In the .green CSS rule, change the background-color property to background.

```css
.green {
  background: #007F00;
}
```

# Step 61
For this marker, you'll use hex color codes for your gradient.
Use the linear-gradient function and set gradientDirection to 180deg. And for the first color argument, use a hex color code with the values 55 for red, 68 for green, and 0D for blue.

```css
.green {
  background:  linear-gradient(180deg, #55680D);
}
```

# Step 62
For the second color argument, use a hex color code with the values 71 for red, F5 for green, and 3E for blue.

```css
.green {
  background: linear-gradient(180deg, #55680D, #71F53E);
}
```

# Step 63
That's looking better, but the bottom edge of the green marker needs to be darker to add a little more dimension.
In the same linear-gradient function, add a hex color code with the values 11 for red, 6C for green, and 31 for blue as the third color argument.

```css
.green {
  background: linear-gradient(180deg, #55680D, #71F53E, #116C31);
}
```

# Step 64
Even without the color-stops, you might have noticed that the colors for the green marker transition at the same points as the red marker. 
The first color is at the start (0%), the second is in the middle (50%), and the last is at the end (100%) of the gradient line. The linear-gradient function automatically calculates these values for you, and places colors evenly along the gradient line by default. In the .red CSS rule, remove the three color stops from the linear-gradient function to clean up your code a bit.

```css
.red {
  background: linear-gradient(180deg, rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
}
```

# Step 65
If no gradientDirection argument is provided to the linear-gradient function, it arranges colors from top to bottom, or along a 180 degree line, by default.
Clean up your code a little more by removing the gradientDirection argument from both linear-gradient functions.

```css
.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
}

.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
}
```

# Step 66
Now you'll apply a gradient to the blue marker, this time using the hsl function as color arguments. In the .blue CSS rule, change the background-color property to background.

```css
.blue {
  background: hsl(240, 100%, 50%);
}
```

# Step 67
Use the linear-gradient function, and pass in the hsl function with the values 186 for hue, 76% for saturation, and 16% for lightness as the first color argument.

```css
.blue {
  background: linear-gradient(hsl(186, 76%, 16%));
}
```

# Step 68
As the second color argument, pass in the hsl function with the values 223 for hue, 90% for saturation, and 60% for lightness.

```css
.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%));
}
```

# Step 69
And as the third color argument, pass in the hsl function with the values 240 for hue, 56% for saturation, and 42% for lightness.

```css
.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
}
```

# Step 70
Now that the markers have the correct colors, it's time to build the marker sleeves. Start with the red marker. Inside the red marker div, create a new div and give it a class of sleeve.

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
      <div class="marker red">
        <div class="sleeve">
        </div>
      </div>
      <div class="marker green">
      </div>
      <div class="marker blue">
      </div>
    </div>
  </body>
</html>
```

# Step 71
Create a new CSS rule that targets the class sleeve. Set the width property to 110px, and the height property to 25px.

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

.sleeve {
  width: 110px;
  height: 25px;
}

.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
}

.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
}

.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
}
```

# Step 72
To make the marker look more realistic, give the sleeve a transparent white color. First, set the sleeve element's background-color to white.

```css
.sleeve {
  width: 110px;
  height: 25px;
  background-color: white;
}
```
