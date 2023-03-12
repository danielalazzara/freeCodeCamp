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
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <link href="https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css" rel="stylesheet" />
    <title>Daniela Portfolio</title>
  </head>

  <body>
    <header id="header">
      <nav id="navbar">
        <ul class="nav-links">
          <li><a href="#welcome-section" class="nav-link">Welcome</a></li>
          <li><a href="#projects" class="nav-link">Projects</a></li>
          <li><a href="#contact" class="nav-link">Contact</a></li>
        </ul>
      </nav>  
    </header>

    <section id="welcome-section">
      <h1>Hello, I am Daniela</h1>
      <h2><i>a web developer</i></h2>
    </section>

    <section id="projects">
      <h1>These are some of my projects</h1>
      <div class="projects">
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/N3aqOmAyOCAo_tYQVMg6ySin7OaHocNb57bendVVfjtpSzSkm1vSWrC0Z8WFBKS39a2Zi0vVDBwAEP28SoJPE9NzNq4nJL0IydGeGp2gMLh3R_uuM3ExHs8u1tDTKdfw6UqAh0zW_g=w2400" alt="Cafe Menu">
          <p><span>&lt</span>Cafe Menu<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/pvjyi2yiWgQk74LYd3c5u5npgFUbKfyz8wWou8rhatykuupu3dc9LFDqy3RYaHR9ZTi5cjnHPmSawNN1FKy9Vjygafm70SRJMLgaKNwvdAFzaJHXjAj3s17NX2qav5nrrCwAApxfVw=w2400" alt="Cat Photo Gallery">
          <p><span>&lt</span>Cat Photo Gallery<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/XqaR7WjRHS6Fof7ZMGrtqYdS_p3PXRrJ2L2z0QSdCewVs-iC99J5Czc6l8rt8uBB2Du-fxAVc-ZxGjJ9HCr5P1XXo8mVHEVpcGq0mGuKW88wc1FujfFSK5OI6VDIxkNyl8e4z7UvWg=w2400" alt="Picasso Painting">
          <p><span>&lt</span>Picasso Painting<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/AhmTCo7Bkpe-hYLL9bkgd8PN4DVgyo2ctFrkeQ6V9877VKuR5at88z-i7aQW-53vytFC2KZHBAH3_HTFPZyYYsE_Z6qxh1dWskVxxByCvOuVPSer2j8tLWpgbtMkkuopr21YPZ8_6g=w2400" alt="Tribute Page">
          <p><span>&lt</span>Tribute Page<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/V9CJW7gpojIvhz-4dcH-NjpfcDv6Ls0FYdwAM4oRyXaP4BYIm-Yrgb6kho1IcOrfq0lluTjTIjqQ6550EyMQCEuzxpb_ZH3eVxGaeUbhvx6zwx0o97uvWraug7sHRTL-hvicHY2RdA=w2400" alt="Balance Sheet">
          <p><span>&lt</span>Balance Sheet<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/dZ1HEnGS7sXhTbcJ1bQkvkxL1jeTi0tJNUFpME6VnwUwMqvJahVxid0wmR_bzY_6h7Q0prr3Cac6VZLvo-TnKQ0N3oSNeBOTWLRfa6ZONH2Wdjr4Bgorv8rJu3Rj-zBIvZK4ABZ4Pw=w2400" alt="Magazine">
          <p><span>&lt</span>Magazine<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/d8gpTM9PxnQzXhpjCY8XjNavw2Jbgzpyfyr5_qJFRdoQnWKsBq-UqLQrESwTI9li-lAKuALrrapJnD1VEOEXo38Xsw3mB7F_yte9eRjP84dnyJ8iw1amlDv7XmwASgRg_n5djodhKQ=w2400" alt="Landing Page">
          <p><span>&lt</span>Landing Page<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/6_j7kqpeOnSHkejL6ksDJjU7KJgw9x0DQu1xIKZ5pvqKuYRiSk1_ZO9b6OAY3sh-TvjqEWTI_ltGF8aQ5wfxIcrEwIYkhPcRdIiWdWf4w-KwilmTni8c2EsDKuFaqn8pMYnoUFlbOg=w2400" alt="City Skyline">
          <p><span>&lt</span>City Skyline<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/aXs8UWojoiSTdsMPEATNOm8xhoYcJWZTK_Lk_ezBH5jhghY6OPttFdwBculKNHCI8OvvRVUeL4NLQtIzWUH0TQY7h8LNHNYhFCD5NSKUsE-Avp5G0IVNRibY5NbbGbkUpIH1CB8QKQ=w2400" alt="Survey Form">
          <p><span>&lt</span>Survey Form<span>/&gt</span></p>
        </a>
        <a href="#" class="project-tile">
          <img src="https://lh3.googleusercontent.com/3mBKiYFE2xCg2bBCnNN1j-OFthDXODby1dQfS68zWK1D5pZX3EC5kX3nHR7RPegqDhcgJHt-3D_0-DFXNRGIcBFDmksH13srC5_Qe79DuMS__HHmCiXRfYbfjKN_gR991ENgXUxmEA=w2400" alt="Registration Form">
          <p><span>&lt</span>Registration Form<span>/&gt</span></p>
        </a>
      </div>
    </section>

    <section id="contact">
      <h1>Let's work together...</h1>
      <h2><i>How do you take your coffee?</i></h2>
      <div class="social-medias">
        <a href="" class="social-media">
          <i class="ri-facebook-box-fill ri-2x"></i>
          <p>Facebook</p>
        </a>
        <a href="https://github.com/danielalazzara" target="_blank" id="profile-link" class="social-media">
          <i class="ri-github-fill ri-2x"></i>
          <p>GitHub</p>
        </a>
        <a href="" class="social-media">
          <i class="ri-fire-fill ri-2x"></i>
          <p>FreeCodeCamp</p>
        </a>
        <a href="" class="social-media">
          <i class="ri-at-line ri-2x"></i>
          <p>Send a mail</p>
        </a>
        <a href="" class="social-media">
          <i class="ri-cellphone-fill ri-2x"></i>
          <p>Call me</p>
        </a>
      </div>
    </section>

    <footer>Created by Daniela Lazzara, March 2023</footer>

  </body>
