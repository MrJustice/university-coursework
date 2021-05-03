<template>
  <v-container>
    <v-img 
      id="main-image"
      height="308"
      contain
      :src="require('../assets/home_image.png')"
    />
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
    <table id="main-table" class="table is-striped is-hoverable mt-8 hidden" style="width: 60%; margin: 0 auto">
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
      let image = document.getElementById("main-image")
      let table = document.getElementById("main-table")
      image.classList.add('hidden')
      this.axios
          .post("/api/guest-history/", {'phone': this.guestPhone})
          .then(responce => {
            this.history = responce.data
            image.style.display = "none"
            table.classList.remove("hidden")
            table.classList.add("visible")
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
.visible {
  visibility: visible;
  opacity: 1;
  transition: opacity .7s linear;
}

.hidden {
  visibility: hidden;
  opacity: 0;
  transition: visibility 0s .7s, opacity .7s linear;
}

/* .move-top {
  position: absolute;
  top: 0%;
  left: 50%;
  animation: 1s moving;
}

@keyframes moving {
  0%{top: 20%}
  50%{top: 10%}
  100%{top: 0%}
} */
</style>