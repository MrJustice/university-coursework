<template>
  <v-container>
    <v-img
      height="308"
      contain
      :src="require('../assets/home_image.png')"
    />
    <p class="has-text-centered font-weight-medium is-size-3-desktop mt-6">
      Данный сайт был разработан с целью повышения качества и скорости бронирования мест в заведенях общественного питания.
    </p>
  </v-container>
</template>

<script>
export default {
  name: "About",
  mounted() {
    document.title = 'About | TR'
  },
}
</script>

<style scoped>
</style>
