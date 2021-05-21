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
      @keyup.enter="showCodeVerificationPopup()"
    ></v-text-field>
    <table v-if="history" id="main-table" class="table is-striped is-hoverable mt-8 hidden" style="width: 90%; margin: 0 auto">
      <thead>
        <tr>
          <th><abbr title="Номер">№</abbr></th>
          <th>Заведение</th>
          <th>Время</th>
          <th>Номер столика</th>
          <th>Кол-во гостей</th>
          <th>Комментарий</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(reservation, index) in history" :key="reservation.id">
          <td>{{ index+1 }}</td>
          <td>{{ reservation.guest_food_establishment.food_establishment.full_title }}</td>
          <td>{{ formatDate(reservation.start_date) }}</td>
          <td class="has-text-centered pr-8">{{ reservation.table.number }}</td>
          <td class="has-text-centered pr-8">{{ reservation.number_of_persons}}</td>
          <td>{{ reservation.comment}}</td>
        </tr>
      </tbody>
    </table>
    <verification-code-modal 
      v-if="isPopupVisible" 
      :guestPhone="guestPhone"
      @verify="getHistory"
      @closePopup="closeCodeVerificationPopup">
    </verification-code-modal>
  </v-container>
</template>

<script>
import { toast } from 'bulma-toast'
import VerificationCodeModal from './VerificationCodeModal.vue';

export default {
  name: "ReservationHistory",
  components: {
    VerificationCodeModal,
  },
  data() {
    return {
      isPopupVisible: false,
      guestPhone: null,
      history: null,
    }
  },
  methods: {
    sendVerificationCode() {
      let params = {"phone": this.guestPhone}
      this.axios
          .get("/api/send-sms-code/", {params: params})
          .then(responce => {})
          .catch(error => {})
    },
    getHistory(phone, code) {
      console.log(phone)
      console.log(code)
      let params = {"phone": phone, "verificationCode": code}
      this.axios
          .get("/api/guest-history/", {params: params})
          .then(responce => {
            this.history = responce.data
          })
          .catch(error => {
            if (error.response) {
              toast({
                message: 'Неверный код',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 3000,
                position: 'bottom-right'
            })
            }
          })
    },
    formatDate(datetime) {
      let date = new Date(datetime)
      return date.toLocaleString("ru-RU", { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit'})
    },
    showCodeVerificationPopup() {
      this.sendVerificationCode()
      this.isPopupVisible = true;
    },
    closeCodeVerificationPopup() {
      this.isPopupVisible = false;
    }
  },
  mounted() {
    document.title = 'History | TR'
  },
}
</script>

<style scoped>
</style>