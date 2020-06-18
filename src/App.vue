<template>
  <div id="app">
    <div id="map"></div>
    <login id="loginid" @tokenVar="gettoken" @codeVar="getcode"></login>
    <search id="search" :logo="searchshow"></search>
    <route id="route" :logo="routeshow"></route>
    <router-view />
  </div>
</template>

<script>
import mapboxgl from "mapbox-gl";
import axios from "axios";
import Login from "./views/login.vue";
import Search from "./views/search.vue";
import Route from "./views/route.vue";
export default {
  name: "mapbox_test",
  components: {
    Login,
    Search,
    Route
  },
  data() {
    return {
      stylejson: "",
      instance: null,
      token: "",
      code: "",
      searchshow: false,
      routeshow: false
    };
  },
  created() {},
  mounted() {
    this.loadmap();
    // console.log(3);
  },
  methods: {
    loadmap() {
      let url = "/style/style.json";
      mapboxgl.accessToken =
        "pk.eyJ1IjoieGdhciIsImEiOiJjajh0dmpmenAwdGhqMndwMHo5ZDZua2E0In0.9CB46jBTn_gALav67l74yw";
      this.instance = axios.create({
        baseUrl: "http://localhost:8080/",
        timeout: "1000"
      });
      this.instance.get(url).then(res => {
        this.GLOBAL.style = res.data;
        console.log("style:", this.GLOBAL.style);
        let map = new mapboxgl.Map({
          container: "map",
          // style: "mapbox://styles/mapbox/streets-v9",
          style: this.GLOBAL.style,
          // style: stylejson,
          center: [116.36511, 39.93896], // 设置地图中心
          zoom: 12 // 设置地图比例
        });
        // console.log('map:',map)
        // a=map.getStyle().layers
        // console.log('a:',a)
        // this.$root.map = map
        console.log("version:", map.version);
        this.GLOBAL.setAmap(map);
        // this.GLOBAL.getlayerid(map);
        // console.log('id:',this.GLOBAL.layerid)
        // map.on("load", () => {
        //   let a = map.getStyle().layers;
        //   console.log("a=", a);
        // });

        // this.GLOBAL.getlayer()
      });
    },
    gettoken(msg) {
      this.token = msg;
      // console.log("TOKEN:",this.token)
    },
    getcode(msg) {
      this.code = msg;
      console.log(this.code, typeof this.code);
      if (this.code == 0) {
        this.searchshow = true;
        this.routeshow = true;
      }
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

#search {
  position: absolute;
  top: 0px;
  width: 100%;
}

#route {
  position: absolute;
  top: 54px;
  width: 100%;
}
</style>