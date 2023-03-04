# html file
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>JavaScript Variables Technical Documentation</title>
    <link rel="stylesheet" href="styles.css"/>
  </head>

  <body>
    <main id="main-doc">
      <nav id="navbar">
        <header>JavaScript</header>
        <ul>
          <li>
            <a class="nav-link" href="#Introduction">Introduction</a>
          </li>
          <li>
            <a class="nav-link" href="#What_you_should_already_know">What you should already know</a>
          </li>
          <li>
            <a class="nav-link" href="#Variables">Variables</a>
          </li>
          <li>
              <a class="nav-link" href="#Declaring_variables">Declaring variables</a>
          </li>
          <li>
            <a class="nav-link" href="#Variable_scope">Variable scope</a>
          </li>
          <li>
              <a class="nav-link" href="#Global_variables">Global variables</a>
          </li>
        </ul>
      </nav>

      <section class="main-section" id="Introduction">
        <header>Introduction</header>
        <p>JavaScript is a cross-platform, object-oriented scripting language. It is a small and lightweight language. Inside a host environment (for example, a web browser), JavaScript can be connected to the objects of its environment to provide programmatic control over them.</p>
        <p>JavaScript contains a standard library of objects, such as Array, Date, and Math, and a core set of language elements such as operators, control structures, and statements.</p>
      </section>

      <section class="main-section" id="What_you_should_already_know">
        <header>What you should already know</header>
        <p>This guide assumes you have the following basic background:</p>
        <ul>
          <li>
            <p>A general understanding of the Internet and the World Wide Web (WWW).</p>
          </li>
          <li>
            <p>Good working knowledge of HyperText Markup Language (HTML).</p>
          </li>
          <li>
            <p>Some programming experience. If you are new to programming, try one of the tutorials linked on the main page about JavaScript.</p>
          </li>
        </ul>

      <section class="main-section" id="Variables">
        <header>Variables</header>
        <p>You use variables as symbolic names for values in your application. The names of variables, called identifiers, conform to certain rules.</p>
        <p>A JavaScript identifier must start with a letter, underscore (_), or dollar sign ($); subsequent characters can also be digits (0-9). Because JavaScript is case sensitive, letters include the characters "A" through "Z" (uppercase) and the characters "a" through "z" (lowercase).</p>
        <p>Some examples of legal names are:</p> 
        <ul>
          <li><code>Number_hits</code></li>
          <li><code> temp99</code></li>
          <li><code>_name</code></li>
        </ul>
      </section>

      <section class="main-section" id="Declaring_variables">
        <header>Declaring variables</header>
        <p>You can declare a variable in three ways:</p>
        <ul>
          <li>
            <p>With the keyword var. For example,</p>
            <code>var x = 42.</code>
            <p>This syntax can be used to declare both local and global variables.</p>
          </li>
          <li>
            <p>By simply assigning it a value. For example,</p>
            <code>var x = 42.</code>
            <p>This always declares a global variable. It generates a strict JavaScript warning. You shouldn't use this variant.</p>
          </li>
          <li>
            <p>With the keyword let. For example,</p>
            <code>let y = 13.</code>
            <p>This syntax can be used to declare a block scope local variable.</p>
          </li>
        </ul>
      </section>

      <section class="main-section" id="Variable_scope">
        <header>Variable scope</header>
        <p>When you declare a variable outside of any function, it is called a global variable, because it is available to any other code in the current document. When you declare a variable within a function, it is called a local variable, because it is available only within that function.</p>
      </section>

      <section class="main-section" id="Global_variables">
        <header>Global variables</header>
        <p>Global variables are in fact properties of the global object. In web pages the global object is window, so you can set and access global variables using the window.variable syntax.</p>
        <p>Consequently, you can access global variables declared in one window or frame from another window or frame by specifying the window or frame name. For example, if a variable called phoneNumber is declared in a document, you can refer to this variable from an iframe as parent.phoneNumber.</p>
      </section>

    </main>
  </body>
</html>
```
  
# css file
```css
html {
  font-family: 'Open Sans', sans-serif;
  color: white;   background-color: black;
margin-left: 20px;
margin-right: 20px;
justify-content: space-between;
margin-top: 30px;
}

header {
  font: bold;
  font-size: 24;
  text-align: center;
}

@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}
```
