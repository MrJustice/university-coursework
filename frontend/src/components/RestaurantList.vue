<template>
  <v-container>
    <v-container class="search_layout">
      <search-bar></search-bar>
    </v-container>
    <v-divider class="mt-0"></v-divider>
  </v-container>
</template>

<script>
import SearchBar from './SearchBar.vue';
import ListMixin from "./mixins/ListMixin";
import RestaurantReserveTable from "./RestaurantReserveTable";

export default {
  name: "RestaurantList",
  components: {
    SearchBar,
    RestaurantReserveTable,
  },
  mixins: [ListMixin],
  data() {
    return {
      base_url: "api/food-establishment/",
    }
  },
  computed: {},
  methods: {},
  watch: {},
  mounted() {},
};
</script>

<style scoped>
.search_layout {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2% auto;
}
</style>