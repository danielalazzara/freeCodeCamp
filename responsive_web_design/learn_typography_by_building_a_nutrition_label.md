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

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Step 1
We've provided a basic HTML boilerplate for you. Create an h1 element within your body element and give it the text Nutrition Facts.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
</head>

<body>
  <h1>Nutrition Facts</h1>
</body>
</html>
```

# Step 2
Below your h1 element, add a p element with the text 8 servings per container.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
</head>

<body>
  <h1>Nutrition Facts</h1>
  <p>8 servings per container</p>
</body>
</html>
```

# Step 3
Add a second p element with the text Serving size 2/3 cup (55g).

```html
<body>
  <h1>Nutrition Facts</h1>
  <p>8 servings per container</p>
  <p>Serving size 2/3 cup (55g)</p>
</body>
```

# Step 4
Within your head element, add a link element with the rel attribute set to stylesheet and the href attribute set to https://fonts.googleapis.com/css?family=Open+Sans:400,700,800. This will import the Open Sans font family, with the font weight values 400, 700, and 800. Also add a link element to link your styles.css file.

```html
<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800" />
  <link rel="stylesheet" href="styles.css" />
</head>
```

# Step 5
Create a body selector and give it a font-family set to Open Sans with a fallback of sans-serif. Remember that fonts with spaces in the name must be wrapped in quotes for CSS.

```css
body {
  font-family: 'Open Sans', sans-serif;
}
```

# Step 6
The font is a bit small. Create an html selector and set the font to have a size of 16px.

```css
html {
  font-size: 16px;
}

body {
  font-family: 'Open Sans', sans-serif;
}
```

# Step 7
Wrap your h1 and p elements in a div element. Give that div a class attribute set to label.

```html
<body>
  <div class="label">
    <h1>Nutrition Facts</h1>
    <p>8 servings per container</p>
    <p>Serving size 2/3 cup (55g)</p>
  </div>
</body>
```

# Step 8
Borders can be used to group and prioritize content. Create a .label selector and give it a border set to 2px solid black.

```css
.label {
  border: 2px solid black;
}
```

# Step 9
Good use of white space can bring focus to the important elements of your page, and help guide your user's eyes through your text. Give your .label selector a width property set to 270px.

```css
.label {
  border: 2px solid black;
  width: 270px;
}
```

# Step 10
Give your .label selector a margin property set to 20px auto, and a padding property set to 0 7px.

```css
.label {
  border: 2px solid black;
  width: 270px;
  margin: 20px auto;
  padding: 0 7px;
}
```

# Step 11
If you inspect your .label element with your browser's developer tools, you may notice that it's actually 288 pixels wide instead of 270. This is because, by default, the browser includes the border and padding when determining an element's size. To solve this, reset the box model by creating a * selector and giving it a box-sizing property of border-box.

```css
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.label {
  border: 2px solid black;
  width: 270px;
  margin: 20px auto;
  padding: 0 7px;
}
```

# Step 12
Remember that the use of h1, h2, and similar tags determine the semantic structure of your HTML. However, you can adjust the CSS of these elements to control the visual flow and hierarchy. Create an h1 rule and set the font-weight property to 800. This will make your h1 text bolder.

```css
h1 {
  font-weight: 800;
}
```

# Step 13
Give your h1 selector a text-align property of center.

```css
h1 {
  font-weight: 800;
  text-align: center;
}
```

# Step 14
Fine-tune the placement of your h1 by giving it a top and bottom margin of -4px and a left and right margin of 0.

```css
h1 {
  font-weight: 800;
  text-align: center;
  margin: -4px 0;
}
```

# Step 15
Create a p selector and remove all margins.

```css
p {
  margin: 0;
}
```

# Step 16
Lines can help separate and group important content, especially when space is limited. Create a div element below your h1 element, and give it a class attribute set to divider.

```html
  <div class="label">
    <h1>Nutrition Facts</h1>
    <div class="divider"></div> 
    <p>8 servings per container</p>
    <p>Serving size 2/3 cup (55g)</p>
  </div>
```

