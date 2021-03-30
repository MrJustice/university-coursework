<template>
  <v-flex d-flex-col>
    <h3>{{ restaurantData }}</h3>
  </v-flex>
</template>

<script>
export default {
  name: "RestaurantDetails",
  data() {
    return {
      restaurantId: this.$route.params.id,
      restaurantData: {},
    }
  },
  methods: {
    getRestaurantData() {
      this.axios
        .get("/api/food-establishment/" + this.restaurantId)
        .then(response => this.restaurantData = response.data)
        .catch(error => console.log("Connection lost"))
    },
  },
  mounted() {
    this.getRestaurantData();
  }
};
</script>

<style scoped>

</style>
