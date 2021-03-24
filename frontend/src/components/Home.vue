<template>
  <v-container>
    <v-img
      :src="require('../assets/home_image.png')"
      contain
      height="300"
    />
    <v-container class="search_layout">
      <div class="columns est-layer">
      	<div class="est-date"></div>
	      <div class="est-time"></div>
	      <div class="est-person"></div>
	      <div class="est-name"></div>
        <div class="est-location"></div>
      </div>
      <button class="find button is-primary">Поиск</button>
    </v-container>
    <v-container>
      <p class="is-size-4 pl-6 mb-1">Лучшие заведения</p>
      <v-divider class="mt-0"></v-divider>
      <ul>
        <li v-for="restaurant in restaurants" :key="restaurant.id">
          <v-card>
            <router-link :to="{name: 'restaurant-page', params: {id: restaurant.id}}">
              <v-card-title class="card-title">
                {{ restaurant.title }}
              </v-card-title>
              <v-card-text class="card-text">
                <p>{{ restaurant.cousine }}</p>
              </v-card-text>
            </router-link>
          </v-card>
        </li>
      </ul>
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
ul,
li {
  margin: 0;
  padding: 0;
  list-style: none;
}

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
  margin: 2% auto 0;
}

.find {
  margin: 0.5% auto 0;
}

ul {
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
  margin-top: 1%;
}

li {
  display: inline-block;
  width: 31.5%;
  margin-right: 2%;
  margin-bottom: 3%;
  z-index: 2;
}

li:nth-child(3n) {
  margin-right: 0;
}
</style>