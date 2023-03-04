# Step 32
Give the label elements text such that the input comes before the text. Then, give the input elements a value matching the text. The text should either be True or False.

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
          <li><a href="#student-info">INFO</a></li>
          <li><a href="#html-questions">HTML</a></li>
          <li><a href="#css-questions">CSS</a></li>
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
                    <input type="radio" id="q1-a1" value="True" />
                    <p>True</p>
                  </label>
                </li>
                <li>
                  <label for="q1-a2">
                    <input type="radio" id="q1-a2" value="False" />
                    <p>False</p>
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
                    <input type="radio" id="q2-a1" value="True" />
                    <p>True</p>
                  </label>
                </li>
                <li>
                  <label for="q2-a2">
                    <input type="radio" id="q2-a2" value="False" />
                    <p>False</p>
                  </label>
                </li>
              </ul>
            </fieldset>
          </div>
        </section>
        <section role="region" aria-labelledby="css-questions">
          <h2 id="css-questions">CSS</h2>
        </section>
      </form>
    </main>
  </body>
</html>
```

# Step 33
If you click on the radio inputs, you might notice both inputs within the same true/false fieldset can be selected at the same time.
Group the relevant inputs together such that only one input from a pair can be selected at a time.

```html
              <ul class="answers-list">
                <li>
                  <label for="q1-a1">
                    <input type="radio" id="q1-a1" value="true" name="True False" />
                    True
                  </label>
                </li>
                <li>
                  <label for="q1-a2">
                    <input type="radio" id="q1-a2" value="false" name="True False" />
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
                    <input type="radio" id="q2-a1" value="true" name="True false" />
                    True
                  </label>
                </li>
                <li>
                  <label for="q2-a2">
                    <input type="radio" id="q2-a2" value="false" name="True false" />
                    False
                  </label>
                </li>
              </ul>
```

# Step 34
To prevent unnecessary repetition, target the before pseudo-element of the p element, and give it a content property of "Question #".

```css
p:before {
  content: "Question #";
}
```

# Step 35
The final section of this quiz will contain a dropdown, and a text box.
Begin by nesting a div with a class of formrow, and nest four div elements inside of it, alternating their class attributes with question-block and answer.

```html
        <section role="region" aria-labelledby="css-questions">
          <h2 id="css-questions">CSS</h2>
          <div class="formrow">
            <div class="question-block"></div>
            <div class="answer"></div>
            <div class="question-block"></div>
            <div class="answer"></div>
          </div>
        </section>
```

# Step 36
Within the div.question-block elements, nest one label element, and give the label elements text content

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
          <li><a href="#student-info">INFO</a></li>
          <li><a href="#html-questions">HTML</a></li>
          <li><a href="#css-questions">CSS</a></li>
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
              <label>Are you a frontend developer?</label>
            </div>
            <div class="answer">
            </div>
            <div class="question-block">
              <label>Do you have any questions:</label>
            </div>
            <div class="answer">
            </div>
          </div>
        </section>
      </form>
    </main>
  </body>
</html>
```
     
# Step 37
Within the first div.answer element, nest one required select element with three option elements.
Give the first option element a value of "", and the text Select an option. Give the second option element a value of yes, and the text Yes. Give the third option element a value of no, and the text No.
    
```html    
            <div class="answer">
              <select required>
                <option value="">Select an option</option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
              </select>
            </div>
```

# Step 38
Link the first label element to the select element, and give the select element a name attribute.

```html
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
```

# Step 39
Nest one textarea element within the second div.answer element, and set the number of rows and columns it has. Then, give the textarea placeholder text describing an example answer.

```html
            <div class="question-block">
              <label>Do you have any questions:</label>
            </div>
            <div class="answer">
              <textarea rows="5" cols="24" placeholder="Who is flexbox..."></textarea>
            </div>
```

# Step 40
As with the other input and label elements, link the textarea to its corresponding label element, and give it a name attribute.

```html
            <div class="answer">
              <textarea id="css-questions" name="css-questions" rows="5" cols="24" placeholder="Who is flexbox..."></textarea>
            </div>
```

# Step 41
Do not forget to give your form a submit button.

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
          <li><a href="#student-info">INFO</a></li>
          <li><a href="#html-questions">HTML</a></li>
          <li><a href="#css-questions">CSS</a></li>
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
        <input type="submit" value="Send" />
      </form>
    </main>
  </body>
