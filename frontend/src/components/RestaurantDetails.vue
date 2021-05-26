<template>
  <v-container>
    <div class="data__title is-flex is-size-3 pl-9 mb-1">
      {{ restaurantData.full_title }}
    </div>
    <!-- <v-img height="308" contain :src="require('../assets/home_image.png')"/> -->
    <!-- <silent-box :gallery="gallery"></silent-box> -->
    <!-- <v-container id="masorny-wall-layout">
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
    </v-container> -->
    <v-container class="mt-3">
      <div class="details is-flex">
        <p class="is-size-4 pl-6 mb-1" @click="hideGallery()">Описание</p>
        <p class="is-size-4 pl-6 mb-1" @click="showGallery()">Фотогалерея</p>
      </div>
      <v-divider class="mt-0"></v-divider>
      <div class="columns">
        <div v-if="!isGalleryVisible" class="column content is-medium has-text-justified description">
          <p>{{ restaurantData.description }}</p>
        </div>
        <v-container v-else id="masorny-wall-layout">
          <vue-masonry-wall v-if="this.restaurantData.photos" :items="gallery" :options="options" @append="appendMasornyWall">
            <template v-slot:default="{item}">
              <div class="Item">
                <img :src="item.image" style="border: 2px solid #000000;"/>
                <div class="Content">
                  <p>{{item.content}}</p>
                </div>
              </div>
            </template>
          </vue-masonry-wall>
        </v-container>
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
      isGalleryVisible: false,
      options: {
        width: 270,
        padding: {
          default: 7,
          1: 5,
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
    },
    showGallery() {
      this.isGalleryVisible = true;
      this.appendMasornyWall();
    },
    hideGallery() {
      this.isGalleryVisible = false;
    },
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

.details p:after {    
  background: none repeat scroll 0 0 transparent;
  content: "";
  display: block;
  height: 2px;
  background: #0ADA9B;
  transition: width 0.3s ease 0s, left 0.3s ease 0s;
  width: 0;
}
  
.details p:hover:after { 
  width: 100%; 
}

.details p:hover {
  cursor: pointer;
  font-weight: bold;
}

#masorny-wall-layout {
  height: 600px;
  overflow-y: scroll;
  overflow-x: hidden;
  scrollbar-width: none;
  padding: 1px;
}

#masorny-wall-layout::-webkit-scrollbar { 
    display: none;
}

</style>