<template>
  <div class="popup_wrapper" ref="popup_wrapper">
    <v-card class="glass column is-4-desktop is-7-mobile has-text-white">
      <v-card-title>{{ restaurant_data.type + ' "' + restaurant_data.title + '"' }}</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="guestName"
          label="Ваше имя"
          hide-details="auto"
          dark
        ></v-text-field>
        <v-text-field
          v-model="guestPhone"
          label="Номер телефона"
          hide-details="auto"
          dark
        ></v-text-field>
      </v-card-text>
      <v-card-title>Свободное время</v-card-title>
      <v-card-text>
        <v-chip-group
          active-class="yellow darken-4"
          mandatory
          v-model="selection"
        >
          <v-chip>5:30</v-chip>
          <v-chip>7:30</v-chip>
          <v-chip>8:00</v-chip>
          <v-chip>9:00</v-chip>
          <!-- <v-chip v-for="time in possibleTimeChoices" :key="time">{{time}}</v-chip> -->
        </v-chip-group>
      </v-card-text>
      <v-card-actions class="is-flex is-justify-content-space-between px-4">
        <button class="button is-danger is-rounded has-text-weight-semibold is-small has-text-black"
          @click="closePopup"
          >Отмена
        </button>
        <button class="button is-primary is-rounded has-text-weight-semibold is-small has-text-black"
          @click="closePopup"
          >Забронировать
        </button>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'RestaurantReserve',
  props: {
    restaurant_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  data() {
    return {
      guestName: '',
      guestPhone: '',
      selection: null,
      timeChoices: ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', 
                    '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                    '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
                    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
                    '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30'],
    }
  },
  computed: {
    possibleTimeChoices() {
      console.log('qweqwe')
    }
  },
  methods: {
    reserve() {
      this.axios
          .post()
          .then()
          .catch(error => {})
    },
    closePopup() {
      this.$emit('closePopup');
    }
  },
  mounted() {
    let vm = this;
    document.addEventListener('click', function(item) {
      if (item.target === vm.$refs['popup_wrapper'])
        vm.closePopup();
    })
  }
}
</script>

<style scoped>
.popup_wrapper {
  background: rgba(255,255,255, 0.9);
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
  top: 35%;
  left: 35%;
  background: linear-gradient(
    to right bottom,
    rgba(0,0,0, 0.8),
    rgba(0,0,0, 0.6)
  );
  border-radius: 1.5rem;
  backdrop-filter: blur(2rem);
}

@media screen {
  
}
</style>