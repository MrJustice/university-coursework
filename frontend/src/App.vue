<template>
  <v-app>
    <nav class="navbar is-transparent navbar-padding-horizontal" role="navigation">
      <div class="container is-widescreen">
        <div class="navbar-brand">
          <a class="navbar-item" href="#">
            <img :src="require('@/assets/logo.png')" alt="Logo"/>
          </a>
          <div
            class="navbar-burger"
            data-target="navbarExampleTransparentExample"
          >
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>

        <div id="navbarExampleTransparentExample" class="navbar-menu">
          <div class="navbar-end">
            <a class="navbar-item has-text-black" href="#"> Home </a>
            <a class="navbar-item has-text-black" href="#"> Something </a>
            <a class="navbar-item has-text-black" href="#"> About </a>
          </div>
        </div>
      </div>
    </nav>
    <v-main>
      <Home />
    </v-main>
  </v-app>
</template>

<script>
import Home from "./components/Home";

export default {
  name: "App",

  components: {
    Home,
  },

  data: () => ({}),
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

nav.navbar {
  font-family: 'Montserrat';
  font-size: 28px;
  height: 5rem !important;
}
</style>