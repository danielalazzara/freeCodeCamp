# Step 73
Opacity describes how opaque, or non-transparent, something is. For example, a solid wall is opaque, and no light can pass through. But a drinking glass is much more transparent, and you can see through the glass to the other side.
With the CSS opacity property, you can control how opaque or transparent an element is. With the value 0, or 0%, the element will be completely transparent, and at 1.0, or 100%, the element will be completely opaque like it is by default.
In the .sleeve CSS rule, set the opacity property to 0.5.

```html
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
  background-color: white;
  opacity: 0.5;
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

# Step 74
Another way to set the opacity for an element is with the alpha channel. Similar to the opacity property, the alpha channel controls how transparent or opaque a color is.
You've already set sleeve's opacity with a named color and the opacity property, but you can add an alpha channel to the other CSS color properties.
Inside the .sleeve rule, remove the opacity property and value.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: white;
}
```

# Step 75
You're already familiar with using the rgb function to set colors. To add an alpha channel to an rgb color, use the rgba function instead. The rgba function works just like the rgb function, but takes one more number from 0 to 1.0 for the alpha channel:

```html
rgba(redValue, greenValue, blueValue, alphaValue);
```

In the .sleeve rule, use the rgba function to set the background-color property to pure white with 50% opacity.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
}
```

# Step 76
Your sleeve is looking good, but it would look even better if it was positioned more toward the right side of the marker. One way to do that is to add another element before the sleeve to push it to the right.
Add a new div with the class cap before the sleeve div element.

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
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker green">
      </div>
      <div class="marker blue">
      </div>
    </div>
  </body>
</html>
```

# Step 77
Create a new CSS rule to target the class cap. In the new rule, set the width property to 60px, and the height to 25px.

```html
.cap {
  width: 60px;
  height: 25px;
}
```

# Step 78
It looks like your sleeve disappeared, but don't worry -- it's still there. What happened is that your new cap div is taking up the entire width of the marker, and is pushing the sleeve down to the next line. This is because the default display property for div elements is block. So when two block elements are next to each other, they stack like actual blocks. For example, your marker elements are all stacked on top of each other.
To position two div elements on the same line, set their display properties to inline-block. Create a new rule to target both the cap and sleeve classes, and set display to inline-block.

```html
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

.cap {
  width: 60px;
  height: 25px;
}

.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
}

.cap, .sleeve {
  display: inline-block;
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

# Step 79
In the last project, you learned a little bit about borders and the border-color property. All HTML elements have borders, though they're usually set to none by default. With CSS, you can control all aspects of an element's border, and set the border on all sides, or just one side at a time. For a border to be visible, you need to set its width and style.
In the .sleeve CSS rule, add the border-left-width property with the value 10px.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left-width: 10px;
}
```

# Step 80
Borders have several styles to choose from. You can make your border a solid line, but you can also use a dashed or dotted line if you prefer. Solid border lines are probably the most common.
In the .sleeve CSS rule, add the border-left-style property with the value solid.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left-width: 10px;
  border-left-style: solid;
}
```

# Step 81
Your border should be visible now. If no color is set, black is used by default. But to make your code more readable, it's better to set the border color explicitly.
In the .sleeve CSS rule, add the border-left-color property with the value black.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left-width: 10px;
  border-left-style: solid;
  border-left-color: black;
}
```

# Step 82
The border-left shorthand property lets you to set the left border's width, style, and color at the same time.
Here is the syntax:

```html
border-left: width style color;
```

In the .sleeve CSS rule, replace the border-left-width, border-left-style, and border-left-color properties with the border-left shorthand property. The values for the width, style, and color of the left border should be the same.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left: 10px solid black;
}
```

# Step 83
Your marker is looking good. But to make it look even more realistic, you can change the border style to double solid borders. For the border-left shorthand property, change the border style value from solid to double.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left: 10px double black;
}
```

# Step 84
The black color of your border looks pretty harsh against the more transparent sleeve. You can use an alpha channel to lower the opacity of the black border.
For the border-left shorthand property, use the rgba function to set the color value to pure black with 75% opacity.

```html
.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left: 10px double rgba(0, 0, 0, 0.75);
}
```

# Step 85
Awesome. Your red marker is looking good. Now all you need to do is add the caps and sleeves to your other markers.
Add a cap and sleeve to both the green and blue markers. You can just copy the div elements from the red marker and paste them into the other two markers.

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
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker green">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker blue">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
    </div>
  </body>
