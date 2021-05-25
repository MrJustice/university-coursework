<template>
  <v-container>
    <v-container class="search_layout my-1">
      <search-bar></search-bar>
      <button id="search" class="button is-primary is-outlined has-text-weight-semibold">Поиск</button>
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
        <span class="is-size-5 has-text-weight-semibold mt-2">Средний чек</span>
        <v-list>
          <v-list-item v-for="item in restaurantPriceItems" :key="item.value">
            <v-checkbox
              v-model="restaurantPriceList"
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
      </div>
    </div>
  </v-container>
</template>

<script>
import SearchBar from './SearchBar.vue';
import RestaurantListItem from './RestaurantListItem.vue'

export default {
  name: 'RestaurantList',
  components: {
    SearchBar,
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
        },
        {
          value: 'PA',
          label: 'Паназиатская'
        },
        {
          value: 'EU',
          label: 'Европейская'
        }
      ],
      restaurantPriceItems: 
      [
        {
          value: '0,30',
          label: 'до 30 руб.'
        },
        {
          value: '31,60',
          label: '31-60 руб.'
        },
        {
          value: '61,100',
          label: '61-100 руб.'
        },
        {
          value: '100,10000',
          label: '101+ руб.'
        }
      ],
      restaurantTypeList: [],
      restaurantCousineList: [],
      restaurantPriceList: [],
      searchData: {'date': this.$route.params.date, 'time': this.$route.params.time,
                   'person': this.$route.params.person, 'name': this.$route.params.name}
    }
  },
  computed: {},
  methods: {
    fetchItems() {
      let params = {
        'filter_by_type': this.restaurantTypeList,
        'filter_by_cousine': this.restaurantCousineList,
        'filter_by_price': this.restaurantPriceList
      }
      this.axios
        .get('api/food-establishment/', { params: params })
        .then(response => this.items = response.data)
        .catch(error => {});
    },
    findBySearchBar() {
      let params = {
        'filter_by_date': this.$store.state.search_by_date,
        'filter_by_time': this.$store.state.search_by_time,
        'filter_by_persons': this.$store.state.search_by_number_of_persons,
        'filter_by_name': this.$store.state.search_by_name
      }
      console.log(params)
    },
  },
  watch: {
    restaurantTypeList: {
      deep: true,
      handler() {
        this.fetchItems();
      }
    },
    restaurantCousineList: {
      deep: true,
      handler() {
        this.fetchItems();
      }
    },
    restaurantPriceList: {
      deep: true,
      handler() {
        this.fetchItems();
      }
    },
  },
  mounted() {
    this.fetchItems();
    document.title = 'Places | TR'
  },
};
</script>

<style scoped>
.search_layout {
  display: flex;
  align-items: center;
  align-content: center;
  justify-content: center;
}

#search {
  margin-left: 3%;
  margin-bottom: 23.5px;
  border-width: 2px;
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