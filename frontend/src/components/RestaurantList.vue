<template>
  <v-container>
    <v-container class="search_layout">
      <search-bar></search-bar>
    </v-container>
    <v-divider class="mt-0"></v-divider>
    <div class="columns">
      <div class="column is-3 is-offset-1 is-flex is-flex-direction-column">
        <span class="is-size-5 has-text-weight-semibold">Тип заведения</span>
        <v-list>
          <v-list-item v-for="item in restaurantTypeItems" :key="item.value">
            <v-checkbox
              v-model="restaurantTypeList"
              :value="item.value" 
              :label="item.label"
              dense
              hide-details
            ></v-checkbox>
          </v-list-item>
        </v-list>
        <span class="is-size-5 has-text-weight-semibold mt-2">Кухня</span>
        <v-list>
          <v-list-item v-for="item in restaurantCousineItems" :key="item.value">
            <v-checkbox
              v-model="restaurantCousineList"
              :value="item.value" 
              :label="item.label"
              dense
              hide-details
            ></v-checkbox>
          </v-list-item>
        </v-list>
      </div>
      <div class="column is-7">
        <restaurant-list-item
          v-for="item in items"
          :key="item.id"
          :restaurant_data="item"
          ></restaurant-list-item>
        <restaurant-list-item
          v-for="item in items"
          :key="item.id"
          :restaurant_data="item"
          ></restaurant-list-item>
      </div>
    </div>
  </v-container>
</template>

<script>
import SearchBar from './SearchBar.vue';
import RestaurantListItem from './RestaurantListItem.vue'
import RestaurantReserveTable from "./RestaurantReserveTable";
export default {
  name: "RestaurantList",
  components: {
    SearchBar,
    RestaurantReserveTable,
    RestaurantListItem
  },
  data() {
    return {
      items: {},
      restaurantTypeItems: 
      [
        {
          value: 'B',
          label: 'Бар'
        },
        {
          value: 'C',
          label: 'Кафе'
        },
        {
          value: 'R',
          label: 'Ресторан'
        }
      ],
      restaurantCousineItems:
      [
        {
          value: 'BY',
          label: 'Национальная'
        },
        {
          value: 'RU',
          label: 'Русская'
        },
        {
          value: 'FR',
          label: 'Французская'
        },
        {
          value: 'I',
          label: 'Итальянская'
        },
        {
          value: 'CN',
          label: 'Китайская'
        },
        {
          value: 'KR',
          label: 'Корейская'
        }
      ],
      restaurantTypeList: [],
      restaurantCousineList: [],
      restaurantPriceList: ['10-30 руб.','31-60 руб.','60-100 руб.','100+ руб.']
    }
  },
  computed: {},
  methods: {
    fetchItems() {
      let params = {
        'filter_by_type': this.restaurantTypeList,
        'filter_by_cousine': this.restaurantCousineList
      }
      this.axios
        .get('api/food-establishment/', { params: params })
        .then(response => this.items = response.data)
        .catch(error => {});
    },
  },
  watch: {
    restaurantTypeList: {
      deep: true,
      handler() {
        this.fetchItems();
      }
    },
    restaurantCousineList:{
      deep: true,
      handler() {
        this.fetchItems();
      }
    },
  },
  mounted() {
    this.fetchItems();
  },
};
</script>

<style scoped>
.search_layout {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2% auto;
}
.v-list {
  padding-top: 0;
}
.v-list-item {
  min-height: 38px;
}
.v-list-item .v-input {
  margin-top: 0px;
}
</style>