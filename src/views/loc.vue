<template>
  <div>
    <button id="position_b" type="button" v-on:click="getposition_b()"></button>
  </div>
</template>

<script>
// import BaiduMap from "vue-baidu-map";
import Vue from "vue";
// Vue.use(BaiduMap, {
//   ak: "Aqok0orEcbo2jt2vMtGZPU3KGDE9hK8O"
// });

export default {
  methods: {
    getposition_b: function() {
      console.log("定位测试！");
      let geolocation = new BMap.Geolocation({
        maximumAge: 10
      });
      geolocation.enableSDKLocation();
    }
  }
};
</script>

<style scoped>
#position_b {
  width: 30px;
  height: 30px;
  background: url("../../public/style/icon/pos3.png") no-repeat;
  background-size: 100%;
  background-color: rgb(255, 255, 255);
  border-style: none;
  border-radius: 4px;
  border: none;
  text-align: center;
  line-height: 32px;
  cursor: pointer;
}
</style>