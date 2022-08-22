<template>
  <div class="container">
    <div class="box-1">A</div>
    <div class="box-2">B</div>
    <div class="box-3">C</div>
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  font-family: sans-serif;
  font-size: 40px;
  width: 100%;
  min-height: 100vh;
}

[class^="box-"] {
  background-color: skyblue;
  /* Размещаем контейнеры по центру */
  display: grid;
  place-items: center;
}

.wrapper {
  min-height: 100%;
}

.container {
  display: grid;
  gap: 20px;

  /* ! */
  grid-template-columns: repeat(1, 500px);
  grid-template-rows: repeat(3, 500px);
}

@media (min-width: 1224px) {
  .container {
    display: grid;
    gap: 20px;

    /* ! */
    grid-template-columns: repeat(2, 500px);
    grid-template-rows: repeat(2, 500px);
  }
}

@media (min-width: 1920px) {
  .container {
    display: grid;
    gap: 20px;

    /* ! */
    grid-template-columns: repeat(3, 500px);
    grid-template-rows: repeat(1, 500px);
  }
}
</style>