</html>
```

# Step 42
Two final semantic HTML elements for this project are the footer and address elements. The footer element is a container for a collection of content that is related to the page, and the address element is a container for contact information for the author of the page.
After the main element, add one footer element, and nest one address element within it.
  
```html
    <footer>
      <address></address>
    </footer>
```

# Step 43
Within the address element, add the following:

```html
freeCodeCamp<br />
San Francisco<br />
California<br />
USA
```

```html
    <footer>
      <address>
        freeCodeCamp<br />
        San Francisco<br />
        California<br />
        USA
      </address>
    </footer>
```

# Step 44
The address element does not have to contain a physical geographical location. It can be used to provide a link to the subject. Wrap a link around the text freeCodeCamp, and set its location to https://freecodecamp.org.

```html
    <footer>
      <address>
        <a href="https://freecodecamp.org">freeCodeCamp</a><br />
        San Francisco<br />
        California<br />
        USA
      </address>
    </footer>      
```

# Step 45
Back to styling the page. Select the list elements within the navigation bar, and give them the following styles:

```css
color: #dfdfe2;
margin: 0 0.2rem;
padding: 0.2rem;
display: block;
```

```css
nav > ul > li {
  color: #dfdfe2;
  margin: 0 0.2rem;
  padding: 0.2rem;
  display: block;
}
```

# Step 46
On the topic of visual accessibility, contrast between elements is a key factor. For example, the contrast between the text and the background of a heading should be at least 4.5:1.
Change the font color of all the anchor elements within the list elements to something with a contrast ratio of at least 7:1.              

```css
li > a {
  color: #dfdfe2;
}
```

# Step 47
To make the navigation buttons look more like typical buttons, remove the underline from the anchor tags. Then, create a new selector targeting the navigation list elements so that when the cursor hovers over them, the background color and text color are switched, and the cursor becomes a pointer.

```css
nav > ul > li:hover {
  color: #1b1b32;
  background-color: #dfdfe2;
  cursor: pointer;
}

li > a {
  color: inherit;
  text-decoration: none;
}             
```

# Step 48
Tidy up the header, by using Flexbox to put space between the children, and vertically center them. Then, fix the header to the top of the viewport.       
              
```css              
header {
  width: 100%;
  height: 50px;
  background-color: #1b1b32;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: fixed;
  top: 0;
}              
```

# Step 49
When the screen width is small, the h1 does not wrap its text content how it should. Align the text for the h1 element in the center.Then, give the main padding such that the Student Info section header can be fully seen.              
              
```css              
h1 {
  color: #f1be32;
  font-size: min(5vw, 1.2em);
  text-align: center;
}

main {
  padding-top: 25px;
}
```

# Step 50
On small screens, the unordered list in the navigation bar overflows the right side of the screen. Fix this by using Flexbox to wrap the ul content. Then, set the following CSS properties to correctly align the text:

```html
align-items: center;
padding-inline-start: 0;
margin-block: 0;
height: 100%;              
```             

```css
nav > ul {
  display: flex;
  justify-content: space-evenly;
  position: fixed;
  flex-wrap: wrap;
  align-items: center;
  padding-inline-start: 0;
  margin-block: 0;
  height: 100%;
}
```

# Step 51
Set the width of the section elements to 80% of their parent container. Then, use margins to center the section elements, adding 10px to the bottom margin. Also, ensure the section elements cannot be larger than 600px in width.              

```css
section {
  width: 80%;
  margin-top: 0;
  margin-bottom: 10px;
  margin-right: auto;
  margin-left: auto;
  max-width: 600px;
}
```

# Step 52
Replace the top margin of the h2 elements with 60px of top padding.          

```css
h2 {
  border-bottom: 4px solid #dfdfe2;
  padding-top: 60px;
  margin-top: 0;
}              
```

# Step 53
Add padding to the top and left of the .info elements, and set the other values to 0.              
  
```css  
.info {
  padding: 10px 0 0 5px;
}
```

# Step 54
Give the .formrow elements top margin, and left and right padding. The other padding values should be 0. Then, increase the font size for all input elements.              
              
```css              
.formrow {
  margin-top: 30px;
  padding: 0px 15px;
}

input {
  font-size: 16px;
}
```                            
