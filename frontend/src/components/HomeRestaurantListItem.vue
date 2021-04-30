<template>
  <div class="column">
    <v-card>
      <v-img
        height="105"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>
      <v-card-title class="s-flex is-justify-content-space-between">
        {{ restaurant_data.full_title }}
        <div>
          <v-rating
            v-model="restaurantRating"
            dense
            medium
            readonly
            half-increments
            fullIcon="star"
            halfIcon="star_half"
            emptyIcon="star_outline"
            color="yellow darken-4"
            background-color="grey darken-1"
          ></v-rating>
        </div>
      </v-card-title>
      <v-card-text class="card-text is-flex is-justify-content-space-between is-size-6">
        <div class="has-text-left">
          {{ restaurant_data.cousine }} кухня <br />Средний чек:&nbsp;{{restaurant_data.average_check}}руб.
        </div>
        <div class="has-text-right">
          {{ restaurant_data.phone }}
          <br />{{ restaurant_data.location }}
        </div>
      </v-card-text>
      <v-card-actions class="is-flex is-justify-content-end">
        <router-link :to="{ name: 'RestaurantPage', params: { id: restaurant_data.id } }">
          <v-btn color="yellow darken-4" text>Подробнее</v-btn>
        </router-link>
        <v-btn 
            @click="showReservePopup"
            color="yellow darken-4" 
            text
          >
            Забронировать
        </v-btn>
      </v-card-actions>
    </v-card>
    <restaurant-reserve 
      v-if="isPopupVisible"
      @closePopup="closeReservePopup"
      :restaurant_data="this.restaurant_data">
    </restaurant-reserve>
  </div>
</template>

<script>
import RestaurantReserve from './RestaurantReserve.vue';

export default {
  name: "HomeRestaurantListItem",
  components: {
    RestaurantReserve
  },
  props: {
    restaurant_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  data() {
    return {
      isPopupVisible: false,
    }
  },
  computed: {
    restaurantRating: function() {
      return parseFloat(this.restaurant_data.rating)
    }
  },
  methods: {
    showReservePopup() {
      this.isPopupVisible = true;
    },
    closeReservePopup() {
      this.isPopupVisible = false;
    }
  }
};
</script>

<style scoped>
</style>