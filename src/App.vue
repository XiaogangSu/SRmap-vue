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
  import Route from "./views/route.vue"
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
      // console.log(3);
    },
    methods: {
      loadmap() {
        let url = "/style/style_SRmap.json";
        mapboxgl.accessToken =
          "pk.eyJ1IjoieGdhciIsImEiOiJjajh0dmpmenAwdGhqMndwMHo5ZDZua2E0In0.9CB46jBTn_gALav67l74yw";
        this.instance = axios.create({
          baseUrl: "http://localhost:8080/",
          timeout: "1000"
        });
        this.instance.get("./style/style_SRmap.json").then(res => {
          this.GLOBAL.style = res.data;
          console.log('style:', this.GLOBAL.style)
          let map = new mapboxgl.Map({
            container: "map",
            style: "mapbox://styles/mapbox/streets-v9",
            // style: this.GLOBAL.style,
            // style: stylejson,
            center: [116.36511, 39.93896], // 设置地图中心
            zoom: 12 // 设置地图比例
          });
          console.log('map:',map)
          a=map.getStyle().layers
          console.log('a:',a)
          // this.$root.map = map
          // this.GLOBAL.setAmap(map);
          // console.log(this.GLOBAL.getlayer())
        });
      },
      gettoken(msg) {
        this.token = msg;
        // console.log("TOKEN:",this.token)
      },
      getcode(msg) {
        this.code = msg;
        console.log(this.code, typeof (this.code))
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