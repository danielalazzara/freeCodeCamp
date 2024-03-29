# Create a Simple JSX Element

React is an Open Source view library created and maintained by Facebook. It's a great tool to render the User Interface (UI) of modern web applications.

React uses a syntax extension of JavaScript called JSX that allows you to write HTML directly within JavaScript. This has several benefits. It lets you use the full programmatic power of JavaScript within HTML, and helps to keep your code readable. For the most part, JSX is similar to the HTML that you have already learned, however there are a few key differences that will be covered throughout these challenges.

For instance, because JSX is a syntactic extension of JavaScript, you can actually write JavaScript directly within JSX. To do this, you simply include the code you want to be treated as JavaScript within curly braces: ```{ 'this is treated as JavaScript code' }```. Keep this in mind, since it's used in several future challenges.

However, because JSX is not valid JavaScript, JSX code must be compiled into JavaScript. The transpiler Babel is a popular tool for this process. For your convenience, it's already added behind the scenes for these challenges. If you happen to write syntactically invalid JSX, you will see the first test in these challenges fail.

It's worth noting that under the hood the challenges are calling ```ReactDOM.render(JSX, document.getElementById('root'))```. This function call is what places your JSX into React's own lightweight representation of the DOM. React then uses snapshots of its own DOM to optimize updating only specific parts of the actual DOM.

The current code uses JSX to assign a ```div``` element to the constant ```JSX```. Replace the ```div``` with an ```h1`` element and add the text ```Hello JSX!``` inside it.

```
const JSX = <h1>Hello JSX!</h1>;
```

# Create a Complex JSX Element

The last challenge was a simple example of JSX, but JSX can represent more complex HTML as well.

One important thing to know about nested JSX is that it must return a single element.

This one parent element would wrap all of the other levels of nested elements.

For instance, several JSX elements written as siblings with no parent wrapper element will not transpile.

Here's an example:

__Valid JSX:__

```
<div>
  <p>Paragraph One</p>
  <p>Paragraph Two</p>
  <p>Paragraph Three</p>
