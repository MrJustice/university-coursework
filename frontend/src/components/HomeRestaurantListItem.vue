<template>
  <div class="column">
    <v-card>
      <v-img 
        max-height="105"
        max-width="408"
        :src="restaurant_data.preview_image"
      ></v-img>
      <v-card-title class="s-flex is-justify-content-space-between is-size-5 pb-2">
        {{ restaurant_data.full_title }}
      </v-card-title>
      <v-card-text class="columns is-multiline card-text is-size-6 pr-0 pb-0">
        <div class="column has-text-left is-7 pb-0">
          {{ restaurant_data.cousine }} кухня
          <br /> Средний чек:&nbsp;{{restaurant_data.average_check}}руб.
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
        </div>
        <div class="column has-text-right is-5 pr-2 pb-0">
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