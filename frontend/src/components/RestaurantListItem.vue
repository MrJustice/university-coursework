<template>
  <div class="columns">
    <div class="column is-3">
      <v-img style="border: 2px solid #000000;"
        height="98%"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>
    </div>
    <div class="column is-9">
      <router-link :to="{ name: 'RestaurantPage', params: { id: restaurant_data.id } }">
        <span class="has-text-weight-bold is-size-5 has-text-black">{{ restaurant_data.type + ' "' + restaurant_data.title + '" (' + restaurant_data.cousine + ' кухня)'}}</span>
      </router-link>
      <br> Средний чек: {{ restaurant_data.average_check }} руб.
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
      <v-spacer></v-spacer>
      <div class="columns">
        <div class="column is-8">
          <br> Время работы: {{ restaurant_data.working_hours }}
          <br> Адрес: {{ restaurant_data.location }}
        </div>
        <div class="column is-4 is-flex is-align-items-end is-justify-content-end">
          <v-btn 
            @click="showReservePopup"
            color="yellow darken-4" 
            text
          >
            Забронировать
          </v-btn>
        </div>
      </div>
    </div>
    <restaurant-reserve 
      v-if="isPopupVisible"
      @closePopup="closeReservePopup"
      :restaurant_data="this.restaurant_data"></restaurant-reserve>
  </div>
</template>

<script>
import RestaurantReserve from './RestaurantReserve.vue';

export default {
  name: "RestaurantListItem",
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
    },
  },
  methods: {
    showReservePopup() {
      this.isPopupVisible = true;
    },
    closeReservePopup() {
      this.isPopupVisible = false;
    }
  },
};
</script>

<style scoped>
</style>