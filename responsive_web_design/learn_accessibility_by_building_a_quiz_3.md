# Step 55
To make the first section look more inline, target only the input elements within .info elements, and set their width to 50%, and left-align their text.
 
```css 
.info input{
  width: 50%;
  text-align: left;
}              
```              
# Step 56
Target all label elements within .info elements, and set their width to 10%, and make it so they do not take up less than 55px.

```css
.info input {
  width: 50%;
  text-align: left;
}

.info label {
  width: 10%;
  min-width: 55px;
}              
```

# Step 57
To align the input boxes with each other, create a new ruleset that targets all input and label elements within an .info element and set the display property to inline-block. Also, align the label element's text to the right.

```css
.info input, .info label {
  display: inline-block;
}

.info input {
  width: 50%;
  text-align: left;
}

.info label {
  width: 10%;
  min-width: 55px;
  text-align: right;
}
```

# Step 58
To neaten the .question-block elements, set the following CSS properties:

```css
text-align: left;
display: block;
width: 100%;
margin-top: 20px;
padding-top: 5px;
```

```css
.question-block {
  text-align: left;
  display: block;
  width: 100%;
  margin-top: 20px;
  padding-top: 5px;
}
```

# Step 59
Make the paragraph elements appear as a higher priority, with the following CSS properties:

```css
margin-top: 5px;
padding-left: 15px;
font-size: 20px;
```

```css
p {
  margin-top: 5px;
  padding-left: 15px;
  font-size: 20px;
}
```

# Step 60
It is useful to see the default border around the fieldset elements, during development. However, it might not be the style you want. Remove the border and bottom padding on the .question elements.

```css
.question {
  border: none;
  padding-bottom: 0;
}
```

# Step 61
Remove the default styling for the list items of .answers-list, and remove the unordered list padding.

```css
 .answers-list {
   list-style: none;
   padding: 0;
 }
```

# Step 62
Give the submit button a freeCodeCamp-style design, with the following CSS properties:

```css
display: block;
margin: 40px auto;
width: 40%;
padding: 15px;
font-size: 23px;
background: #d0d0d5;
border: 3px solid #3b3b4f;
```
```css
button {
  display: block;
  margin: 40px auto;
  width: 40%;
  padding: 15px;
  font-size: 23px;
  background: #d0d0d5;
  border: 3px solid #3b3b4f;
}
```

# Step 63
Set the footer background color to #2a2a40, and use Flexbox to horizontally center the text.

```css
footer {
  background-color: #2a2a40;
  display: flex;
  justify-content: center;
}
```

# Step 64
Now, we cannot read the text. Target the footer and the anchor element within to set the font color to a color of adequate contrast ratio.

```css
footer, footer a {
  color: #dfdfe2;
}
```

# Step 65
Horizontally center all the text within the address element, and add some padding.

```css
address {
  text-align: center;
  padding: 0.3em;
}
```

# Step 66
Clicking on the navigation links should jump the viewport to the relevant section. However, this jumping can be disorienting for some users. Select all elements, and set the scroll-behavior to smooth.

```css
* {
  scroll-behavior: smooth;
}
```

# Step 67
Certain types of motion-based animations can cause discomfort for some users. In particular, people with vestibular disorders have sensitivity to certain motion triggers.
The @media at-rule has a media feature called prefers-reduced-motion to set CSS based on the user's preferences. It can take one of the following values:

```css
reduce
no-preference
@media (feature: value) {
  selector {
    styles
  }
}
```

Wrap the style rule that sets scroll-behavior: smooth within an @media at-rule with the media feature prefers-reduced-motion having no-preference set as the value.

```css
@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}
```

# Step 68
Finally, the navigation accessibility can be improved by providing keyboard shortcuts. The accesskey attribute accepts a space-separated list of access keys. For example:

```html
<button type="submit" accesskey="s">Submit</button>
```

