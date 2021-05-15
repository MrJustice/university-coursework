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
          <div class="navbar-end pt-3">
            <router-link :to="'/'">
              <a class="navbar-item has-text-black" href="#">Главная</a>
            </router-link>

            <template v-if="!$store.state.isAuthenticated">
              <router-link :to="'History'">
                <a class="navbar-item has-text-black" href="#">История</a>
              </router-link>
            </template>

            <router-link :to="'About'">
              <a class="navbar-item has-text-black" href="#">О нас</a>
            </router-link>

            <v-btn class="mt-3 ml-2" color="error" v-if="$store.state.isAuthenticated" @click="logout" outlined small fab>
              <v-icon>mdi-logout</v-icon>
            </v-btn>
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
  methods: {
    logout() {
      this.axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")

      this.$store.commit("REMOVE_TOKEN")
      this.$router.push("/")
    }
  },
  beforeCreate() {
    this.$store.commit('INITIALIZE_STORE')
    
    const token = this.$store.state.token

    if (token) {
      this.axios.defaults.headers.common["Authorization"] = "Token" + token
    } else {
      this.axios.defaults.headers.common["Authorization"] = ""
    }
  }
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
  font-size: 26px;
  // text-transform: uppercase;
  height: 5rem;
}

.navbar-brand a:first-of-type {
  background: url("assets/fork.png") center;
  background-size: contain;
  background-repeat: no-repeat;
  width: 110px;
  height: 110px;
  position: absolute;
  top: 0;
}

.slide-fade-enter-active {
  transition: all .5s ease;
}

.slide-fade-leave-active {
  transition: all .5s cubic-bezier(1, 1, 0, 0);
}

.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(500px);
  opacity: 0;
}
</style>