</div>
```

__Invalid JSX:__

```
<p>Paragraph One</p>
<p>Paragraph Two</p>
<p>Paragraph Three</p>
```

Define a new constant ```JSX``` that renders a ```div``` which contains the following elements in order:

An ```h1```, a ```p```, and an unordered list that contains three ```li``` items. You can include any text you want within each element.

Note: When rendering multiple elements like this, you can wrap them all in parentheses, but it's not strictly required. Also notice this challenge uses a ```div``` tag to wrap all the child elements within a single parent element. If you remove the ```div```, the JSX will no longer transpile. Keep this in mind, since it will also apply when you return JSX elements in React components.

```
const JSX = {
  <div>
    <h1></h1>
    <p></p>
    <ul>
      <li></li>
      <li></li>
      <li></li>
    </ul>
  </div>
};
```

# Add Comments in JSX

JSX is a syntax that gets compiled into valid JavaScript. Sometimes, for readability, you might need to add comments to your code. Like most programming languages, JSX has its own way to do this.

To put comments inside JSX, you use the syntax ```{/* */}``` to wrap around the comment text.

The code editor has a JSX element similar to what you created in the last challenge. Add a comment somewhere within the provided ```div``` element, without modifying the existing ```h1``` or ```p``` elements.

```
const JSX = (
  <div>
    {/*HELLO*/}
    <h1>This is a block of JSX</h1>
    <p>Here's a subtitle</p>
  </div>
);
```

# Render HTML Elements to the DOM

So far, you've learned that JSX is a convenient tool to write readable HTML within JavaScript. With React, we can render this JSX directly to the HTML DOM using React's rendering API known as ReactDOM.

ReactDOM offers a simple method to render React elements to the DOM which looks like this: ```ReactDOM.render(componentToRender, targetNode)```, where the first argument is the React element or component that you want to render, and the second argument is the DOM node that you want to render the component to.

As you would expect, ```ReactDOM.render()``` must be called after the JSX element declarations, just like how you must declare variables before using them.

The code editor has a simple JSX component. Use the ```ReactDOM.render()``` method to render this component to the page. You can pass defined JSX elements directly in as the first argument and use ```document.getElementById()``` to select the DOM node to render them to. There is a ```div``` with ```id='challenge-node'``` available for you to use. Make sure you don't change the ```JSX``` constant.

```
const JSX = (
  <div>
    <h1>Hello World</h1>
    <p>Lets render this to the DOM</p>
  </div>
);
// Change code below this line
ReactDOM.render(JSX, document.getElementById("challenge-node"));
```

# Define an HTML Class in JSX

Now that you're getting comfortable writing JSX, you may be wondering how it differs from HTML.

So far, it may seem that HTML and JSX are exactly the same.

One key difference in JSX is that you can no longer use the word ```class``` to define HTML classes. This is because ```class``` is a reserved word in JavaScript. Instead, JSX uses ```className```.

In fact, the naming convention for all HTML attributes and event references in JSX become camelCase. For example, a click event in JSX is ```onClick```, instead of ```onclick```. Likewise, ```onchange``` becomes ```onChange```. While this is a subtle difference, it is an important one to keep in mind moving forward.

Apply a class of ```myDiv``` to the ```div``` provided in the JSX code.

```
const JSX = (
  <div className="myDiv">
    <h1>Add a class to this div</h1>
  </div>
);
```

# Learn About Self-Closing JSX Tags

So far, you’ve seen how JSX differs from HTML in a key way with the use of ```className``` vs. ```class``` for defining HTML classes.

Another important way in which JSX differs from HTML is in the idea of the self-closing tag.

In HTML, almost all tags have both an opening and closing tag: ```<div></div>```; the closing tag always has a forward slash before the tag name that you are closing. However, there are special instances in HTML called “self-closing tags”, or tags that don’t require both an opening and closing tag before another tag can start.

For example the line-break tag can be written as ```<br>``` or as ```<br />```, but should never be written as ```<br></br>```, since it doesn't contain any content.

In JSX, the rules are a little different. Any JSX element can be written with a self-closing tag, and every element must be closed. The line-break tag, for example, must always be written as ```<br />``` in order to be valid JSX that can be transpiled. A ```<div>```, on the other hand, can be written as ```<div />``` or ```<div></div>```. The difference is that in the first syntax version there is no way to include anything in the ```<div />```. You will see in later challenges that this syntax is useful when rendering React components.

Fix the errors in the code editor so that it is valid JSX and successfully transpiles. Make sure you don't change any of the content - you only need to close tags where they are needed.

```
const JSX = (
  <div>
    <h2>Welcome to React!</h2> <br />
    <p>Be sure to close all tags!</p>
    <hr />
  </div>
);
```

# Create a Stateless Functional Component

Components are the core of React. Everything in React is a component and here you will learn how to create one.

There are two ways to create a React component. The first way is to use a JavaScript function. Defining a component in this way creates a stateless functional component. The concept of state in an application will be covered in later challenges. For now, think of a stateless component as one that can receive data and render it, but does not manage or track changes to that data. (We'll cover the second way to create a React component in the next challenge.)

To create a component with a function, you simply write a JavaScript function that returns either JSX or ```null```. One important thing to note is that React requires your function name to begin with a capital letter. Here's an example of a stateless functional component that assigns an HTML class in JSX:

```
const DemoComponent = function() {
  return (
    <div className='customClass' />
  );
};
```


After being transpiled, the ```<div>``` will have a CSS class of ```customClass```.

Because a JSX component represents HTML, you could put several components together to create a more complex HTML page. This is one of the key advantages of the component architecture React provides. It allows you to compose your UI from many separate, isolated components. This makes it easier to build and maintain complex user interfaces.

The code editor has a function called ```MyComponent```. Complete this function so it returns a single ```div``` element which contains some string of text.

Note: The text is considered a child of the ```div``` element, so you will not be able to use a self-closing tag.

```
const MyComponent = function() {
  // Change code below this line
  return (
    <div>Hello World!</div>
  );

  // Change code above this line
}
```

# Create a React Component

The other way to define a React component is with the ES6 ```class``` syntax. In the following example, ```Kitten``` extends ```React.Component```:

```
class Kitten extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>Hi</h1>
    );
  }
}
```

This creates an ES6 class ```Kitten``` which extends the ```React.Component``` class. So the ```Kitten``` class now has access to many useful React features, such as local state and lifecycle hooks. Don't worry if you aren't familiar with these terms yet, they will be covered in greater detail in later challenges. Also notice the ```Kitten``` class has a ```constructor``` defined within it that calls ```super()```. It uses ```super()``` to call the constructor of the parent class, in this case ```React.Component```. The constructor is a special method used during the initialization of objects that are created with the ```class``` keyword. It is best practice to call a component's ```constructor``` with ```super```, and pass ```props``` to both. This makes sure the component is initialized properly. For now, know that it is standard for this code to be included. Soon you will see other uses for the constructor as well as ```props```.

```MyComponent``` is defined in the code editor using class syntax. Finish writing the ```render``` method so it returns a ```div``` element that contains an ```h1``` with the text ```Hello React!```.

```
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    // Change code below this line
    return (
      <div>
        <h1>Hello React!</h1>
      </div>
    );
    // Change code above this line
  }
};
```

# Create a Component with Composition

Now we will look at how we can compose multiple React components together. Imagine you are building an app and have created three components: a ```Navbar```, ```Dashboard```, and ```Footer```.

To compose these components together, you could create an ```App``` parent component which renders each of these three components as children. To render a component as a child in a React component, you include the component name written as a custom HTML tag in the JSX. For example, in the ```render``` method you could write:

```
return (
 <App>
  <Navbar />
  <Dashboard />
  <Footer />
 </App>
)
```

When React encounters a custom HTML tag that references another component (a component name wrapped in ```< />``` like in this example), it renders the markup for that component in the location of the tag. This should illustrate the parent/child relationship between the ```App``` component and the ```Navbar```, ```Dashboard```, and ```Footer```.

In the code editor, there is a simple functional component called ```ChildComponent``` and a class component called ```ParentComponent```. Compose the two together by rendering the ```ChildComponent``` within the ```ParentComponent```. Make sure to close the ```ChildComponent``` tag with a forward slash.

Note: ```ChildComponent``` is defined with an ES6 arrow function because this is a very common practice when using React. However, know that this is just a function. If you aren't familiar with the arrow function syntax, please refer to the JavaScript section.

```
const ChildComponent = () => {
  return (
    <div>
      <p>I am the child</p>
    </div>
  );
};

