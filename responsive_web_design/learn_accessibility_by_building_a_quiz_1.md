# Step 1
Welcome to the first part of the Accessibility Quiz. As you are becoming a seasoned HTML and CSS developer, we have started you off with the basic boilerplate.
Start this accessibility journey by providing a lang attribute to your html element. This will assist screen readers in identifying the language of the page.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>

  </body>
</html>
```

# Step 2
You may be familiar with the meta element already; it is used to specify information about the page, such as the title, description, keywords, and author.
Give your page a meta element with an appropriate charset value. The charset attribute specifies the character encoding of the page, and, nowadays, UTF-8 is the only encoding supported by most browsers.

```html
  <head>
    <link rel="stylesheet" href="styles.css" />
    <meta charset="UTF-8">
  </head>
```

# Step 3
Continuing with the meta elements, a viewport definition tells the browser how to render the page. Including one betters visual accessibility on mobile, and improves SEO (search engine optimization).
Add a viewport definition with a content attribute detailing the width and initial-scale of the page.

```html
  <head>
    <meta charset="UTF-8">
    <meta name="viewport"  content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles.css" />
  </head>
```

# Step 4
Another important meta element for accessibility and SEO is the description definition. The value of the content attribute is used by search engines to provide a description of your page.
Add a meta element with the name attribute set to description, and give it a useful content attribute.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="freeCodeCamp Accessibility Quiz practice project" />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>

  </body>
</html>
```

# Step 5
Lastly in the head, the title element is useful for screen readers to understand the content of a page. Furthermore, it is an important part of SEO. Give your page a title that is descriptive and concise.

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

  </body>
</html>
```

# Step 6
Navigation is a core part of accessibility, and screen readers rely on you to provide the structure of your page. This is accomplished with semantic HTML elements.
Add a header and a main element to your page. The header element will be used to introduce the page, as well as provide a navigation menu. The main element will contain the core content of your page.

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
    <header></header>
    <main></main>
  </body>
</html>
```

# Step 7
Within the header, provide context about the page by nesting one img, h1, and nav element. The img should point to https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg, and have an id of logo. The h1 should contain the text HTML/CSS Quiz.

```html
    <header>
      <img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" id="logo"/>
      <h1>HTML/CSS Quiz</h1>
      <nav></nav>
    </header>
```

# Step 8
A useful property of an SVG (scalable vector graphics) is that it contains a path attribute which allows the image to be scaled without affecting the resolution of the resultant image.
Currently, the img is assuming its default size, which is too large. Correctly, scale the image using it's id as a selector, and setting the width to max(100px, 18vw).

```html
#logo {
  width: max(100px, 18vw);
}
```

# Step 9
As described in the freeCodeCamp Style Guide, the logo should retain an aspect ratio of 35 / 4, and have padding around the text.
First, change the background-color to #0a0a23 so you can see the logo. Then, use the aspect-ratio property to set the desired aspect ratio to 35 / 4. Finally, add a padding of 0.4rem all around.

```html
#logo {
  width: max(100px, 18vw);
  background-color: #0a0a23;
  aspect-ratio: 35 / 4;
  padding: 0.4rem;
}
```

# Step 10
Make the header take up the full width of its parent container, set its height to 50px, and set the background-color to #1b1b32. Then, set the display to use Flexbox.

```html
header {
  height: 50px;
  width: 100%;
  background-color: #1b1b32;
  display: flex;
}
```

# Step 11
Change the h1 font color to #f1be32, and set the font size to min(5vw, 1.2em).

```html
h1 {
  color: #f1be32;
  font-size: min(5vw, 1.2em);
}
```

# Step 12
To enable navigation on the page, add an unordered list with the following three list items:
INFO
HTML
CSS
The list items text should be wrapped in anchor tags.

```html
      <nav>
        <ul>
          <li><a>INFO</a></li>
          <li><a>HTML</a></li>
          <li><a>CSS</a></li>
        </ul>
      </nav>
```

# Step 13
Target unordered list elements within nav elements, and use Flexbox to evenly space the children.

```html
nav > ul {
  justify-content: space-evenly;
  display: flex;
}
```

# Step 14
As this is a quiz, you will need a form for users to submit answers. You can semantically separate the content within the form using section elements.
Within the main element, create a form with three nested section elements. Then, make the form submit to https://freecodecamp.org/practice-project/accessibility-quiz, using the correct method.

```html
    <main>
      <form method="post" action="https://freecodecamp.org/practice-project/accessibility-quiz">
        <section></section>
        <section></section>
        <section></section>     
      </form>
    </main>
```

