<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Table of Contents</summary>

- [html file](#html-file)
- [css file](#css-file)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# html file

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AC Personal Training Studio</title>
    <link rel="stylesheet" href="styles.css"/>
  </head>

  <body>
    <header id="header">
      <nav id="nav-bar">
        <div class="logo-container">
          <img  
            id="header-img"
            src="https://t3.ftcdn.net/jpg/03/76/06/08/360_F_376060885_G8bX8DQ4UFAqpaOAoT7G0xxZrvD05BxC.jpg" 
            alt="logo" 
          />
          <span class="logo-name"> Personal Training Studio</span>
          <ul class="nav-links">
            <li ><a href="#About" class="nav-link">ABOUT</a></li>
            <li ><a href="#Personal_trainers" class="nav-link">PERSONAL TRAINERS</a></li>
            <li ><a href="#Contact" class="nav-link">CONTACT</a></li>
          </ul>
        </div>
      </nav>  
    </header>

    <section id="title">
      <h1 class="Title">Take Your Fitness
To The Next Level</h1>
    </section>

    <section>
      <h2>Please type here your e-mail address:</h2>
      <form id="form" action="https://www.freecodecamp.com/email-submit">
        <input id="email" type="email"    placeholder="Please enter your email" name="email" required />
        <input type="submit" id="submit" value="SUBMIT" />
      </form>
    </section>

    <section>
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYvGBVSZb3mjYGLmpxz5ulynVJUSX-mabw1A&usqp=CAU" alt="weights" width="418" />
      <img src="https://media.architecturaldigest.com/photos/5e8610a986a09a0009065e1a/2:1/w_4200,h_2100,c_limit/20190822_Kasler_Nashville_09_Gym_008.jpg" alt="gym" width="555" />
      <img src="https://www.thespruce.com/thmb/vAsg7QjNedjF9cOl4BawkypBWBE=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/NW3-Gym-01-980x654-6dd93bd9f1fc47828bcb424622dbb2ea.jpg" alt="gym" width="415" />
    </section>

    <section id="About">
      <h3>What we offer</h3>
      <div class="About">
        <p>Certified Personal Trainers</p>
      </div>
      <hr>
      <div class="About">
        <p>Personalized workout programs designed to effectively help you make progress</p>
      </div>
      </hr>
      <hr>
      <div class="About">
        <p>High quality gym equipment for a full-body workout</p>
      </div>
      </hr>
    </section>

    <section>
      <h3>Personal Trainers</h3>
    </section>


    <section id="Personal_trainers">
      <div class="Personal_trainers">
        <div class="grid">
          <div class="image">
            <img src="https://athleticsweekly.com/wp-content/uploads/2020/11/PT-image-via-OriGym.jpg" alt="PT" width="250" />
          </div>
          <div class="text">
            <h2>Mark Green</h2>
            <h5>Dedicated fitness professional with a passion for improving client health, wellness and quality of life and with weight management expertise. Deliver high-energy training using the latest techniques in exercise science, cardio programs and strength training.
            </h5>
          </div>
        </div>

        <div class="grid">
          <div class="image">
            <img src="https://assets.entrepreneur.com/content/3x2/2000/20190620131326-Example-of-Personal-Trainer-Business-Ideas-Bigstock-4000pxW-X-2670pxH-copy.jpeg" alt="PT" width="250" />
          </div>
          <div class="text">
            <h2>John Smith</h2>
            <h5>Spirited personal fitness trainer with weight management expertise and the ability to motivate others toward accomplishing weight loss goals. Designs classes to match the skill and learning levels of all participants. Skilled in personal program development and individual life and body assessments.
            </h5>
          </div>
        </div>

        <div class="grid">
          <div class="image">
            <img src="https://www.k2crossfit.com/wp-content/uploads/2019/11/personal-1277392_1920.jpg" alt="PT" width="250" />
          </div>
          <div class="text">
            <h2>Mary Jane</h2>
            <h5>Effective personal trainer with over 10 years of experience helping clients achieve their health goals. Seeking to join a team of seasoned trainers at In-Shape to encourage, motivate, and shift perspectives on fitness, health, and wellness.
            </h5>
          </div>
        </div>
      </div>
    </section>

    <section id="Contact">
      <iframe 
        id="video"
        width="698" 
        height="297" 
        margin-left="100"
        margin-top="100"
        src="https://www.youtube.com/embed/o3tNt84zxqo" 
        title="Alex Parsons fitness personal trainer intro" frameborder="0"   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>  
    </section> 

  </body>
</html>
```
# css file

```css
:root {
  --white: #ffffff;
  --text-color: #b38600;
  --black: #000000;
}

* {
  margin: 0;
}

body {
  background-color: var(--black);
  color: var(--white)
}

#header-img {
  width: 60px;
  object-fit: contain;
}

#nav-bar {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
  background-color: var(--white);
  color: var(--black);
  padding: 10px;
}

.nav-links {
  display: flex;
  list-style: none;
}

.nav-links a {
  text-decoration: none;
  color: var(--text-color);
  margin-right: 20px;
  padding: 0 10px;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo-name {
  font-size: 20px;
  font-weight: 500;
  font-family: Sans-Serif;
  margin-left: 5px;
}

section::before {
  display: block;
  content: " ";
  margin-top: -100px;
  height: 100px;
  visibility: hidden;
  pointer-events: none;
}

section {
  margin: 40px 20px;
}

h1 {
  color: var(--text-color); 
  font-size: 80px;
  text-align: center;
  margin-top: 100px;
  font-family: Sans-Serif;
  font-weight: 550;
}

#email 
{
  margin-top: 15px;
}

input {
  padding: 8px;
  border: 1px solid var(--text-color);
  border-radius: 5px;
}

@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}

h2 {
  font-family: Sans-Serif;
}

h3 {
  color: var(--text-color); 
  font-size: 60px;
  text-align: center;
  margin-top: 50px;
  font-family: Sans-Serif;
  font-weight: 550;
}

p {
  font-style: Sans-sserif;
  font-weight: 600;
  font-size: 30px;
  text-align: center;
  margin-top: 20px;
}

hr {
  margin: 1.5rem 0;
  border: 0.5px solid var(--text-color);
  align: center;
  margin-left: 150px;
  margin-right: 150px;
}

.image {
  margin-right: 30px;
}

.grid {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: 90%;
  max-width: 3500px;
}

.Personal_trainers {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin-top: 30px;
  margin-bottom: 30px;
}

h5 {
  font-size: 20px;
  text-align: justify;
  margin-top: 10px;
  margin-bottom: 10px;
  font-family: Sans-Serif;
  font-weight: 550;
}
```
