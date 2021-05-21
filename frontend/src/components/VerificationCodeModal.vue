<template>
  <div class="popup_wrapper" ref="popup_wrapper">
    <v-card class="glass column is-4-desktop is-7-mobile has-text-white">
      <v-card-title class="is-size-5 is-flex is-justify-content-center">Подтверждение статуса владельца</v-card-title>
      <v-card-text class="pb-0">
        <div class="columns">
          <div class="column">
            <p class="has-text-white">На указанный номер телефона было отправлено смс с кодом:</p>
            <v-text-field
              v-model="guestCode"
              label="Код"
              hide-details="auto"
              dark
            ></v-text-field>
          </div>
        </div>
      </v-card-text>
      <v-card-actions class="is-flex is-justify-content-center mt-3">
        <button class="button is-primary is-rounded has-text-weight-semibold is-small has-text-black"
          @click="verifyCode"
          >Подтвердить
        </button>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'RestaurantReserve',
  props: {
    guestPhone: null,
  },
  data() {
    return {
      guestCode: null,
    }
  },
  methods: {
    verifyCode() {
      this.$emit('verify', this.guestPhone, this.guestCode)
      this.closePopup()
    },
    closePopup() {
      this.$emit('closePopup');
    },
  },
  mounted() {
    let vm = this;
    document.addEventListener('click', function(item) {
      if (item.target === vm.$refs['popup_wrapper'])
        vm.closePopup();
    })
  },
}
</script>

<style scoped>
.popup_wrapper {
  background: rgba(255,255,255, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 999;
}

.glass {
  position: fixed;
  /* top: 40%;
  left: 5.5%; */
  top: 30%;
  left: 33.5%;
  background: linear-gradient(
    to right bottom,
    rgba(0,0,0, 0.9),
    rgba(0,0,0, 0.75)
  );
  border-radius: 1.5rem;
  backdrop-filter: blur(2rem);
}
</style>