Give each of the navigation links a single-letter access key.
Note: It is not always advised to use access keys, but they can be useful
Well done. You have completed the Accessibility Quiz practice project.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="freeCodeCamp Accessibility Quiz practice project" />
    <title>Accessibility Quiz</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <header>
      <img id="logo" src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg">
      <h1>HTML/CSS Quiz</h1>
      <nav>
        <ul>
          <li><a href="#student-info" <button type="submit" accesskey="s">Submit</button>INFO</a></li>
          <li><a href="#html-questions" <button type="submit" accesskey="h">Submit</button>HTML</a></li>
          <li><a href="#css-questions" <button type="submit" accesskey="c">Submit</button>CSS</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <form method="post" action="https://freecodecamp.org/practice-project/accessibility-quiz">
        <section role="region" aria-labelledby="student-info">
          <h2 id="student-info">Student Info</h2>
          <div class="info">
            <label for="student-name">Name:</label>
            <input type="text" name="student-name" id="student-name" />
          </div>
          <div class="info">
            <label for="student-email">Email:</label>
            <input type="email" name="student-email" id="student-email" />
          </div>
          <div class="info">
            <label for="birth-date">D.O.B.<span class="sr-only">(Date of Birth)</span></label>
            <input type="date" name="birth-date" id="birth-date" />
          </div>
        </section>
        <section role="region" aria-labelledby="html-questions">
          <h2 id="html-questions">HTML</h2>
          <div class="question-block">
            <p>1</p>
            <fieldset class="question" name="html-question-one">
              <legend>
                The legend element represents a caption for the content of its
                parent fieldset element
              </legend>
              <ul class="answers-list">
                <li>
                  <label for="q1-a1">
                    <input type="radio" id="q1-a1" name="q1" value="true" />
                    True
                  </label>
                </li>
                <li>
                  <label for="q1-a2">
                    <input type="radio" id="q1-a2" name="q1" value="false" />
                    False
                  </label>
                </li>
              </ul>
            </fieldset>
          </div>
          <div class="question-block">
            <p>2</p>
            <fieldset class="question" name="html-question-two">
              <legend>
                A label element nesting an input element is required to have a
                for attribute with the same value as the input's id
              </legend>
              <ul class="answers-list">
                <li>
                  <label for="q2-a1">
                    <input type="radio" id="q2-a1" name="q2" value="true" />
                    True
                  </label>
                </li>
                <li>
                  <label for="q2-a2">
                    <input type="radio" id="q2-a2" name="q2" value="false" />
                    False
                  </label>
                </li>
              </ul>
            </fieldset>
          </div>
        </section>
        <section role="region" aria-labelledby="css-questions">
          <h2 id="css-questions">CSS</h2>
          <div class="formrow">
            <div class="question-block">
              <label for="customer">Are you a frontend developer?</label>
            </div>
            <div class="answer">
              <select name="customer" id="customer" required>
                <option value="">Select an option</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
            </div>
            <div class="question-block">
              <label for="css-questions">Do you have any questions:</label>
            </div>
            <div class="answer">
              <textarea id="css-questions" name="css-questions" rows="5" cols="24" placeholder="Who is flexbox..."></textarea>
            </div>
          </div>
        </section>
        <button type="submit">Send</button>
      </form>
    </main>
    <footer>
      <address>
        <a href="https://freecodecamp.org">freeCodeCamp</a><br />
        San Francisco<br />
        California<br />
        USA
      </address>
    </footer>
  </body>
</html>
```

```css
@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}

body {
  background: #f5f6f7;
  color: #1b1b32;
  font-family: Helvetica;
  margin: 0;
}

header {
  width: 100%;
  height: 50px;
  background-color: #1b1b32;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  top: 0;
}

#logo {
  width: max(100px, 18vw);
  background-color: #0a0a23;
  aspect-ratio: 35 / 4;
  padding: 0.4rem;
}

h1 {
  color: #f1be32;
  font-size: min(5vw, 1.2em);
  text-align: center;
}

nav {
  width: 50%;
  max-width: 300px;
  height: 50px;
}

nav > ul {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
  align-items: center;
  padding-inline-start: 0;
  margin-block: 0;
  height: 100%;
}

nav > ul > li {
  color: #dfdfe2;
  margin: 0 0.2rem;
  padding: 0.2rem;
  display: block;
}

nav > ul > li:hover {
  background-color: #dfdfe2;
  color: #1b1b32;
  cursor: pointer;
}

li > a {
  color: inherit;
  text-decoration: none;
}

main {
  padding-top: 50px;
}

section {
  width: 80%;
  margin: 0 auto 10px auto;
  max-width: 600px;
}

h1,
h2 {
  font-family: Verdana, Tahoma;
}

h2 {
  border-bottom: 4px solid #dfdfe2;
  margin-top: 0px;
  padding-top: 60px;
}

.info {
  padding: 10px 0 0 5px;
}

.formrow {
  margin-top: 30px;
  padding: 0px 15px;
}

input {
  font-size: 16px;
}

.info label, .info input {
  display: inline-block;
}

.info input {
  width: 50%;
  text-align: left;
}

.info label {
  width: 10%;
  min-width: 55px;
  text-align: right;
}

.question-block {
  text-align: left;
  display: block;
  width: 100%;
  margin-top: 20px;
  padding-top: 5px;
}

p {
  margin-top: 5px;
  padding-left: 15px;
  font-size: 20px;
}

p::before {
  content: "Question #";
}

.question {
  border: none;
  padding-bottom: 0;
}

.answers-list {
  list-style: none;
  padding: 0;
}

button {
  display: block;
  margin: 40px auto;
  width: 40%;
  padding: 15px;
  font-size: 23px;
  background: #d0d0d5;
  border: 3px solid #3b3b4f;
}

footer {
  background-color: #2a2a40;
  display: flex;
  justify-content: center;
}

footer,
footer a {
  color: #dfdfe2;
}

address {
  text-align: center;
  padding: 0.3em;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```
