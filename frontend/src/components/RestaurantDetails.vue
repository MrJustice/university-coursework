<template>
  <v-container>
    <div class="data__title is-flex is-size-3 pl-9 mb-1">
      {{ restaurantData.full_title }}
    </div>
    <!-- <v-img height="308" contain :src="require('../assets/home_image.png')"/> -->
    <!-- <silent-box :gallery="gallery"></silent-box> -->
    <div id="masorny-wall-layout">
      <vue-masonry-wall v-if="this.restaurantData.photos" :items="gallery" :options="options" @append="appendMasornyWall">
        <template v-slot:default="{item}">
          <div class="Item">
            <img :src="item.image"/>
            <div class="Content">
              <p>{{item.content}}</p>
            </div>
          </div>
        </template>
      </vue-masonry-wall>
    </div>
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
import VueMasonryWall from 'vue-masonry-wall';

export default {
  name: "RestaurantDetails",
  components: {
    RestaurantReserve,
    VueMasonryWall,
  },
  data() {
    return {
      isPopupVisible: false,
      restaurantId: this.$route.params.id,
      restaurantData: {},
      restaurantRating: 0.0,
      gallery: [],
      options: {
        width: 300,
        padding: {
          2: 8,
          default: 1
        },
      },
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
        .catch(error => console.log(error))
    },
    showReservePopup() {
      this.isPopupVisible = true;
    },
    closeReservePopup() {
      this.isPopupVisible = false;
    },
    appendMasornyWall() {
      if (this.gallery.length != this.restaurantData.photos.length) {
        for (let i = 0; i < this.restaurantData.photos.length; i++) {
          this.gallery.push({
            image: this.restaurantData.photos[i].picture,
            content: this.restaurantData.photos[i].description,
          })
        }
      }
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

#masorny-wall-layout {
  max-height: 308px;
  overflow: auto;
  overflow-x: hidden;
}
#masorny-wall-layout::-webkit-scrollbar { 
    display: none;  /* Safari and Chrome */
}
</style>
