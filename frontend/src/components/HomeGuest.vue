<template>
  <v-container>
    <v-img height="308" contain :src="require('../assets/home_image.png')"/>
    <v-container class="search_layout">
      <search-bar></search-bar>
      <router-link :to="{name: 'RestaurantList'}">
        <button class="find button is-primary is-outlined has-text-weight-semibold">Поиск</button>
      </router-link>
    </v-container>
    <v-container>
      <p class="is-size-4 pl-6 mb-1">Лучшие заведения</p>
      <v-divider class="mt-0"></v-divider>
      <div class="columns">
        <home-restaurant-list-item
          v-for="restaurant in restaurants"
          :key="restaurant.id"
          :restaurant_data="restaurant"
          ></home-restaurant-list-item>
      </div>
    </v-container>
  </v-container>
</template>

<script>
import SearchBar from './SearchBar.vue';
import HomeRestaurantListItem from './HomeRestaurantListItem.vue'

export default {
  name: 'HomeGuest',
  components: { SearchBar, HomeRestaurantListItem },
  data() {
    return {
      restaurants: {},
    }
  },
  methods: {
    getHighRatedRestaurants() {
      this.axios
        .get('api/get-high-rated/')
        .then(response => this.restaurants = response.data)
        .catch(error => console.log("Connection lost"))
    },
  },
  mounted() {
    document.title = 'Home | TR'
    this.getHighRatedRestaurants();
  }
};
</script>

<style scoped>
.search_layout {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2% auto;
}

.find {
  margin: 0.5% auto 0;
}
</style>