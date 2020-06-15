import Vue from 'vue'
import App from './App.vue'
import Appbak from './App-pure.vue'
import router from './router'
import Globalvar from './api/glabal_var.js'

Vue.config.productionTip = false
Vue.prototype.GLOBAL = Globalvar

new Vue({
  router,
  // data:function(){
  //   return{
  //     map:''
  //   }
  // },
  render: h => h(App)
}).$mount('#app')
