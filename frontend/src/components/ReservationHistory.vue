<template>
  <v-container>
    <p class="has-text-centered font-weight-medium is-size-4-desktop mt-6">
      Для просмотра истории введите номер телефона:
    </p>
    <v-text-field
      id="main-p"
      style="width: 50%; margin: 0 auto"
      v-model="guestPhone"
      label="Номер телефона"
      hide-details="auto"
      @keyup.enter="getHistory()"
    ></v-text-field>
    <table v-if="history" id="main-table" class="table is-striped is-hoverable mt-8 hidden" style="width: 60%; margin: 0 auto">
      <thead>
        <tr>
          <th><abbr title="Номер">№</abbr></th>
          <th>Заведение</th>
          <th>Время</th>
          <th>Номер столика</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(reservation, index) in history" :key="reservation.id">
          <td>{{ index+1 }}</td>
          <td>{{ reservation.guest_food_establishment.food_establishment.full_title }}</td>
          <td>{{ formatDate(reservation.start_date) }}</td>
          <td>{{ reservation.table.number }}</td>
        </tr>
      </tbody>
    </table>
  </v-container>
</template>

<script>
export default {
  name: "ReservationHistory",
  data() {
    return {
      guestPhone: null,
      history: null,
    }
  },
  methods: {
    getHistory() {
      this.axios
          .post("/api/guest-history/", {'phone': this.guestPhone})
          .then(responce => {
            this.history = responce.data
          })
          .catch(error => {})
    },
    formatDate(datetime) {
      let date = new Date(datetime)
      return date.toLocaleString("ru-RU", { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit'})
    },
  },
  mounted() {
    document.title = 'History | TR'
  },
}
</script>

<style scoped>
</style>