</html>
```

# Step 86
The last thing you'll do is add a slight shadow to each marker to make them look even more realistic.
The box-shadow property lets you apply one or more shadows around an element. Here is basic syntax:

```html
box-shadow: offsetX offsetY color;
```
Start by adding a simple shadow to the red marker. In the .red CSS rule, add the box-shadow property with the values 5px for offsetX, 5px for offsetY, and red for color.

```html
.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
  box-shadow: 5px 5px red;
}
```

# Step 87
As you can see, you added a simple red shadow around your marker that's 5 pixels to the right, and 5 pixels down. But what if you wanted to position your shadow on the opposite side? You can do that by using negative values for offsetX and offsetY.
Update the values for the box-shadow property, and set offsetX to -5px, and offsetY to -5px.

```html
.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
  box-shadow: -5px -5px red;
}
```

# Step 88
Notice that the edges of the shadow are sharp. This is because there is an optional blurRadius value for the box-shadow property: box-shadow: offsetX offsetY blurRadius color; If a blurRadius value isn't included, it defaults to 0 and produces sharp edges. The higher the value of blurRadius, the greater the blurring effect is.
In the .green CSS rule, add the box-shadow property with the values 5px for offsetX, 5px for offsetY, 5px for blurRadius, and green for color.

```html
.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
  box-shadow: 5px 5px 5px green;
}
```

# Step 89
But what if you wanted to expand the shadow out further? You can do that with the optional spreadRadius value: box-shadow: offsetX offsetY blurRadius spreadRadius color; Like blurRadius, spreadRadius defaults to 0 if it isn't included.
Practice by adding a 5 pixel shadow directly around the blue marker.
In the .blue CSS rule, add the box-shadow property with the values 0 for offsetX, 0 for offsetY, 0 for blurRadius, 5px for spreadRadius, and blue for color.

```html
.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
  box-shadow: 0 0 0 5px blue;
}
```

# Step 90
Now that you're familiar with the box-shadow property you can finalize the shadows, starting with the one for the red marker.
In the .red CSS rule, update the values for the box-shadow property so offsetX is 0,offsetY is 0, blurRadius is 20px, spreadRadius is 0, and color is red.

```html
.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
  box-shadow: 0 0 20px 0 red;
}
```

# Step 91
Next, update the color value of the red marker's box-shadow property. Replace the named color with the rgba function. Use the values 83 for red, 14 for green, 14 for blue and 0.8 for the alpha channel.

```html
.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
  box-shadow: 0 0 20px 0 rgba(83, 14, 14, 0.8);
}
```

# Step 92
The shadows for your green and blue markers will have the same position, blur, and spread. The only difference will be the colors.
In the .green and .blue CSS rules, update the values for the box-shadow properties so offsetX is 0,offsetY is 0, blurRadius is 20px, and spreadRadius is 0. Leave the colors as green and blue for now.

```html
.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
  box-shadow: 0 0 20px 0 green;
}

.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
  box-shadow: 0 0 20px 0 blue;
}
```

# Step 93
For the green marker's box-shadow property, replace the named color with a hex color code. Use the values 3B for red, 7E for green, 20 for blue, and CC for the alpha channel.

```html
.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
  box-shadow: 0 0 20px 0 #3B7E20CC;
}
```

# Step 94
Finally, for the blue marker's box-shadow property, replace the named color with the hsla function. Use the values 223 for hue, 59% for saturation, 31% for lightness, and 0.8 for the alpha channel. And with that, your set of colored markers is complete! Well done.

```html
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

.cap {
  width: 60px;
  height: 25px;
}

.sleeve {
  width: 110px;
  height: 25px;
  background-color: rgba(255, 255, 255, 0.5);
  border-left: 10px double rgba(0, 0, 0, 0.75);
}

.cap, .sleeve {
  display: inline-block;
}

.red {
  background: linear-gradient(rgb(122, 74, 14), rgb(245, 62, 113), rgb(162, 27, 27));
  box-shadow: 0 0 20px 0 rgba(83, 14, 14, 0.8);
}

.green {
  background: linear-gradient(#55680D, #71F53E, #116C31);
  box-shadow: 0 0 20px 0 #3B7E20CC;
}

.blue {
  background: linear-gradient(hsl(186, 76%, 16%), hsl(223, 90%, 60%), hsl(240, 56%, 42%));
  box-shadow: 0 0 20px 0 hsla(223, 59%, 31%, 0.8);
}
```html

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
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker green">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
      <div class="marker blue">
        <div class="cap"></div>
        <div class="sleeve"></div>
      </div>
    </div>
  </body>
</html>
```
