<template>
  <div id="app">
    <div id = "map" v-show="mapshow"></div>
    <login id="loginid" @tokenVar="gettoken" @codeVar="getcode"></login>
    
    <router-view/>
  </div>
</template>

<script>
import mapboxgl from "mapbox-gl";
import axios from "axios";
import Login from "./views/login.vue"
export default {
  name: "mapbox_test",
  components:{
    Login
  },
  data() {
    return {
      stylejson: "",
      instance: null,
      mapshow:true,
      token:'',
      code:''
    };
  },
  created() {
    console.log("1");
    this.instance = axios.create({
      baseUrl: "http://localhost:8080/",
      timeout: "1000"
    });
    this.instance.get("./style/style_SRmap.json").then(res => {
      this.stylejson = res.data;
      console.log("2");
    });
  },
  mounted() {
    this.loadmap();
    console.log(3);
  },
  methods: {
    loadmap() {
      // var url = "/style/style_SRmap.json";
      mapboxgl.accessToken =
        "pk.eyJ1IjoieGdhciIsImEiOiJjajh0dmpmenAwdGhqMndwMHo5ZDZua2E0In0.9CB46jBTn_gALav67l74yw";
      const map = new mapboxgl.Map({
        container: "map",
        style: "mapbox://styles/mapbox/streets-v9",
        // style: res["data"],
        // style: '/style/style_SRmap.json',
        center: [116.36511, 39.93896], // 设置地图中心
        zoom: 12 // 设置地图比例
      });
    },
    gettoken(msg){
      this.token=msg
      // console.log("TOKEN:",this.token)
    },
    getcode(msg){
      this.code=msg
      // console.log('CODE:',this.code)
    }
  }
};
</script>

<style>
#map {
  position: absolute;
  left: 0;
  top: 0;
  text-align: left;
  width: 100%;
  height: 100%;
  z-index: -1;
}

</style>
