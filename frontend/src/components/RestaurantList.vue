<template>
  
</template>

<script>
import ListMixin from './mixins/ListMixin'

import RestaurantReserveTable from './RestaurantReserveTable'

export default {
  name: 'RestaurantList',
  components: {
    RestaurantReserveTable
  },
  mixins: [ListMixin],
  data: () => ({
    base_url: 'api/food-establishment/',
  }),
  computed: {

  },
  methods: {

  },
  watch: {

  },
  mounted() {

  },
}
</script>

<style scoped>

</style>