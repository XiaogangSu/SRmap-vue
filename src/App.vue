<template>
  <div id="app">
    <div id="map"></div>
    <login id="loginid" @codeVar="getcode"></login>
    <funlogo id='logo' :logoshow="logoshow" @showVar="get_showvar"></funlogo>
    <search id="search" v-show="searchshow" ></search>
    <route id="route" :logo="routeshow"></route>
    <loc id='loc'></loc>
    <router-view />
  </div>
</template>

<script>
import mapboxgl from "mapbox-gl";
import axios from "axios";
import Login from "./views/login.vue";
import Search from "./views/search.vue";
import Route from "./views/route.vue";
import Funlogo from "./views/funlogo.vue"
import Loc from './views/loc.vue'

export default {
  name: "mapbox_test",
  components: {
    Login,
    Search,
    Route,
    Funlogo,
    Loc
  },
  data() {
    return {
      stylejson: "",
      instance: null,
      token: "",
      code: "",
      logoshow: false,
      searchshow: false,
      routeshow: false,
      showvar:""
    };
  },
  created() {},
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
        // this.GLOBAL.map.addControl(new mapboxgl.NavigationControl(), "bottom-right");
        //添加
        map.loadImage("./style/icon/begin2.png", function(error, image) {
          if (error) throw error;
          if (!map.hasImage("startimg")) map.addImage("startimg", image);
        });
        map.loadImage("./style/icon/end2.png", function(error, image) {
          if (error) throw error;
          if (!map.hasImage("endimg")) map.addImage("endimg", image);
        });
        map.loadImage("./style/icon/position.png", function(error, image) {
          if (error) throw error;
          if (!map.hasImage("positionimg")) map.addImage("positionimg", image);
        });
        map.loadImage("./style/icon/poi.png", function(error, image) {
          if (error) throw error;
          if (!map.hasImage("poiImg")) map.addImage("poiImg", image);
        });

      });
    },
    // gettoken(msg) {
    //   this.token = msg;
    //   // console.log("TOKEN:",this.token)
    // },
    getcode(msg) {
      this.code = msg;
      console.log(this.code, typeof this.code);
      if (this.code == 0) {
        // this.searchshow = true;
        // this.routeshow = true;
        this.logoshow = true;
      }
      // console.log('CODE:',this.code)
    },
    get_showvar(msg){
      this.showvar = msg
      // console.log('showvar:',msg)
      if (this.showvar==0){
        this.searchshow=true
        this.routeshow=false
      }else if(this.showvar==1){
        this.searchshow=false
        this.routeshow=true
      }
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

/* #search {
  position: absolute;
  top: 0px;
  width: 100%;
} */

/* #route {
  position: absolute;
  top: 54px;
  width: 100%;
} */
#route{
  background-color:#FFFFFF;
}
#logo{
  position: absolute;
  top:30%;
  left:5px;
}
#loc{
  position: absolute;
  bottom:3px;
  right:3px;
}
</style>