class ParentComponent extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>I am the parent</h1>
        { /* Change code below this line */ }
        <ChildComponent />
        { /* Change code above this line */ }
      </div>
    );
  }
};
```

# Use React to Render Nested Components

The last challenge showed a simple way to compose two components, but there are many different ways you can compose components with React.

Component composition is one of React's powerful features. When you work with React, it is important to start thinking about your user interface in terms of components like the App example in the last challenge. You break down your UI into its basic building blocks, and those pieces become the components. This helps to separate the code responsible for the UI from the code responsible for handling your application logic. It can greatly simplify the development and maintenance of complex projects.

There are two functional components defined in the code editor, called ```TypesOfFruit``` and ```Fruits```. Take the ```TypesOfFruit``` component and compose it, or nest it, within the ```Fruits``` component. Then take the ```Fruits``` component and nest it within the ```TypesOfFood``` component. The result should be a child component, nested within a parent component, which is nested within a parent component of its own!

```
const TypesOfFruit = () => {
  return (
    <div>
      <h2>Fruits:</h2>
      <ul>
        <li>Apples</li>
        <li>Blueberries</li>
        <li>Strawberries</li>
        <li>Bananas</li>
      </ul>
    </div>
  );
};

const Fruits = () => {
  return (
    <div>
      { /* Change code below this line */ }
      <TypesOfFruit />
      { /* Change code above this line */ }
    </div>
  );
};

