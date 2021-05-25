import './assets/reset.css';
import 'element-ui/lib/theme-chalk/index.css';
import 'material-design-icons-iconfont/dist/material-design-icons.css'

import Vue from 'vue'
import App from './App.vue'

import ElementUI from 'element-ui';
import vuetify from './plugins/vuetify';
import VueAgile from 'vue-agile'

import VueMask from 'v-mask';
// import VueExpandableImage from 'vue-expandable-image'

import axios from 'axios'
import VueAxios from 'vue-axios'

import store from './store'
import router from './router'

Vue.config.productionTip = false

Vue.use(VueAxios, axios)
Vue.use(ElementUI)
Vue.use(VueAgile)
Vue.use(VueMask);
// Vue.use(VueExpandableImage)

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
