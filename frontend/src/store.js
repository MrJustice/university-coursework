import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const store = new Vuex.Store({
  // state: {
  //   search_by_date: false,
  //   search_by_time: '15:00',
  //   search_by_number_of_persons: 2,
  //   search_by_name: '',
  // },
  // mutations: {
  //   CHANGE_DATE: (state, value) => {
  //     state.search_by_date = value
  //   },
  //   CHANGE_TIME: (state, value) => {
  //     state.search_by_time = value
  //   },
  //   CHANGE_NUMBER_OF_SEATS: (state, value) => {
  //     state.search_by_number_of_persons = value
  //   },
  //   CHANGE_NAME: (state, value) => {
  //     state.search_by_name = value
  //   },
  // },
  // actions: {
  //   TOOGLE_DATE({commit}) {
  //     commit('CHANGE_DATE', value)
  //   },
  //   TOOGLE_TIME({commit}) {
  //     commit('CHANGE_TIME', value)
  //   },
  //   TOOGLE_NOP({commit}) {
  //     commit('CHANGE_NUMBER_OF_SEATS', value)
  //   },
  //   TOOGLE_NAME({commit}) {
  //     commit('CHANGE_NAME', value)
  //   },
  // },
  // getters: {
  //   GET_SEARCH_BY_DATE(state) {
  //     return state.search_by_date
  //   },
  //   GET_SEARCH_BY_TIME(state) {
  //     return state.search_by_time
  //   },
  //   GET_SEARCH_BY_NUMBER_OF_PERSONS(state) {
  //     return state.search_by_number_of_persons
  //   },
  //   GET_SEARCH_BY_NAME(state) {
  //     return state.search_by_name
  //   },
  // }
});

export default store;