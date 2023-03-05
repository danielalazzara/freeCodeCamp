# html file

```htnl
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Survey Form</title>
    <link rel="stylesheet" href="styles.css"/>
  </head>
  <body>
    <h1 id="title">Survey Form</h1>
    <p id="description">Healthy eating habits</p>
    <form id="survey-form">
      <fieldset>
         <label for="name" id="name-label" >Enter Your Name: <input id="name" type="text" required placeholder="Your full name" /></label>
         <label for="email" id="email-label">Enter Your Email: <input id="email" type="email" required placeholder="Your email" /></label>
         <label for="number" id="number-label">Enter Your Age: <input id="number" type="number" min=10 max=120 required placeholder="Your age" /></label>
         <select id="dropdown">
           <option>Female</option>
           <option>Male</option>
         </select>
      </fieldset>
      <fieldset>
        <label>How many times a day do you eat fruit?</label>
        <label for="1-2"><input type="radio"/name="1-2" value=1 > 1-2 </label>
        <label for="3-4"><input type="radio" name="3-4" value=1 /> 3-4 </label>
        <label for="5-6"><input type="radio" name="5-6" value=1 /> 5-6 </label>
      </fieldset>

      <fieldset>
        <label>How many times a day do you eat vegetables?</label>
        <label for="1-2"><input type="radio"/name="1-2" value=1 > 1-2 </label>
        <label for="3-4"><input type="radio" name="3-4" value="1" /> 3-4 </label>
        <label for="5-6"><input type="radio" name="5-6" value=1 /> 5-6 </label>
      </fieldset>

      <fieldset>
        <label>Do you drink milk every day?</label>
        <label for="yes"><input id="yes" type="checkbox" required name="yes" value=0 /> yes 
        </label>
        <label for="no"><input id="no" type="checkbox" required name="no" value=0 /> no
        </label>
      </fieldset>

      <fieldset>
        <label>Do you eat sweets every day?</label>
        <label for="yes"><input id="yes" type="checkbox" required name="yes" value=0 /> yes 
        </label>
        <label for="no"><input id="no" type="checkbox" required name="no" value=0 /> no
        </label>
      </fieldset>

      <fieldset>
        <label>Please enter your additional comments here</label>
        <textarea></textarea>
      </fieldset>
      <input id="submit" type="submit" value="Submit" />
    </form>
  </body>
</html>


# css file

```css
body {
  width: 100%;
  height:100vh;
  margin: 0;
  background-color: #1b1b32;
  color: #f5f6f7;
}

fieldset {
  border: none;
  padding: 2rem 0;
  border-bottom: 3px solid #3b3b4f;
}
```
