<template>
  <v-container>
    <agile :nav-buttons="false" :autoplay-speed="5000" :speed="2500" fade pause-on-hover autoplay>
      <img class="slide" :src="require('../assets/home_image.png')"/>
      <img class="slide" :src="require('../assets/home_image2.png')"/>
      <img class="slide" :src="require('../assets/home_image3.png')"/>
      <img class="slide" :src="require('../assets/home_image4.png')"/>
      <img class="slide" :src="require('../assets/home_image5.png')"/>
      <img class="slide" :src="require('../assets/home_image6.png')"/>
    </agile>
    <v-container class="search_layout mt-3">
      <search-bar></search-bar>
      <router-link :to="{name: 'RestaurantList'}">
        <button id="search" class="button is-primary is-outlined has-text-weight-semibold">Поиск</button>
      </router-link>
    </v-container>
    <v-container>
      <p class="is-size-4 pl-6 mb-1">Лучшие заведения</p>
      <v-divider class="mt-0"></v-divider>
      <div class="items-layout columns">
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
import { VueAgile } from 'vue-agile'

export default {
  name: 'HomeGuest',
  components: { SearchBar, HomeRestaurantListItem, agile: VueAgile },
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
  flex-direction: row;
  justify-content: center;
  align-items: center;
  align-content: center;
  padding-bottom: 0;
}

#search {
  margin-left: 50%;
  margin-bottom: 23.5px;
  border-width: 2px;
}

.slide {
  display: block;
	object-fit: contain;
  height: 98%;
}

@media (max-width:73em) {
  .search_layout {
    flex-direction: column;
  }
  #search {
    margin: 0;
    margin-top: 5%;
    border-width: 2px;
  }
}
@media (max-width:50em) {
  .items-layout {
    display: flex;
    flex-direction: column;
  }
}
@media (max-width:46.8em) {

}
@media (max-width:24em) {
}
</style>