class TypesOfFood extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1>Types of Food:</h1>
        { /* Change code below this line */ }
          <Fruits />
        { /* Change code above this line */ }
      </div>
    );
  }
};
```

# Compose React Components

As the challenges continue to use more complex compositions with React components and JSX, there is one important point to note. Rendering ES6 style class components within other components is no different than rendering the simple components you used in the last few challenges. You can render JSX elements, stateless functional components, and ES6 class components within other components.

In the code editor, the ```TypesOfFood``` component is already rendering a component called ```Vegetables```. Also, there is the ```Fruits``` component from the last challenge.

Nest two components inside of ```Fruits``` — first ```NonCitrus```, and then ```Citrus```. Both of these components are provided for you behind the scenes. Next, nest the ```Fruits``` class component into the ```TypesOfFood``` component, below the ```h1``` heading element and above ```Vegetables```. The result should be a series of nested components, which uses two different component types.

```
class Fruits extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h2>Fruits:</h2>
        { /* Change code below this line */ }
          <NonCitrus />
          <Citrus />
        { /* Change code above this line */ }
      </div>
    );
  }
};

class TypesOfFood extends React.Component {
  constructor(props) {
     super(props);
  }
  render() {
    return (
      <div>
        <h1>Types of Food:</h1>
        { /* Change code below this line */ }
          <Fruits />
        { /* Change code above this line */ }
        <Vegetables />
      </div>
    );
  }
};
```

# Render a Class Component to the DOM

You may remember using the ReactDOM API in an earlier challenge to render JSX elements to the DOM. The process for rendering React components will look very similar. The past few challenges focused on components and composition, so the rendering was done for you behind the scenes. However, none of the React code you write will render to the DOM without making a call to the ReactDOM API.

Here's a refresher on the syntax: 
```ReactDOM.render(componentToRender, targetNode)```. The first argument is the React component that you want to render. The second argument is the DOM node that you want to render that component within.

React components are passed into ```ReactDOM.render()``` a little differently than JSX elements. For JSX elements, you pass in the name of the element that you want to render. However, for React components, you need to use the same syntax as if you were rendering a nested component, for example ```ReactDOM.render(<ComponentToRender />, targetNode)```. You use this syntax for both ES6 class components and functional components.

Both the ```Fruits``` and ```Vegetables``` components are defined for you behind the scenes. Render both components as children of the ```TypesOfFood``` component, then render ```TypesOfFood``` to the DOM. There is a ```div``` with ```id='challenge-node'``` available for you to use.

```
class TypesOfFood extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>Types of Food:</h1>
        {/* Change code below this line */}
          <Fruits />
          <Vegetables />
        {/* Change code above this line */}
      </div>
    );
  }
};

// Change code below this line
ReactDOM.render(<TypesOfFood />, document.getElementById('challenge-node'))
```

# Write a React Component from Scratch

Now that you've learned the basics of JSX and React components, it's time to write a component on your own. React components are the core building blocks of React applications so it's important to become very familiar with writing them. Remember, a typical React component is an ES6 ```class``` which extends ```React.Component```. It has a render method that returns HTML (from JSX) or ```null```. This is the basic form of a React component. Once you understand this well, you will be prepared to start building more complex React projects.

Define a class ```MyComponent``` that extends ```React.Component```. Its render method should return a ```div``` that contains an ```h1``` tag with the text: ```My First React Component!``` in it. Use this text exactly, the case and punctuation matter. Make sure to call the constructor for your component, too.

Render this component to the DOM using ```ReactDOM.render()```. There is a ```div``` with ```id='challenge-node'``` available for you to use.

```
// Change code below this line
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>My First React Component!</h1> 
      </div>
    );
  }
};

ReactDOM.render(<MyComponent />, document.getElementById("challenge-node"))
```

# Pass Props to a Stateless Functional Component

The previous challenges covered a lot about creating and composing JSX elements, functional components, and ES6 style class components in React. With this foundation, it's time to look at another feature very common in React: __props__. In React, you can pass props, or properties, to child components. Say you have an ```App``` component which renders a child component called ```Welcome``` which is a stateless functional component. You can pass ```Welcome``` a ```user``` property by writing:

```
<App>
  <Welcome user='Mark' />
