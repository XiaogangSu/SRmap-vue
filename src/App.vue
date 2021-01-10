<template>
  <div id="app">
    <div id="map"></div>
    <!-- <input id="layernumshow" v-model="layernum" /> -->
    <!-- <input id="layernumshow" v-model="layernum" /> -->
    <div id='layernumshow'>Z:12</div>

    <login id="loginid" @codeVar="getcode"></login>
    <funlogo id='logo' :logoshow="logoshow" @showVar="get_showvar"></funlogo>
    <search id="search" :logo="searchshow"></search>
    <route id="route" :logo="routeshow"></route>
    <!-- <poi id="poi" :logo="poishow"></poi> -->
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
  import Poi from './views/poi.vue'
  import Vue from "vue";


  export default {
    name: "mapbox_test",
    components: {
      Login,
      Search,
      Route,
      Funlogo,
      Loc,
      Poi
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
        poishow: false,
        showvar: "",
        layernum: 12
      };
    },
    created() { },
    mounted() {
      this.loadmap();
      // console.log(3);
    },
    methods: {
      loadmap() {
        let url = "/style/style_SRmap-yn.json";
        // let url = "/style/osmstyle.json";
        mapboxgl.accessToken =
          "pk.eyJ1IjoieGdhciIsImEiOiJjajh0dmpmenAwdGhqMndwMHo5ZDZua2E0In0.9CB46jBTn_gALav67l74yw";
        this.instance = axios.create({
          baseUrl: "http://localhost:8080/",
          timeout: "5000"
        });
        this.instance.get(url).then(res => {
          this.GLOBAL.style = res.data;
          console.log("style:", this.GLOBAL.style);
          let map = new mapboxgl.Map({
            container: "map",
            // style: "mapbox://styles/mapbox/streets-v9",
            style: this.GLOBAL.style,
            // style: stylejson,
            // center: [105.04713,23.09181], // 设置地图中心
            center: [116.26261,40.05378],
            zoom: 12 // 设置地图比例
          });
          // console.log('map:',map)
          // a=map.getStyle().layers
          // console.log('a:',a)
          // this.$root.map = map
          map.on("wheel", function () {
            // console.log("A wheel event occurred.");
            // let range = map.getZoom();
            // this.layernum = range;
            // console.log(this.layernum);
            let zoomlevel = map.getZoom().toFixed(1);
            document.getElementById('layernumshow').innerHTML = 'L:' + zoomlevel;
          });
          console.log("version:", map.version);
          this.GLOBAL.setAmap(map);
          // this.GLOBAL.map.addControl(new mapboxgl.NavigationControl(), "bottom-right");
          //添加
          map.loadImage("./style/icon/begin2.png", function (error, image) {
            if (error) throw error;
            if (!map.hasImage("startimg")) map.addImage("startimg", image);
          });
          map.loadImage("./style/icon/end2.png", function (error, image) {
            if (error) throw error;
            if (!map.hasImage("endimg")) map.addImage("endimg", image);
          });
          map.loadImage("./style/icon/position.png", function (error, image) {
            if (error) throw error;
            if (!map.hasImage("positionimg")) map.addImage("positionimg", image);
          });
          map.loadImage("./style/icon/poi.png", function (error, image) {
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
          this.searchshow = true;
          this.routeshow = false;
          this.logoshow = true;
        }
        // console.log('CODE:',this.code)
      },
      get_showvar(msg) {
        this.showvar = msg
        // console.log('showvar:',msg)
        if (this.showvar == 0) {
          this.searchshow = true
          this.routeshow = false
          this.poishow = false
        } else if (this.showvar == 1) {
          this.searchshow = false
          this.routeshow = true
          this.poishow = false
        } else if (this.showvar == 2) {
          this.searchshow = false
          this.routeshow = false
          this.poishow = true
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

  #layernumshow {
    position: absolute;
    width: 50px;
    height: 20px;
    left:0px;
    bottom:5px;
    font-weight: bolder;
    z-index: 2;
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
  #route {
    background-color: #FFFFFF;
  }

  #logo {
    position: absolute;
    top: 30%;
    left: 5px;
  }

  #loc {
    position: absolute;
    bottom: 3px;
    right: 3px;
  }
</style>