</html>
```

# css file

```css
:root {
  --white: #ffffff;
  --black: #000000;
  --red: #b3003b;
  --grey: #333333;
  --blue: #44586e;
  --dark-blue: #303f4f;
  --orange: #ff751a;
}

* {
  margin: 0;
  font-family: Sans-Serif;
}

#navbar {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: right;
  position: fixed;
  width: 100%;
  top: 0;
  background-color: var(--red);
  color: var(--white);
  font-size: 20px;
  padding: 20px 0;
}

.nav-links {
  display: flex;
  list-style: none;
}

.nav-links a {
  text-decoration: none;
  color: var(--white);
  margin-left: 20px;
  padding: 0 10px;
}

.nav-links a:hover {
    text-decoration: underline;
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
  padding: 70px 0;
  min-height: 100vh;
}

#welcome-section {
  background-color: var(--grey);
  text-align: center;
}

h1 {
  color: var(--white); 
  font-size: 80px;
  margin-top: 300px;
  font-family: Sans-Serif;
  font-weight: 550;
}

h2 {
  color: var(--red); 
  font-size: 50px;
  margin-top: 10px;
  font-family: Sans-Serif;
  font-weight: 550;
}

#projects {
  background-color: var(--blue);
  color: var(--white);
}

#projects h1 {
  color: var(--white); 
  font-size: 60px;
  margin-top: 10px;
  margin-bottom: 100px;
  font-family: Sans-Serif;
  font-weight: 400;
  border-bottom: 5px solid var(--white);
  width: fit-content;
  margin: auto;
}

#projects .projects {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  padding: 20px;
  place-items: center;
  max-width: 1200px;
  margin: auto;
}

#projects .project-tile {
  height: 525px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: var(--dark-blue);
  text-decoration: none;
  color: var(--white);
  border-radius: 5px;
  box-shadow: 8px 8px 10px 5px rgba(100, 100, 100, 0.4);
}

#projects .project-tile img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

#projects .project-tile p {
  font-size: 20px;
  padding: 10px;
}

#projects .project-tile span {
  opacity: 0%;
  padding: 0 5px;
}

#projects .project-tile:hover span {
  opacity: 100%;
  color: var(--orange);
  transition: opacity 0.25s ease-in;
}

#contact {
  background-color: var(--grey);
  text-align: center;
}

#contact h2 {
  font-size: 30px;
}

#contact p {
  color: var(--white);
}

#contact .social-medias {
  display: flex;
  flex-wrap: wrap;
  max-width: 1000px;
  justify-content: space-around;
  margin: auto;
  margin-top: 50px;
  font-size: 20px;
}

#contact .social-media {
  text-decoration: none;
  color: var(--white);
  transition: transform 0.25s ease-in;
  display: flex;
  align-items: center;
  margin: 20px;
}

#contact .social-media:hover {
  transform: translateY(10px);
}

footer {
  border-top: 6px solid var(--red);
  color: var(--white);
  background-color: var(--grey);
  font-size: 25px;
  padding: 30px;
  display: flex;
  align-items: right;
  justify-content: right;
}

@media (prefers-reduced-motion: no-preference) {
  * {
    scroll-behavior: smooth;
  }
}
```
