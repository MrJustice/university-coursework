<template>
  <div class="popup_wrapper" ref="popup_wrapper">
    <v-card class="glass column is-4-desktop is-7-mobile has-text-white">
      <v-card-title class="is-size-3 is-flex is-justify-content-center">{{ restaurant_data.type + ' "' + restaurant_data.title + '"' }}</v-card-title>
      <v-card-text class="pb-0">
        <div class="columns">
          <div class="column">
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
            <div class="is-flex is-justify-content-space-between is-flex-direction-column has-text-white pl-0 pt-5">
              <div class="est-date">
                <v-menu
                  v-model="menu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      class="mt-0 pt-1 mx-1"
                      v-model="computedDateFormatted"
                      prepend-inner-icon="event"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      dark
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    locale="ru"
                    v-model="guestDate"
                    @input="menu = false"
                    no-title
                    scrollable
                    dark
                  ></v-date-picker>
                </v-menu>
              </div>
              <div class="is-flex is-justify-content-end">
                <span>Кол-во гостей:</span>
                <el-input-number
                  class="ml-5"
                  v-model="guestPersons"
                  :min="1"
                  :max="12"
                ></el-input-number>
              </div>
            </div>    
          </div>
          <div class="column">
            <v-select
              label="Выберите столик"
              :items="restaurant_data.tables"
              item-text="number"
              item-value="id"
              v-model="guestTable"
              :clearable="true"
              dark
          ></v-select>
          </div>
        </div>
      </v-card-text>
      <v-card-title>Свободное время</v-card-title>
      <v-card-text>
        <v-chip-group
          active-class="yellow darken-4"
          mandatory
          column
          v-model="guestTime"
        >
          <v-chip class="is-flex is-justify-content-center" 
                  style="width: 11%; margin-right: 1.5%" 
                  v-for="time in possibleTimeChoices" :key="time" :value="time"
          >{{time}}</v-chip>
        </v-chip-group>
      </v-card-text>
      <v-card-actions class="is-flex is-justify-content-space-between px-4">
        <button class="button is-danger is-rounded has-text-weight-semibold is-small has-text-black"
          @click="closePopup"
          >Отмена
        </button>
        <button class="button is-primary is-rounded has-text-weight-semibold is-small has-text-black"
          @click="reserve"
          >Забронировать
        </button>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { toast } from 'bulma-toast'

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
      guestPersons: this.$store.state.search_by_number_of_persons,
      guestTime: null,
      guestTable: null,
      menu: false,
      guestDate: this.$store.state.search_by_date,
      timeChoices: ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', 
                    '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                    '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
                    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
                    '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30'],
    }
  },
  computed: {
    possibleTimeChoices() {
      let workingHours = this.restaurant_data.working_hours.split(" ")
      let freeHours = []
      for (let i = 0; i <= this.timeChoices.length; i++) {
        if (this.timeChoices[i] >= workingHours[0] && this.timeChoices[i] <= workingHours[2])
          freeHours.push(this.timeChoices[i])
      }
      return freeHours
    },
    computedDateFormatted() {
      return this.formatDate(this.guestDate)
    }
  },
  methods: {
    reserve() {
      let guestData = {'name': this.guestName, 'phone': this.guestPhone,
                       'numberOfPersons': this.guestPersons, 'date': this.guestDate,
                       'time': this.guestTime, 'table': this.guestTable,
                       'restaurant': this.restaurant_data.id}
      this.axios
          .post("/api/reserve/", guestData)
          .then(responce => {
            toast({
              message: 'Бронирование завершено!',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 3000,
              position: 'bottom-right'
            })
            this.closePopup();
          })
          .catch(error => {})
    },
    closePopup() {
      this.$emit('closePopup');
    },
    formatDate(date) {
      if (!date) return null
      const [year, month, day] = date.split('-')
      return `${day}.${month}.${year}`
    },
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
  top: 20%;
  left: 33.5%;
  background: linear-gradient(
    to right bottom,
    rgba(0,0,0, 0.9),
    rgba(0,0,0, 0.75)
  );
  border-radius: 1.5rem;
  backdrop-filter: blur(2rem);
}

.el-input-number {
  color: black;
}

@media screen {
  
}
</style>