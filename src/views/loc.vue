<template>
  <div>
    <button id="position_b" type="button" v-on:click="getposition_b()"></button>
  </div>
</template>

<script>
// import BaiduMap from "vue-baidu-map";
import Vue from "vue";
import { gcj02towgs84, bd09togcj02 } from "../api/cor_bias.js";

// Vue.use(BaiduMap, {
//   ak: "Aqok0orEcbo2jt2vMtGZPU3KGDE9hK8O"
// });

export default {
  methods: {
    getposition_b: function() {
      let geolocation = new BMap.Geolocation({
        maximumAge: 10
      });
      geolocation.enableSDKLocation();
      let layerids = this.GLOBAL.getlayerid(this.GLOBAL.map);
      for (let i = 0; i < layerids.length; i++) {
        if (layerids[i].search("Bpospoint") == 0) {
          this.GLOBAL.map.removeLayer(layerids[i]);
          this.GLOBAL.map.removeSource(layerids[i]);
        }
      }
      geolocation.getCurrentPosition(r => {
        let lon_bd09 = r.point.lng;
        let lat_bd09 = r.point.lat;
        console.log("百度定位坐标：" + r.point.lng + "," + r.point.lat);
        let gc02_cor = bd09togcj02(lon_bd09, lat_bd09);
        let wgs84_cor = gcj02towgs84(gc02_cor[0], gc02_cor[1]);
        let lon = wgs84_cor[0];
        let lat = wgs84_cor[1];
        this.GLOBAL.map.flyTo({
          center: [lon, lat],
          zoom: 15
        });
        let posjson = {
          type: "FeatureCollection",
          features: [
            {
              type: "Feature",
              geometry: {
                type: "Point",
                coordinates: [lon, lat]
              }
            }
          ]
        };
        this.GLOBAL.map.addSource("Bpospoint", {
          type: "geojson",
          data: posjson
        });
        this.GLOBAL.map.addLayer({
          id: "Bpospoint",
          type: "symbol",
          source: "Bpospoint",
          layout: {
            "icon-image": "positionimg",
            "icon-size": 0.2
          }
        });
      });
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