# Step 15
To increase the page accessibility, the role attribute can be used to indicate the purpose behind an element on the page to assistive technologies. The role attribute is a part of the Web Accessibility Initiative (WAI), and accepts preset values.
Give each of the section elements the region role.

```html
      <form method="post" action="https://freecodecamp.org/practice-project/accessibility-quiz">
        <section role="region"></section>
        <section role="region"></section>
        <section role="region"></section>
      </form>
```

# Step 16
Every region role requires a label, which helps screen reader users understand the purpose of the region. One method for adding a label is to add a heading element inside the region and then reference it with the aria-labelledby attribute.
Add the following aria-labelledby attributes to the section elements:
student-info
html-questions
css-questions
Then, within each section element, nest one h2 element with an id matching the corresponding aria-labelledby attribute. Give each h2 suitable text content.

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
          <li><a>INFO</a></li>
          <li><a>HTML</a></li>
          <li><a>CSS</a></li>
        </ul>
      </nav>
    </header>
    <main>
      <form method="post" action="https://freecodecamp.org/practice-project/accessibility-quiz">
        <section role="region" aria-labelledby="student-info">
          <h2 id="student-info">Student Info</h2>
        </section>
        <section role="region" aria-labelledby="html-questions">
          <h2 id="html-questions">HTML</h2>
        </section>
        <section role="region" aria-labelledby="css-questions">
          <h2 id="css-questions">CSS</h2>
        </section>
      </form>
    </main>
  </body>
</html>
```

# Step 17
Typeface plays an important role in the accessibility of a page. Some fonts are easier to read than others, and this is especially true on low-resolution screens.
Change the font for both the h1 and h2 elements to Verdana, and use another web-safe font in the sans-serif family as a fallback. Also, add a border-bottom of 4px solid #dfdfe2 to h2 elements to make the sections distinct.

```html
h1, h2 {
  font-family: Verdana Tahoma;
}

h2 {
  border-bottom: 4px solid #dfdfe2;
}
```

# Step 18
To be able to navigate within the page, give each anchor element an href corresponding to the id of the h2 elements.

```html
        <ul>
          <li><a href="#student-info">INFO</a></li>
          <li><a href="#html-questions">HTML</a></li>
          <li><a href="#css-questions">CSS</a></li>
        </ul>
```

# Step 19
Filling out the content of the quiz, below #student-info, add three div elements with a class of info. Then, within each div nest one label element, and one input element.

```html
        <section role="region" aria-labelledby="student-info">
          <h2 id="student-info">Student Info</h2>
            <div class="info">
              <label></label>
              <input />
            </div>
            <div class="info">
              <label></label>
              <input />
            </div>
            <div class="info">
              <label></label>
              <input />
            </div>
        </section>
```

# Step 20
It is important to link each input to the corresponding label element. This provides assistive technology users with a visual reference to the input. This is done by giving the label a for attribute, which contains the id of the input. This section will take a student's name, email address, and date of birth. Give the label elements appropriate for attributes, as well as text content. Then, link the input elements to the corresponding label elements.

```html
        <section role="region" aria-labelledby="student-info">
          <h2 id="student-info">Student Info</h2>
          <div class="info">
            <label for="student name">Student name</label>
            <input id="student name" />
          </div>
          <div class="info">
            <label for="email address">email</label>
            <input id="email address" />
          </div>
          <div class="info">
            <label for="date of birth">Date of birth</label>
            <input id="date of birth" />
          </div>
        </section>
```

# Step 21
Keeping in mind best-practices for form inputs, give each input an appropriate type and name attribute. Then, give the first input a placeholder attribute.

```html
          <div class="info">
            <label for="student-name">Name:</label>
            <input type="text" name="student-name" id="student-name" placeholder="e.g. Quincy Larson" />
          </div>
          <div class="info">
            <label for="student-email">Email:</label>
            <input type="email" name="student-email" id="student-email" />
          </div>
          <div class="info">
            <label for="birth-date">D.O.B.:</label>
            <input type="date" name="birth-date" id="birth-date" />
          </div>
        </section>
```

# Step 22
Even though you added a placeholder to the first input element in the previous lesson, this is actually not a best-practice for accessibility; too often, users confuse the placeholder text with an actual input value - they think there is already a value in the input.
Remove the placeholder text from the first input element, relying on the label being the best-practice.

```html
          <div class="info">
            <label for="student-name">Name:</label>
            <input type="text" name="student-name" id="student-name" />
          </div>
