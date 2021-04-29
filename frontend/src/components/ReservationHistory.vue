<template>
  <v-container>
    <v-img
      height="308"
      contain
      :src="require('../assets/home_image.png')"
    />
    <p class="has-text-centered font-weight-medium is-size-4-desktop mt-6">
      Для просмотра истории введите номер телефона:
    </p>
    <v-text-field
      style="width: 50%; margin: 0 auto"
      v-model="guestPhone"
      label="Номер телефона"
      hide-details="auto"
    ></v-text-field>
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
      let phone = this.guestPhone;
      this.axios
          .post("/api/guest-history/", phone)
          .then(responce => this.history = responce)
          .catch(error => {})
    }
  },
  mounted() {
    document.title = 'History | TR'
  },
}
</script>

<style scoped>
</style>