</App>
```

You use __custom HTML attributes__ created by you and supported by React to be passed to the component. In this case, the created property ```user``` is passed to the component ```Welcome```. Since ```Welcome``` is a stateless functional component, it has access to this value like so:

```
const Welcome = (props) => <h1>Hello, {props.user}!</h1>
```

It is standard to call this value ```props``` and when dealing with stateless functional components, you basically consider it as an argument to a function which returns JSX. You can access the value of the argument in the function body. With class components, you will see this is a little different.

There are ```Calendar``` and ```CurrentDate``` components in the code editor. When rendering ```CurrentDate``` from the ```Calendar``` component, pass in a property of ```date``` assigned to the current date from JavaScript's ```Date``` object. Then access this ```prop``` in the ```CurrentDate``` component, showing its value within the ```p``` tags. Note that for ```prop``` values to be evaluated as JavaScript, they must be enclosed in curly brackets, for instance ```date={Date()}```.

```
const CurrentDate = (props) => {
  return (
    <div>
      { /* Change code below this line */ }
      <p>The current date is: {props.date}</p>
      { /* Change code above this line */ }
    </div>
  );
};

class Calendar extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h3>What date is it?</h3>
        { /* Change code below this line */ }
        <CurrentDate date={Date()} />
        { /* Change code above this line */ }
      </div>
    );
  }
};
```

# Pass an Array as Props

The last challenge demonstrated how to pass information from a parent component to a child component as ```props``` or properties. This challenge looks at how arrays can be passed as ```props```. To pass an array to a JSX element, it must be treated as JavaScript and wrapped in curly braces.

```
<ParentComponent>
  <ChildComponent colors={["green", "blue", "red"]} />
</ParentComponent>
```

The child component then has access to the array property ```colors```. Array methods such as ```join()``` can be used when accessing the property. ```const ChildComponent = (props) => <p>{props.colors.join(', ')}</p>``` This will join all ```colors``` array items into a comma separated string and produce: ```<p>green, blue, red</p>``` Later, we will learn about other common methods to render arrays of data in React.

There are ```List``` and ```ToDo``` components in the code editor. When rendering each ```List``` from the ```ToDo``` component, pass in a ```tasks``` property assigned to an array of to-do tasks, for example ```["walk dog", "workout"]```. Then access this ```tasks``` array in the ```List``` component, showing its value within the ```p``` element. Use ```join(", ")``` to display the ```props.tasksarray``` in the ```p``` element as a comma separated list. Today's list should have at least 2 tasks and tomorrow's should have at least 3 tasks.

```
const List = (props) => {
  { /* Change code below this line */ }
  return <p>{props.tasks.join(", ")}</p>
  { /* Change code above this line */ }
};

class ToDo extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>To Do Lists</h1>
        <h2>Today</h2>
        { /* Change code below this line */ }
        <List tasks={["Walk", "Cook", "Bake"]} />
        <h2>Tomorrow</h2>
        <List tasks={["Study", "Code", "Eat"]} />
        { /* Change code above this line */ }
      </div>
    );
  }
};
```

# Use Default Props

React also has an option to set default props. You can assign default props to a component as a property on the component itself and React assigns the default prop if necessary. This allows you to specify what a prop value should be if no value is explicitly provided. For example, if you declare ```MyComponent.defaultProps = { location: 'San Francisco' }```, you have defined a location prop that's set to the string ```San Francisco```, unless you specify otherwise. React assigns default props if props are undefined, but if you pass ```null``` as the value for a prop, it will remain ```null```.

The code editor shows a ```ShoppingCart``` component. Define default props on this component which specify a ```prop``` items with a value of ```0```.

```
const ShoppingCart = (props) => {
  return (
    <div>
      <h1>Shopping Cart Component</h1>
    </div>
  )
};
// Change code below this line
ShoppingCart.defaultProps = {items: 0}
```

# Override Default Props

The ability to set default props is a useful feature in React. The way to override the default props is to explicitly set the prop values for a component.

The ```ShoppingCart``` component now renders a child component ```Items```. This ```Items``` component has a default prop ```quantity``` set to the integer ```0```. Override the default prop by passing in a value of ```10``` for ```quantity```.

Note: Remember that the syntax to add a prop to a component looks similar to how you add HTML attributes. However, since the value for ```quantity``` is an integer, it won't go in quotes but it should be wrapped in curly braces. For example, ```{100}```. This syntax tells JSX to interpret the value within the braces directly as JavaScript.

```
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
}

