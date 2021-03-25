<template>
  <v-container>
    <v-img
      height="308"
      contain
      :src="require('../assets/home_image.png')"
    />
    <v-container class="search_layout">
      <div class="columns est-layer">
      	<div class="est-date"></div>
	      <div class="est-time"></div>
	      <div class="est-person"></div>
	      <div class="est-name"></div>
        <div class="est-location"></div>
      </div>
      <button class="find button is-primary has-text-weight-semibold">Поиск</button>
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
                <router-link :to="{name: 'restaurant-page', params: {id: restaurant.id}}">
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
  export default {
    name: 'Home',
    data: () => ({
      restaurants: {},
      menu: false,
      date: new Date().toISOString().slice(0, 10),
      rating: 3.5,
    }),
    computed: {
      computedDateFormatted() {
        return this.formatDate(this.date)
      }
    },
    methods: {
      getHighRatedRestaurants() {
        this.axios
          .get('api/get-four-high-rated/')
          .then(response => this.restaurants = response.data)
      }
    },
    mounted() {
      this.getHighRatedRestaurants();
    }
  }
</script>

<style scoped>
div.est-layer {
  display: flex;
  width: 710px;
  height: 40px;
  border: 2px solid #000000;
  border-radius: 4px;
}

div.est-date,
div.est-time,
div.est-person,
div.est-name {
  width: 15%;
  border-right: 2px solid #000000;
}

div.est-name {
  width: 45%;
}

div.est-location {
  width: 10%;
}

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