import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home.vue'
import About from '../components/About.vue'
import LogIn from '../components/LogIn.vue'
import RestaurantList from '../components/RestaurantList.vue'
import RestaurantDetails from '../components/RestaurantDetails.vue'
import ReservationHistory from '../components/ReservationHistory.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogIn
    },
    {
      path: '/history',
      name: 'History',
      component: ReservationHistory
    },
    {
      path: '/places',
      name: 'RestaurantList',
      component: RestaurantList
    },
    {
      path: '/places/:id',
      name: 'RestaurantPage',
      component: RestaurantDetails,
      props: true
    },
  ]
})