Items.defaultProps = {
  quantity: 0
}

class ShoppingCart extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    { /* Change code below this line */ }
    return <Items quantity={10}/>
    { /* Change code above this line */ }
  }
};
```

# Use PropTypes to Define the Props You Expect

React provides useful type-checking features to verify that components receive props of the correct type. For example, your application makes an API call to retrieve data that you expect to be in an array, which is then passed to a component as a prop. You can set ```propTypes``` on your component to require the data to be of type ```array```. This will throw a useful warning when the data is of any other type.

It's considered a best practice to set ```propTypes``` when you know the type of a prop ahead of time. You can define a ```propTypes``` property for a component in the same way you defined ```defaultProps```. Doing this will check that props of a given key are present with a given type. Here's an example to require the type ```function``` for a prop called ```handleClick```:

```
MyComponent.propTypes = { handleClick: PropTypes.func.isRequired }
```

In the example above, the ```PropTypes.func``` part checks that ```handleClick``` is a function. Adding ```isRequired``` tells React that ```handleClick``` is a required property for that component. You will see a warning if that prop isn't provided. Also notice that ```func``` represents ```function```. Among the seven JavaScript primitive types, ```function``` and ```boolean``` (written as ```bool```) are the only two that use unusual spelling. In addition to the primitive types, there are other types available. For example, you can check that a prop is a React element. Please refer to the documentation for all of the options.

Note: As of React v15.5.0, ```PropTypes``` is imported independently from React, like this: ```import PropTypes from 'prop-types';```

Define ```propTypes``` for the ```Items``` component to require quantity as a ```prop``` and verify that it is of type ```number```.

```
const Items = (props) => {
  return <h1>Current Quantity of Items in Cart: {props.quantity}</h1>
};

// Change code below this line
Items.propTypes = {
  quantity: PropTypes.number.isRequired
};
// Change code above this line

Items.defaultProps = {
  quantity: 0
};

class ShoppingCart extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return <Items />
  }
};
```

# Access Props Using this.props

The last several challenges covered the basic ways to pass props to child components. But what if the child component that you're passing a prop to is an ES6 class component, rather than a stateless functional component? The ES6 class component uses a slightly different convention to access props.

Anytime you refer to a class component within itself, you use the ```this``` keyword. To access props within a class component, you preface the code that you use to access it with ```this```. For example, if an ES6 class component has a prop called ```data```, you write ```{this.props.data}``` in JSX.

Render an instance of the ```Welcome``` component in the parent component ```App```. Here, give ```Welcome``` a prop of ```name``` and assign it a value of a string. Within the child, ```Welcome```, access the ```name``` prop within the ```strong``` tags.

```
class App extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
        <div>
            { /* Change code below this line */ }
            <Welcome name="Daniela" />
            { /* Change code above this line */ }
        </div>
    );
  }
};

class Welcome extends React.Component {
  constructor(props) {
    super(props);

  }
  render() {
    return (
        <div>
          { /* Change code below this line */ }
          <p>Hello, <strong>{this.props.name}</strong>!</p>
          { /* Change code above this line */ }
        </div>
    );
  }
};
```

# Review Using Props with Stateless Functional Components

Except for the last challenge, you've been passing props to stateless functional components. These components act like pure functions. They accept props as input and return the same view every time they are passed the same props. You may be wondering what state is, and the next challenge will cover it in more detail. Before that, here's a review of the terminology for components.

A _stateless functional component_ is any function you write which accepts props and returns JSX. A _stateless component_, on the other hand, is a class that extends ```React.Component```, but does not use internal state (covered in the next challenge). Finally, a _stateful component_ is a class component that does maintain its own internal state. You may see stateful components referred to simply as components or React components.

A common pattern is to try to minimize statefulness and to create stateless functional components wherever possible. This helps contain your state management to a specific area of your application. In turn, this improves development and maintenance of your app by making it easier to follow how changes to state affect its behavior.

The code editor has a ```CampSite component``` that renders a ```Camper``` component as a child. Define the ```Camper``` component and assign it default props of ```{ name: 'CamperBot' }```. Inside the ```Camper``` component, render any code that you want, but make sure to have one ```p``` element that includes only the ```name``` value that is passed in as a ```prop```. Finally, define ```propTypes``` on the ```Camper``` component to require ```name``` to be provided as a prop and verify that it is of type ```string```.

```
class CampSite extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <Camper/>
      </div>
    );
  }
};
// Change code below this line
const Camper = props => <p>{props.name}</p>;

