<template>
  <v-container>
    <v-img
      height="308"
      contain
      :src="require('../assets/home_image.png')"
    />
    <v-container class="search_layout">
      <search-bar></search-bar>
      <router-link :to="{name: 'RestaurantList', params: {date: search_by_date, time: search_by_time, 
                                                          person: search_by_number_of_persons, name: search_by_name}}">
        <button class="find button is-primary has-text-weight-semibold">Поиск</button>
      </router-link>
    </v-container>
    <v-container>
      <p class="is-size-4 pl-6 mb-1">Лучшие заведения</p>
      <v-divider class="mt-0"></v-divider>
      <div class="columns">
        <div v-for="restaurant in restaurants" :key="restaurant.id" class="column">
          <v-card>
              <v-img
                height="105"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
              ></v-img>
              <v-card-title class="card-title s-flex is-justify-content-space-between">
                {{ restaurant.type + ' "' + restaurant.title + '"'}}
                <div>
                  <v-rating
                    v-model="rating"
                    dense
                    large
                    half-increments
                    fullIcon=star
                    halfIcon=star_half
                    emptyIcon=star_outline
                    color="yellow darken-3"
                    background-color="grey darken-1"
                  ></v-rating>
                </div>
              </v-card-title>
              <v-card-text class="card-text is-flex is-justify-content-space-between is-size-6">
                 <div class="has-text-left">
                  {{ restaurant.cousine }} кухня
                  <br>Средний чек:&nbsp;{{ restaurant.average_check }} руб.
                 </div>
                 <div class="has-text-right">
                   {{ restaurant.phone }}
                   <br>{{ restaurant.location }}
                 </div>
              </v-card-text>
              <v-card-actions>
                <router-link :to="{name: 'RestaurantPage', params: {id: restaurant.id}}">
                  <v-btn color="yellow darken-3" text>Подробнее</v-btn>
                </router-link>
                <v-btn color="yellow darken-3" text>Забронировать</v-btn>
              </v-card-actions>
          </v-card>
        </div>
      </div>
    </v-container>
  </v-container>
</template>

<script>
import SearchBar from './SearchBar.vue';

  export default {
    name: 'Home',
    components: { SearchBar },
    data: () => ({
      restaurants: {},
      rating: 3.5,
    }),
    methods: {
      getHighRatedRestaurants() {
        this.axios
          .get('api/get-four-high-rated/')
          .then(response => this.restaurants = response.data)
          .catch(responce => console.log("Connection lost"))
      },
    },
    mounted() {
      this.getHighRatedRestaurants();
    }
  }
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