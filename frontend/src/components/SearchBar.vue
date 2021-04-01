<template>
  <div class="columns est-layer">
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
          ></v-text-field>
        </template>
        <v-date-picker
          locale="ru"
          v-model="search_by_date"
          @input="menu = false"
          no-title
          scrollable
        ></v-date-picker>
      </v-menu>
    </div>
    <div class="est-time">
      <v-select
        class="mt-0 pt-1 mx-1"
        v-model="search_by_time"
        :items="timeChoices"
        prepend-inner-icon="query_builder"
        autocomplete
        @change="sendData"
      ></v-select>
    </div>
    <div class="est-person">
      <v-select
        class="mt-0 pt-1 mx-1"
        v-model="search_by_number_of_persons"
        :items="personChoices"
        prepend-inner-icon="people"
        autocomplete
        @change="sendData"
      ></v-select>
    </div>
    <div class="est-name">
      <v-text-field
        class="mt-0 pt-1 mx-1"
        v-model="search_by_name"
        label="Поиск по названию"
        prepend-inner-icon="search"
        single-line
        hide-details
        autocomplete
        @change="sendData"
      ></v-text-field>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      menu: false,
      search_by_date: new Date().toISOString().slice(0, 10),
      search_by_time: '15:00',
      search_by_number_of_persons: 2,
      search_by_name: '',
      timeChoices: ['00:00', '00:30', '01:00', '01:30', '02:00', '02:30', '03:00', '03:30', '04:00', '04:30', 
                    '05:00', '05:30', '06:00', '06:30', '07:00', '07:30', '08:00', '08:30', '09:00', '09:30',
                    '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30',
                    '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30',
                    '20:00', '20:30', '21:00', '21:30', '22:00', '22:30', '23:00', '23:30'],
      personChoices: [1,2,3,4,5,6],
    }
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.search_by_date)
    }
  },
  methods: {
    formatDate(date) {
      if (!date) return null
      const [year, month, day] = date.split('-')
      return `${day}.${month}.${year}`
    },
    sendData() {
      this.$emit('sendAllData', [this.search_by_date, this.search_by_time, this.search_by_number_of_persons, this.search_by_name])
    }
  },
};
</script>

<style scoped>
div.est-layer {
  display: flex;
  width: 710px;
  height: 39px;
  border: 2px solid #000000;
  border-radius: 4px;
}

div.est-date,
div.est-time,
div.est-person {
  width: 22%;
  border-right: 2px solid #000000;
}

div.est-name {
  width: 34%;
}
</style>