# Step 17
Create a selector for your new .divider and set the border-bottom property to 1px solid #888989. Also give it a top and bottom margin of 2px. It should not have any left or right margin.

```css
.divider {
  border-bottom: 1px solid #888989;
  margin: 2px 0;
}
```

# Step 18
The letter-spacing property can be used to adjust the space between each character of text in an element. Give your h1 selector a letter-spacing property set to 0.15px to space them out a bit more.

```css
h1 {
  font-weight: 800;
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px;
}
```

# Step 19
Nutrition labels have a lot of bold text to draw attention to important information. Rather than targeting each element that needs to be bold, it is more efficient to use a class to apply the bold styling to every element. Give your second p element a class attribute set to bold.

```html
  <div class="label">
    <h1>Nutrition Facts</h1>
    <div class="divider"></div>
    <p>8 servings per container</p>
    <p class="bold">Serving size 2/3 cup (55g)</p>
  </div>
```

# Step 20
Your new class does not have any styling yet. Create a .bold selector and give it a font-weight property set to 800 to make the text bold. Go ahead and remove the font-weight property from your h1 selector as well.

```css
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.label {
  border: 2px solid black;
  width: 270px;
  margin: 20px auto;
  padding: 0 7px;
}

h1 {
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px;
}

p {
  margin: 0;
}

.divider {
  border-bottom: 1px solid #888989;
  margin: 2px 0;
}

.bold {
  font-weight: 800;
}
```

# Step 21
Give your h1 element a class attribute set to bold. This will make the text bold again.

```html
  <div class="label">
    <h1 class="bold">Nutrition Facts</h1>
    <div class="divider"></div>
    <p>8 servings per container</p>
    <p class="bold">Serving size 2/3 cup (55g)</p>
  </div>
```

# Step 22
Horizontal spacing between equally important elements can increase the readability of your text. Wrap the text 2/3 cup (55g) in a span element.

```html
  <div class="label">
    <h1 class="bold">Nutrition Facts</h1>
    <div class="divider"></div>
    <p>8 servings per container</p>
    <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
  </div>
```

# Step 23
Now we can add the horizontal spacing using flex. In your p selector, add a display property set to flex and a justify-content property set to space-between.

```css
p {
  margin: 0;
  display: flex;
  justify-content: space-between;
}
```

# Step 24
Wrap everything within the .label element in a new header element.

```html
  <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
  </div>
```

# Step 25
Now update your h1 selector to be header h1 to specifically target your h1 element within your new header.

```css
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.label {
  border: 2px solid black;
  width: 270px;
  margin: 20px auto;
  padding: 0 7px;
}

header h1 {
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px
}

p {
  margin: 0;
  display: flex;
  justify-content: space-between;
}

.divider {
  border-bottom: 1px solid #888989;
  margin: 2px 0;
}

.bold {
  font-weight: 800;
}
```

# Step 26
Create a new div element below your header element, and give it a class attribute set to divider large.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800" rel="stylesheet">
  <link href="./styles.css" rel="stylesheet">
</head>

<body>
  <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
    <div class="divider large"></div>
  </div>
</body>
</html>
```

# Step 27
Create a new .large selector and give it a height property set to 10px. Also create an .large, .medium selector and set the background-color property to black.

```css
.large {
  height:10px;
}

.large, .medium {
  background-color:black;
}
```

# Step 28
You may notice there is still a small border at the bottom of your .large element. To reset this, give your .large, .medium selector a border property set to 0. Note: the medium(medium) class will be utilized in step 37 for the thinner bars of the nutrition label.

```css
.large, .medium {
  background-color: black;
  border: 0;
}
```

# Step 29
Create a new div below your .large element and give it a class attribute set to calories-info.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800" rel="stylesheet">
  <link href="./styles.css" rel="stylesheet">
</head>

<body>
  <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
    <div class="divider large"></div>
    <div class="calories-info"></div>
  </div>
</body>
</html>
```

