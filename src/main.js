import Vue from 'vue'
import App from './App.vue'
import Appbak from './App-pure.vue'
import router from './router'
import Globalvar from './api/glabal_var.js'
import BaiduMap from "vue-baidu-map";

Vue.config.productionTip = false
Vue.prototype.GLOBAL = Globalvar

Vue.use(BaiduMap, {
  ak: "Aqok0orEcbo2jt2vMtGZPU3KGDE9hK8O"
});

new Vue({
  router,
  // data:function(){
  //   return{
  //     map:''
  //   }
  // },
  render: h => h(App)
}).$mount('#app')
