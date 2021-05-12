<template>
  <div>
    <p class="mt-3 mb-6 is-size-4">Список зарезервированых столиков на сегодня</p>
    <v-data-table 
      :headers="headers"
      :items="items"
      :items-per-page="10"
      no-data-text="Нет данных"
      :footer-props="{
        showFirstLastPage: true,
        firstIcon: 'mdi-arrow-collapse-left',
        lastIcon: 'mdi-arrow-collapse-right',
        prevIcon: 'mdi-minus',
        nextIcon: 'mdi-plus'
      }">
      <template v-if="items" v-slot:item="{ item, index }">
        <tr>
          <td>{{ index+1 }}</td>
          <td>{{ item.guest_food_establishment.guest.first_name }}</td>
          <td>{{ item.guest_food_establishment.guest.phone }}</td>
          <td>{{ formatDate(item.start_date) }}</td>
          <td class="has-text-centered pr-8" v-if="item.table">{{ item.table.number }}</td>
          <td class="has-text-centered pr-8" v-else></td>
          <td class="has-text-centered pr-8">{{ item.number_of_persons }}</td>
          <td>
            <v-icon class="ml-2" @click="editItem(item)">
              mdi-pencil
            </v-icon>
            <v-icon class="ml-5" @click="deleteItem(item)">
              mdi-delete
            </v-icon>
          </td>
        </tr>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "HomeAuth",
  data() {
    return {
      items: [],
      headers: [
        {
          align: 'left',
          text: '№',
          sortable: true,
          value: 'id'
        },
        {
          align: 'left',
          text: 'Имя',
          sortable: true,
          value: 'guest_food_establishment.guest.first_name'
        },
        {
          align: 'left',
          text: 'Номер телефона',
          sortable: true,
          value: 'guest_food_establishment.guest.phone'
        },
        {
          align: 'left',
          text: 'На какое время',
          sortable: true,
          value: 'start_date'
        },
        {
          align: 'center',
          text: 'Номер столика',
          sortable: true,
          value: 'table.number'
        },
        {
          align: 'center',
          text: 'Колв-во человек',
          sortable: true,
          value: 'number_of_persons'
        },
        {
          align: 'left',
          text: 'Действия',
          sortable: false,
          value: ''
        }
      ]
    }
  },
  computed: {},
  methods: {
    fetchItems() {
      let params = {"restaurantId": 1}
      this.axios
        .get('api/get-reservations/', {params: params})
        .then(response => this.items = response.data)
        .catch(error => {});
    },
    formatDate(datetime) {
      let date = new Date(datetime)
      return date.toLocaleString("ru-RU", { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit'})
    }
  },
  mounted() {
    this.fetchItems()
    document.title = ' | TR'
  },
}
</script>

<style lang="scss" scoped>
.v-data-table::v-deep th {
  font-size: 16px !important;
}
.v-data-table::v-deep td {
  font-size: 16px !important;
}
</style>