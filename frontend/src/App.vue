<template>
  <v-app>
    <nav class="navbar is-transparent navbar-padding-horizontal" role="navigation">
      <div class="container is-max-desktop">
        <div class="navbar-brand">
          <router-link class="navbar-item" :to="'/'"></router-link>
          <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
          <div class="navbar-end">
            <router-link :to="'/'">
              <a class="navbar-item has-text-black " href="#"> Главная </a>
            </router-link>
            <router-link :to="'About'">
              <a class="navbar-item has-text-black" href="#"> О нас </a>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <v-main>
      <v-container fluid>
        <transition name="slide-fade" mode="out-in">
          <router-view></router-view>
        </transition>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "app",

  data: () => ({}),
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
@font-face {
  font-family: 'Montserrat';
  src: url('assets/fonts/Montserrat-Regular.ttf');
}

#app {
  font-family: 'Montserrat', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

nav.navbar {
  font-size: 30px;
  height: 5.5rem;
}

.navbar-brand a:first-of-type {
  background: url("assets/logo.png") center;
  background-size: contain;
  background-repeat: no-repeat;
  width: 125px;
}
</style>