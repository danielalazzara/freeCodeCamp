<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Table of Contents</summary>

- [html file](#html-file)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# html file

```html
<!DOCTYPE html>
<html lang="en">
  <main id="main">
    <link rel="stylesheet" href="styles.css"/>
    <h1 id="title">Isaac Asimov</h1>
    <figure id="img-div">
      <img id="image" src="https://media.nature.com/lw767/magazine-assets/d41586-020-00176-4/d41586-020-00176-4_17582700.jpg" />
      <figcaption id="img-caption">Isaac Asimov in 1982 on Ellis Island, New York.</figcaption>  
      <img-div id="img-caption"> Credit: Arnold Newman Properties/Getty</img-div>
      <div class="divider"></div>
      <h3>Short Biography</h3>
      <p id="tribute-info">Isaac Asimov, (born January 2, 1920, Petrovichi, Russia—died April 6, 1992, New York, New York, U.S.), American author and biochemist, a highly successful and prolific writer of science fiction and of science books for the layperson. He wrote or edited about 500 volumes, of which the most famous are those in the Foundation and robot series.</p>
      <p>For more info please click <a id="tribute-link" href="https://www.nature.com/articles/d41586-020-00176-4" target="_blank" >here</></p>
    </figure>
  </main>
</html>
```

css file

```css
* {
  padding: 0;
  margin: 0;
  background-color: black;
}

h1 {
  text-align: center;
  font-size: 38;
  font-family: 'Open Sans', sans-serif;
}

p {
  font-size: 18;
  font-family: 'Open Sans', sans-serif;
}

img {
  margin: auto;
  max-width: 100%;
  height: auto;
  margin: auto;
  display: block;
}

main {
  background-color: black;
  color: white;
  text-align: auto;
}

.divider {
  border-bottom: 1px solid #888989;
  margin: 2px 0;
}

figcaption {
  text-align: center;
}
```
