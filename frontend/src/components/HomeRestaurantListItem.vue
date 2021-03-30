<template>
  <div class="column">
    <v-card>
      <v-img
        height="105"
        src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
      ></v-img>
      <v-card-title class="card-title s-flex is-justify-content-space-between">
        {{ restaurant_data.type + ' "' + restaurant_data.title + '"' }}
        <div>
          <v-rating
            v-model="restaurantRating"
            dense
            large
            readonly
            half-increments
            fullIcon="star"
            halfIcon="star_half"
            emptyIcon="star_outline"
            color="yellow darken-3"
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
      <v-card-actions>
        <router-link :to="{ name: 'RestaurantPage', params: { id: restaurant_data.id } }">
          <v-btn color="yellow darken-3" text>Подробнее</v-btn>
        </router-link>
        <v-btn color="yellow darken-3" text>Забронировать</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "HomeRestaurantListItem",
  props: {
    restaurant_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  computed: {
    restaurantRating: function() {
      return parseFloat(this.restaurant_data.rating)
    }
  }
};
</script>

<style scoped>
</style>