```

# Step 23
Arguably, D.O.B. is not descriptive enough. This is especially true for visually impaired users. One way to get around such an issue, without having to add visible text to the label, is to add text only a screen reader can read.
Append a span element with a class of sr-only to the current text content of the third label element.

```html
          <div class="info">
            <label for="birth-date">D.O.B.<span class="sr-only"></span></label>
            <input type="date" name="birth-date" id="birth-date" />
          </div>
```

# Step 24
Within the span element, add the text (Date of Birth).

```html
          <div class="info">
            <label for="birth-date">D.O.B.<span class="sr-only">(Date of Birth)</span></label>
            <input type="date" name="birth-date" id="birth-date" />
          </div>
```

# Step 25
The .sr-only text is still visible. There is a common pattern to visually hide text for only screen readers to read. This pattern is to set the following CSS properties:

```html
position: absolute;
width: 1px;
height: 1px;
padding: 0;
margin: -1px;
overflow: hidden;
clip: rect(0, 0, 0, 0);
white-space: nowrap;
border: 0;
```

Use the above to define the sr-only class.

```html
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

# Step 26
Within the second section element, add two div elements with a class of question-block. Then, within each div.question-block element, add one p element with text of incrementing numbers, starting at 1, and one fieldset element with a class of question.

```html
        <section role="region" aria-labelledby="html-questions">
          <h2 id="html-questions">HTML</h2>
          <div class="question-block">
            <p>1</p>
            <fieldset class="question">
          </div>
          <div class="question-block">
            <p>2</p>
            <fieldset class="question">
          </div>
        </section>
```
      
# Step 27
Each fieldset will contain a true/false question. Within each fieldset, nest one legend element, and one ul element with two options.
        
```html        
        <section role="region" aria-labelledby="html-questions">
          <h2 id="html-questions">HTML</h2>
          <div class="question-block">
            <p>1</p>
            <fieldset class="question">
              <legend></legend>
              <ul>
                <li></li>
                <li></li>
              </ul>
            </fieldset>
          </div>
          <div class="question-block">
            <p>2</p>
            <fieldset class="question">
              <legend></legend>
              <ul>
                <li></li>
                <li></li>
              </ul>
            </fieldset>
          </div>
        </section>
```

# Step 28
Give each fieldset an adequate name attribute. Then, give both unordered lists a class of answers-list. Finally, use the legend to caption the content of the fieldset by placing a true/false question as the text content. 

```html
        <section role="region" aria-labelledby="html-questions">
          <h2 id="html-questions">HTML</h2>
          <div class="question-block">
            <p>1</p>
            <fieldset class="question" name="question">
              <legend>True</legend>
              <ul class="answers-list">
                <li></li>
                <li ></li>
              </ul>
            </fieldset>
          </div>
          <div class="question-block">
            <p>2</p>
            <fieldset class="question" name="question">
              <legend>False</legend>
              <ul class="answers-list">
                <li></li>
                <li></li>
              </ul>
            </fieldset>
          </div>
        </section>
```
 
# Step 29
To provide the functionality of the true/false questions, we need a set of inputs which do not allow both to be selected at the same time. Within each list element, nest one label element, and within each label element, nest one input element with the appropriate type.

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
                <li><label><input type="radio" /></label></li>
                <li><label><input type="radio" /></label></li>
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
                <li><label><input type="radio" /></label></li>
                <li><label><input type="radio" /></label></li>
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

# Step 30
Add an id to all of your radio inputs so you can link your labels to them. Give the first one an id of q1-a1. Give the rest of them ids of q1-a2, q2-a1, and q2-a2, respectively.

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
                  <label>
                    <input type="radio" id="q1-a1"/>
                  </label>
                </li>
                <li>
                  <label>
                    <input type="radio" id="q1-a2"/>
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
                  <label>
                    <input type="radio" id="q2-a1" />
                  </label>
                </li>
                <li>
                  <label>
                    <input type="radio" id="q2-a2" />
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

Step 31
Although not required for label elements with a nested input, it is still best-practice to explicitly link a label with its corresponding input element.
Now, add a for attribute to each of your four labels that links the label to its corresponding radio input.

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
                    <input type="radio" id="q1-a1"/>
                  </label>
                </li>
                <li>
                  <label for="q1-a2">
                    <input type="radio" id="q1-a2" />
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
                    <input type="radio" id="q2-a1" />
                  </label>
                </li>
                <li>
                  <label for="q2-a2">
                    <input type="radio" id="q2-a2" />
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