# Step 30
Within your .calories-info element, create a div element. Give that div element a class attribute set to left-container. Within the newly created div element, create a h2 element with the text Amount per serving. Give the h2 element a class attribute set to bold small-text.

```html
    <div class="calories-info">
      <div class="left-container">
        <h2 class="bold small-text">Amount per serving</h2>
      </div>
    </div>
```

# Step 31
The rem unit stands for root em, and is relative to the font size of the html element. Create an .small-text selector and set the font-size to 0.85rem, which would calculate to be roughly 13.6px (remember that you set your html to have a font-size of 16px).

```css
.small-text {
  font-size: 0.85rem;
}
```

# Step 32
Create a .calories-info h2 selector and remove all margins.

```css
.calories-info h2 {
  margin: 0;
}
```

# Step 33
Below your .small-text element, create a new p element with the text Calories. Also below the .left-container element, create a new span element with the text 230.

```html
    <div class="calories-info">
      <div class="left-container">
        <h2 class="bold small-text">Amount per serving</h2>
        <p>Calories</p>
      </div>
      <span>230</span>
    </div>
```

# Step 34
Create a new .calories-info selector and give it a display property set to flex. Also give it a justify-content property set to space-between and align-items property set to flex-end.

```css
.calories-info {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}
```

# Step 35
Create a new .left-container p selector setting the top and bottom margin to -5px, and the left and right margin to -2px. Also set the font-size to 2em and font-weight to 700.

```css
.left-container p {
  margin: -5px -2px;
  font-size: 2em;
  font-weight: 700;
}
```

# Step 36
Create a .calories-info span selector, set its font-size to 2.4em and font-weight to 700.

```css
.calories-info span {
  font-size: 2.4em;
  font-weight: 700;
}
```

# Step 37
Typography is often more art than science. You may have to tweak things like alignment until it looks correct. Give your .calories-info span selector a margin set to -7px -2px. This will shift your 230 text into place.

```css
.calories-info span {
  font-size: 2.4em;
  font-weight: 700;
  margin: -7px -2px;
}
```

# Step 38
Below your .calories-info element, add a div with the class attribute set to divider medium.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800" rel="stylesheet">
  <link href="./styles.css" rel="stylesheet">
</head>

<body>
  <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
    <div class="divider large"></div>
    <div class="calories-info">
      <div class="left-container">
        <h2 class="bold small-text">Amount per serving</h2>
        <p>Calories</p>
      </div>
      <span>230</span>
    </div>
    <div class="divider medium"></div>
  </div>
</body>
</html>
```

# Step 39
Create an .medium selector and give it a height property of 5px.

```css
.medium {
  height: 5px;
}
```

# Step 40
Create a new div element below your .medium element. Give it a class attribute set to daily-value small-text. Within this new div, add a p element with the text % Daily Value *, and set the class attribute to bold right.

```html
    <div class="divider medium"></div>
    <div class="daily-value small-text">
      <p class="bold right">% Daily Value *</p>
    </div>
```

# Step 41
The text * Daily Value % should be aligned to the right. Create a .right selector and use the justify-content property to do it.

```css
.right {
  justify-content: flex-end;
}
```

# Step 42
Use your existing .divider element as an example to add a new divider after the p element.

```html
    <div class="daily-value small-text">
      <p class="bold right">% Daily Value *</p>
      <div class="divider"></div>
    </div>
```

# Step 43
After your last .divider element, create a p element and give it the text Total Fat 8g 10%. Wrap the text Total Fat in a span element with the class of bold. Wrap the text 10% in another span element with the class of bold. Finally, nest the Total Fat span element and the text 8g in an additional span element for alignment.

```html
    <div class="daily-value small-text">
      <p class="bold right">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span><span class="bold">10%</span></p>
    </div>
