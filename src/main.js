import Vue from 'vue'
import App from './App.vue'
import Appbak from './App-pure.vue'
import router from './router'
import Globalvar from './api/glabal_var.js'

Vue.config.productionTip = false
Vue.prototype.GLOBAL = Globalvar


new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
