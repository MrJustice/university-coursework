<template>
  <v-container>
    <v-img
      height="308"
      contain
      :src="require('../assets/home_image.png')"
    />
    <v-container class="search_layout">
      <div class="columns est-layer">
      	<div class="est-date">
          <v-menu
            v-model="menu"
            :close-on-content-click="false"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                class="mt-0 pt-1 mx-1"
                v-model="computedDateFormatted"
                prepend-inner-icon="event"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker locale="ru" 
              v-model="search_by_date"
              @input="menu = false"
              no-title 
              scrollable
            ></v-date-picker>
          </v-menu>
        </div>
	      <div class="est-time">
          <v-select class="mt-0 pt-1 mx-1"
            v-model="this.search_by_time"
            :items="this.timeChoices"
            prepend-inner-icon="query_builder"
            autocomplete
          ></v-select>
        </div>
	      <div class="est-person">
          <v-select class="mt-0 pt-1 mx-1"
            v-model="this.search_by_number_of_persons"
            :items="this.personChoices"
            prepend-inner-icon="people"
            autocomplete
          ></v-select>
        </div>
	      <div class="est-name">
          <v-text-field class="mt-0 pt-1 mx-1"
            v-model="this.search_by_name"
            label="Поиск по названию"
            prepend-inner-icon="search"
            single-line
            hide-details
            autocomplete
          ></v-text-field>
        </div>
      </div>
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
  export default {
    name: 'Home',
    data: () => ({
      restaurants: {},
      menu: false,
      search_by_date: new Date().toISOString().slice(0, 10),
      search_by_time: '15:00',
      search_by_number_of_persons: 2,
      search_by_name: '',
      timeChoices: ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', 
                    '05:00', '05:30', '06:00', '06:30', '07:30', '08:00', '08:30', '09:30', '10:00', '10:30', 
                    '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30',
                    '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30',
                    '21:00', '21:30', '22:00', '22:30', '23:00', '23:30'],
      personChoices: [1,2,3,4,5,6],
      rating: 3.5,
    }),
    computed: {
      computedDateFormatted() {
        return this.formatDate(this.search_by_date)
      }
    },
    methods: {
      getHighRatedRestaurants() {
        this.axios
          .get('api/get-four-high-rated/')
          .then(response => this.restaurants = response.data)
          .catch(responce => console.log("Connection lost"))
      },
      formatDate(date) {
        if (!date) return null
        const [year, month, day] = date.split('-')
        return `${day}.${month}.${year}`
      },
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
div.est-person {
  width: 22%;
  border-right: 2px solid #000000;
}

div.est-name {
  width: 34%;
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