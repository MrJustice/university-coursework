<template>
  <v-app>
    <nav class="navbar is-transparent navbar-padding-horizontal" role="navigation">
      <div class="container is-max-desktop">
        <div class="navbar-brand">
          <router-link :to="'/'">
            <a class="navbar-item" href="#"></a>
          </router-link>
          <div class="navbar-burger" data-target="navbarExampleTransparentExample">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>

        <div id="navbarExampleTransparentExample" class="navbar-menu">
          <div class="navbar-end">
            <router-link :to="'/'">
              <a class="navbar-item has-text-black" href="#"> Главная </a>
            </router-link>
            <router-link :to="'Home'">
              <a class="navbar-item has-text-black" href="#"> Что-то там </a>
            </router-link>
            <router-link :to="'About'">
              <a class="navbar-item has-text-black" href="#"> О нас </a>
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    <v-main>
      <v-content>
        <v-container fluid>
          <transition name="slide-fade" mode="out-in">
            <router-view></router-view>
          </transition>
        </v-container>
      </v-content>
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

* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: 'Montserrat', Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

nav.navbar {
  font-size: 28px;
  height: 6rem;
}

.navbar-brand a {
  background: url("assets/logo.png") center;
  background-size: contain;
  background-repeat: no-repeat;
  width: 125px;
}
</style>