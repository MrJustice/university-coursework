<template>
  <v-container>
    <div class="data__title is-flex is-size-3 pl-9 mb-1">
      {{ restaurantData.full_title }}
    </div>
    <v-img height="308" contain :src="require('../assets/home_image.png')"/>
    <v-container class="mt-3">
      <p class="is-size-4 pl-6 mb-1">Описание</p>
      <v-divider class="mt-0"></v-divider>
      <div class="columns">
        <div class="column content is-medium has-text-justified description">
          <p>{{ restaurantData.description }}</p>
        </div>
        <div class="column is-one-third content is-medium is-flex is-flex-direction-column is-align-items-baseline stats"> 
          <p class="has-text-weight-semibold is-align-self-center">Кухня: <span>{{ restaurantData.cousine }}</span></p>
          <p class="has-text-weight-semibold is-align-self-center">Средний чек: <span>{{ restaurantData.average_check }} руб.</span></p>
          <p class="has-text-weight-semibold is-align-self-center">Телефон: <span>{{ restaurantData.phone }}</span></p>
          <p class="has-text-weight-semibold is-align-self-center">Время работы: <span>{{ restaurantData.working_hours }}</span></p>
          <p class="has-text-weight-semibold is-align-self-center">Адрес: <span>{{ restaurantData.location }}</span></p>
          <v-btn class="button is-primary is-outlined has-text-weight-semibold is-align-self-center"
            @click="showReservePopup"
            text
          >
            Забронировать
          </v-btn>
        </div>
      </div>
    </v-container>
    <restaurant-reserve 
      v-if="isPopupVisible"
      @closePopup="closeReservePopup"
      :restaurant_data="this.restaurantData">
    </restaurant-reserve>
  </v-container>
</template>

<script>
import RestaurantReserve from './RestaurantReserve.vue';

export default {
  name: "RestaurantDetails",
  components: {
    RestaurantReserve
  },
  data() {
    return {
      isPopupVisible: false,
      restaurantId: this.$route.params.id,
      restaurantData: {},
      restaurantRating: 0.0,
    }
  },
  methods: {
    getRestaurantData() {
      this.axios
        .get("/api/food-establishment/" + this.restaurantId)
        .then(response => {
          this.restaurantData = response.data
          this.restaurantRating = parseFloat(response.data.rating)
          document.title = this.restaurantData.title + " | TR"
        })
        .catch(error => console.log("Connection lost"))
    },
    showReservePopup() {
      this.isPopupVisible = true;
    },
    closeReservePopup() {
      this.isPopupVisible = false;
    }
  },
  mounted() {
    this.getRestaurantData();
  }
};
</script>

<style scoped>
div.description {
  text-indent: 1.2em;
}
span {
  font-weight: 400;
}
div.stats p {
  margin-bottom: 1.5%;
}
button {
  border-color: linear-gradient(98.96deg, #0ADA12 0%, #0ADA9B 100%);
}
</style>