```

# Step 44
Below your element with the Total Fat text, create a new p element with the text Saturated Fat 1g 5%. Wrap the 5% in a span with the class attribute set to bold. In this case this is enough to align the percentage to 5%.

```html
    <div class="daily-value small-text">
      <p class="bold right">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p> Saturated Fat 1g <span class="bold">5%</span></p>
    </div>
```

# Step 45
This new p element will need to be indented. Give it a class set to indent.

```html
    <div class="daily-value small-text">
      <p class="bold right">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent">Saturated Fat 1g <span class="bold">5%</span></p>
    </div>
```

# Step 46
Create a new .indent selector and give it a margin-left property set to 1em.

```css
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.label {
  border: 2px solid black;
  width: 270px;
  margin: 20px auto;
  padding: 0 7px;
}

header h1 {
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px
}

p {
  margin: 0;
  display: flex;
  justify-content: space-between;
}

.divider {
  border-bottom: 1px solid #888989;
  margin: 2px 0;
}

.bold {
  font-weight: 800;
}

.large {
  height: 10px;
}

.large, .medium {
  background-color: black;
  border: 0;
}

.medium {
  height: 5px;
}

.small-text {
  font-size: 0.85rem;
}

.calories-info {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.calories-info h2 {
  margin: 0;
}

.left-container p {
  margin: -5px -2px;
  font-size: 2em;
  font-weight: 700;
}

.calories-info span {
  margin: -7px -2px;
  font-size: 2.4em;
  font-weight: 700;
}

.right {
  justify-content: flex-end;
}

.indent {
  margin-left: 1em;
}
```

# Step 47
Create a .daily-value p selector to target all of your p elements in the daily-value section. Give this new selector a border-bottom set to 1px solid #888989.

```css
.daily-value p {
  border-bottom: 1px solid #888989;
}
```

# Step 48
The bottom borders under your % Daily Value * and Saturated Fat 1g 5% elements do not extend the full width of the label. Add no-divider to the class for these two elements.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
    </div>
```

# Step 49
The :not pseudo-selector can be used to select all elements that do not match the given CSS rule.

```css
div:not(#example) {
  color: red;
}
```

The above selects all div elements without an id of example. Modify your .daily-value p selector to exclude the .no-divider elements.

```css
.daily-value p:not(.no-divider) {
  border-bottom: 1px solid #888989;
}
```

# Step 50
Now you will have to add separate dividers below your .no-divider elements. Your first .no-divider element has a .divider after it. Create another .divider after your second .no-divider element.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
    </div> 
```

# Step 51
After your last .divider, create another p element with the text Trans Fat 0g. Italicize the word Trans by wrapping it in an i element. Give the new p element the class attribute set to indent no-divider. Wrap Trans Fat 0g in a span element for alignment.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
    </div>  
```

# Step 52
Create another .divider after your last p element.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
    </div> 
```

# Step 53
After your last .divider, create a new p element with the text Cholesterol 0mg 0%. Wrap the text Cholesterol in a span element, and give that span element the class attribute set to bold. Wrap the text 0% in another span element, with the class set to bold. Finally, nest the Cholesterol and 0mg span elements inside an additional span element for alignment.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
    </div> 
```

# Step 54
Below your last p element, create another p element with the text Sodium 160mg 7%. Wrap the text Sodium in a span element with a class attribute set to bold. Wrap the 7% text in another span element with the class set to bold. Also add an additional span element around Sodium 160mg for aligning it correctly.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
    </div>  
```

# Step 55
Add another p element with the text Total Carbohydrate 37g 13%. Like before, use span elements to make the text Total Carbohydrate and 13% bold. Also add an additional span element to wrap the Total Carbohydrate 37g text in a span element so to have it aligned to the left, and 13% to the right.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
    </div>   
```

# Step 56
Below your last p element, add another p element with the text Dietary Fiber 4g. Give the p element the class necessary to indent it and remove the dividing border. Then create a divider below that p element.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
    </div> 
```

# Step 57
Create another p element after your last .divider, and give it the text Total Sugars 12g. Assign that p element the class values necessary to indent it and remove the bottom border. Then create another .divider below your new p element.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider"></div>
    </div>    
```

# Step 58
The advantage to creating these dividers is that you can apply specific classes to style them individually. Add double-indent to the class for your last .divider.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800" rel="stylesheet">
  <link href="./styles.css" rel="stylesheet">
</head>

<body>
  <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
    <div class="divider large"></div>
    <div class="calories-info">
      <div class="left-container">
        <h2 class="bold small-text">Amount per serving</h2>
        <p>Calories</p>
      </div>
      <span>230</span>
    </div>
    <div class="divider medium"></div>
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
    </div>    
  </div>
</body>
</html>
```

# Step 59
Create a .double-indent selector and give it a left margin of 2em.

```css
.double-indent  {
  margin-left: 2em;
}
```

# Step 60
Below your .double-indent element, add a new p element with the text Includes 10g Added Sugars 20%. Your new p element should also be double indented, and have no bottom border. Use a span to make the 20% bold and right aligned. Then create another divider after that p element.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
      <p class="double-indent no-divider">Includes 10g Added Sugars <span class="bold">20%</span></p>
      <div class="divider"></div>
    </div>
```

# Step 61
After your last divider, create another p element with the text Protein 3g. Use the necessary classes to remove the bottom border, and a span to make the Protein bold. Following this element, create a large divider.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
      <p class="double-indent no-divider">Includes 10g Added Sugars <span class="bold">20%</span>
      <div class="divider"></div>
      <p class="no-divider"><span class="bold">Protein</span> 3g</p>
      <div class="large divider"></div>
    </div>
```

# Step 62
Create another p element below your large divider. Give the p element the text Vitamin D 2mcg 10%. The p element contains only text, you can wrap the percentage in a span element so that it is considered a separate entity from the rest of the text, and it's moved to the right.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
      <p class="double-indent no-divider">Includes 10g Added Sugars <span class="bold">20%</span>
      <div class="divider"></div>
      <p class="no-divider"><span class="bold">Protein</span> 3g</p>
      <div class="divider large"></div>
      <p>Vitamin D 2mcg <span>10%</span></p>
    </div>
```

# Step 63
Create another p element, give it the text Calcium 260mg 20%. Align 20% to the right. Below that, create a p element with the text Iron 8mg 45%, aligning the 45% to the right.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
      <p class="double-indent no-divider">Includes 10g Added Sugars <span class="bold">20%</span>
      <div class="divider"></div>
      <p class="no-divider"><span class="bold">Protein</span> 3g</p>
      <div class="divider large"></div>
      <p>Vitamin D 2mcg <span>10%</span></p>
      <p>Calcium 260mg <span>20%</span></p>
      <p>Iron 8mg <span>45%</span></p>
    </div>
```

# Step 64
Create the final p element for your .daily-value section. Give it the text Potassium 235mg 6%. Align the 6% text to the right, and remove the bottom border of the p element.

```html
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
      <p class="double-indent no-divider">Includes 10g Added Sugars <span class="bold">20%</span>
      <div class="divider"></div>
      <p class="no-divider"><span class="bold">Protein</span> 3g</p>
      <div class="divider large"></div>
      <p>Vitamin D 2mcg <span>10%</span></p>
      <p>Calcium 260mg <span>20%</span></p>
      <p>Iron 8mg <span>45%</span></p>
      <p class="no-divider">Potassium 235mg <span>6%</span></p>
    </div>
```

# Step 65
Add a medium divider after your .daily-value element. Below that new divider, create a p element with the class attribute set to note. Give the p element the following text: * The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.

```html
    <div class="divider medium"></div>
    <p class="note">* The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.</p>
```

# Step 66
Create a .note selector, and set the size of the font to 0.6rem. Also set the top and bottom margins to 5px, removing the left and right margins.

```css
.note {
  font-size: 0.6rem;
  margin: 5px 0;
}
```

Step 67
Give the .note selector a left and right padding of 8px, removing the top and bottom padding. Also set the text-indent property to -8px.
With these last changes, your nutrition label is complete!

```css
* {
  box-sizing: border-box;
}

html {
  font-size: 16px;
}

body {
  font-family: 'Open Sans', sans-serif;
}

.label {
  border: 2px solid black;
  width: 270px;
  margin: 20px auto;
  padding: 0 7px;
}

header h1 {
  text-align: center;
  margin: -4px 0;
  letter-spacing: 0.15px
}

p {
  margin: 0;
  display: flex;
  justify-content: space-between;
}

.divider {
  border-bottom: 1px solid #888989;
  margin: 2px 0;
}

.bold {
  font-weight: 800;
}

.large {
  height: 10px;
}

.large, .medium {
  background-color: black;
  border: 0;
}

.medium {
  height: 5px;
}

.small-text {
  font-size: 0.85rem;
}


.calories-info {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

.calories-info h2 {
  margin: 0;
}

.left-container p {
  margin: -5px -2px;
  font-size: 2em;
  font-weight: 700;
}

.calories-info span {
  margin: -7px -2px;
  font-size: 2.4em;
  font-weight: 700;
}

.right {
  justify-content: flex-end;
}

.indent {
  margin-left: 1em;
}

.double-indent {
  margin-left: 2em;
}

.daily-value p:not(.no-divider) {
  border-bottom: 1px solid #888989;
}

.note {
  font-size: 0.6rem;
  margin: 5px 0;
  padding: 0 8px;
  text-indent: -8px;
}
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Nutrition Label</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700,800" rel="stylesheet">
  <link href="./styles.css" rel="stylesheet">
</head>

<body>
  <div class="label">
    <header>
      <h1 class="bold">Nutrition Facts</h1>
      <div class="divider"></div>
      <p>8 servings per container</p>
      <p class="bold">Serving size <span>2/3 cup (55g)</span></p>
    </header>
    <div class="divider large"></div>
    <div class="calories-info">
      <div class="left-container">
        <h2 class="bold small-text">Amount per serving</h2>
        <p>Calories</p>
      </div>
      <span>230</span>
    </div>
    <div class="divider medium"></div>
    <div class="daily-value small-text">
      <p class="bold right no-divider">% Daily Value *</p>
      <div class="divider"></div>
      <p><span><span class="bold">Total Fat</span> 8g</span> <span class="bold">10%</span></p>
      <p class="indent no-divider">Saturated Fat 1g <span class="bold">5%</span></p>
      <div class="divider"></div>
      <p class="indent no-divider"><span><i>Trans</i> Fat 0g</span></p>
      <div class="divider"></div>
      <p><span><span class="bold">Cholesterol</span> 0mg</span> <span class="bold">0%</span></p>
      <p><span><span class="bold">Sodium</span> 160mg</span> <span class="bold">7%</span></p>
      <p><span><span class="bold">Total Carbohydrate</span> 37g</span> <span class="bold">13%</span></p>
      <p class="indent no-divider">Dietary Fiber 4g</p>
      <div class="divider"></div>
      <p class="indent no-divider">Total Sugars 12g</p>
      <div class="divider double-indent"></div>
      <p class="double-indent no-divider">Includes 10g Added Sugars <span class="bold">20%</span>
      <div class="divider"></div>
      <p class="no-divider"><span class="bold">Protein</span> 3g</p>
      <div class="divider large"></div>
      <p>Vitamin D 2mcg <span>10%</span></p>
      <p>Calcium 260mg <span>20%</span></p>
      <p>Iron 8mg <span>45%</span></p>
      <p class="no-divider">Potassium 235mg <span>6%</span></p>
    </div>
    <div class="divider medium"></div>
    <p class="note">* The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily
      diet. 2,000 calories a day is used for general nutrition advice.</p>
  </div>
</body>
</html>
```
