<template>
  <component :is="view"></component>
</template>

<script>
import HomeAuth from './HomeAuth.vue';
import HomeGuest from './HomeGuest.vue'

export default {
  name: "Home",
  components: { HomeAuth , HomeGuest },
  computed: {
    view() {
      return this.$store.state.isAuthenticated ? HomeAuth : HomeGuest
    }
  }
}
</script>

<style scoped>
</style>