Camper.defaultProps = {
  name: "CamperBot"
};

Camper.propTypes = {
  name: PropTypes.string.isRequired
};
```

# Create a Stateful Component

One of the most important topics in React is ```state```. State consists of any data your application needs to know about, that can change over time. You want your apps to respond to state changes and present an updated UI when necessary. React offers a nice solution for the state management of modern web applications.

You create state in a React component by declaring a ```state``` property on the component class in its ```constructor```. This initializes the component with ```state``` when it is created. The ```state``` property must be set to a JavaScript ```object```. Declaring it looks like this:

```
this.state = {

}
```

You have access to the ```state``` object throughout the life of your component. You can update it, render it in your UI, and pass it as props to child components. The ```state``` object can be as complex or as simple as you need it to be. Note that you must create a class component by extending ```React.Component``` in order to create state like ```this```.

There is a component in the code editor that is trying to render a ```firstName``` property from its ```state```. However, there is no ```state``` defined. Initialize the component with ```state``` in the ```constructor``` and assign your name to a property of ```firstName```.

```
class StatefulComponent extends React.Component {
  constructor(props) {
    super(props);
    // Only change code below this line
    this.state = {
      firstName: "Name"
    }
    // Only change code above this line
  }
  render() {
    return (
      <div>
        <h1>{this.state.firstName}</h1>
      </div>
    );
  }
};
```

# Render State in the User Interface

Once you define a component's initial state, you can display any part of it in the UI that is rendered. If a component is stateful, it will always have access to the data in ```state``` in its ```render()``` method. You can access the data with ```this.state```.

If you want to access a state value within the ```return``` of the render method, you have to enclose the value in curly braces.

```state``` is one of the most powerful features of components in React. It allows you to track important data in your app and render a UI in response to changes in this data. If your data changes, your UI will change. React uses what is called a virtual DOM, to keep track of changes behind the scenes. When state data updates, it triggers a re-render of the components using that data - including child components that received the data as a prop. React updates the actual DOM, but only where necessary. This means you don't have to worry about changing the DOM. You simply declare what the UI should look like.

Note that if you make a component stateful, no other components are aware of its ```state```. Its ```state``` is completely encapsulated, or local to that component, unless you pass state data to a child component as ```props```. This notion of encapsulated ```state``` is very important because it allows you to write certain logic, then have that logic contained and isolated in one place in your code.

In the code editor, ```MyComponent``` is already stateful. Define an ```h1``` tag in the component's render method which renders the value of ```name``` from the component's state.

Note: The ```h1``` should only render the value from ```state``` and nothing else. In JSX, any code you write with curly braces ```{ }``` will be treated as JavaScript. So to access the value from ```state``` just enclose the reference in curly braces.

```
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'freeCodeCamp'
    }
  }
  render() {
    return (
      <div>
        { /* Change code below this line */ }
          <h1>{this.state.name}</h1>
        { /* Change code above this line */ }
      </div>
    );
  }
};
```

# Render State in the User Interface Another Way

There is another way to access ```state``` in a component. In the ```render()``` method, before the ```return``` statement, you can write JavaScript directly. For example, you could declare functions, access data from ```state``` or ```props```, perform computations on this data, and so on. Then, you can assign any data to variables, which you have access to in the ```return``` statement.

In the ```MyComponent``` render method, define a ```const``` called ```name``` and set it equal to the name value in the component's ```state```. Because you can write JavaScript directly in this part of the code, you don't have to enclose this reference in curly braces.

Next, in the return statement, render this value in an ```h1``` tag using the variable ```name```. Remember, you need to use the JSX syntax (curly braces for JavaScript) in the return statement.

 ```

 ```
