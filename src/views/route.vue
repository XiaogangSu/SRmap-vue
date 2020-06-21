<template>
  <div v-show="logo">
    <van-row type="flex" align="center">
      <van-col span="18">
        <van-field id='start' v-model="startcor" placeholder="输入起点坐标或地名" left-icon="location-o" background='rgba(74,144,226,0.7)'>
          <template #button>
            <van-button size="small" type="primary" @click="startbtn">地图选点</van-button>
          </template>
        </van-field>
      </van-col>
      <van-col span="6" type="flex" justify="center">
        <van-button size="small" type="primary" @click="startbtn">起终点互换</van-button>
      </van-col>
    </van-row>

    <van-row type="flex" align="center">
      <van-col span="18">
        <van-field v-model="endcor" placeholder="输入终点坐标或地名" left-icon="location-o">
          <template #button>
            <van-button size="small" type="primary" @click="endbtn">地图选点</van-button>
          </template>
        </van-field>
      </van-col>
      <van-col span="6">
        <van-button size="small" type="primary" @click="routepath">路径规划</van-button>
      </van-col>
    </van-row>
  </div>
</template>

<script>
import Vue from "vue";
import { Button, Field, Col, Row, Cell, Search } from "vant";
import axios from "axios";
import { gcj02towgs84 } from "../api/cor_bias.js";

export default {
  components: {
    [Button.name]: Button,
    [Field.name]: Field,
    [Col.name]: Col,
    [Row.name]: Row,
    [Cell.name]: Cell,
    [Search.name]: Search
    // [Popup.name]: Popup
  },
  props: ["logo"],
  data() {
    return {
      startcor: "",
      endcor: "",
      routecor: ""
    };
  },
  methods: {
    startonclick(e) {
      let nowcor = e.lngLat;
      console.log("nowcor:", nowcor);
      this.startcor = nowcor.lat.toFixed(7) + "," + nowcor.lng.toFixed(7);
      let layerids = this.GLOBAL.getlayerid(this.GLOBAL.map);
      // let layerids = this.GLOBAL.layerid;
      // console.log("layers id:", layerids);
      //检查起始点图层是否存在，若存在则删除
      for (let i = 0; i < layerids.length; i++) {
        if (layerids[i].search("startpoint") != -1) {
          this.GLOBAL.map.removeLayer(layerids[i]);
          this.GLOBAL.map.removeSource(layerids[i]);
        }
      }
      let startjson = {
        type: "FeatureCollection",
        features: [
          {
            type: "Feature",
            geometry: {
              type: "Point",
              coordinates: [nowcor.lng, nowcor.lat]
            },
            properties: {
              title: "start",
              description: "起始点"
            }
          }
        ]
      };
      this.GLOBAL.map.addSource("startpoint", {
        type: "geojson",
        data: startjson
      });

      this.GLOBAL.map.addLayer({
        id: "startpoint",
        type: "symbol",
        source: "startpoint",
        layout: {
          "icon-image": "startimg",
          "icon-size": 0.2
        }
      });
      return nowcor;
    },
    endonclick(e) {
      let nowcor = e.lngLat;
      this.endcor = nowcor.lat.toFixed(7) + "," + nowcor.lng.toFixed(7);
      let layerids = this.GLOBAL.getlayerid(this.GLOBAL.map);
      // console.log("layers id:", layerids);
      //检查起始点图层是否存在，若存在则删除
      for (var i = 0; i < layerids.length; i++) {
        if (layerids[i].search("endpoint") != -1) {
          this.GLOBAL.map.removeLayer(layerids[i]);
          this.GLOBAL.map.removeSource(layerids[i]);
        }
      }
      var endjson = {
        type: "FeatureCollection",
        features: [
          {
            type: "Feature",
            geometry: {
              type: "Point",
              coordinates: [nowcor.lng, nowcor.lat]
            },
            properties: {
              title: "end",
              description: "终点"
            }
          }
        ]
      };
      this.GLOBAL.map.addSource("endpoint", {
        type: "geojson",
        data: endjson
      });
      this.GLOBAL.map.addLayer({
        id: "endpoint",
        type: "symbol",
        source: "endpoint",
        layout: {
          "icon-image": "endimg",
          "icon-size": 0.2
        }
      });
      return nowcor;
    },
    startbtn: function() {
      let map = this.GLOBAL.map;
      map.on("click", this.startonclick);
      map.off("click", this.endonclick);
    },
    endbtn: function() {
      let map = this.GLOBAL.map;
      map.on("click", this.endonclick);
      map.off("click", this.startonclick);
    },
    routepath: function() {
      console.log("路径规划！");
      // console.log('token:',this.GLOBAL.token)
      this.GLOBAL.map.off("click", this.startonclick);
      this.GLOBAL.map.off("click", this.endonclick);
      let url1 = "http://121.199.14.136:8989/route?point=";
      let url2 =
        "&type=json&locale=zh-CN&vehicle=car&weighting=fastest&points_encoded=false";
      let startcor = this.startcor;
      let endcor = this.endcor;
      let url = url1 + startcor + "&point=" + endcor + url2;
      axios({
        method: "get",
        url: url
      }).then(res => {
        console.log("urlback:", res);
        let urlbackcor = res.data.paths[0]["points"]["coordinates"];
        let polylinecor = [];
        for (let i = 0; i < urlbackcor.length; i++) {
          // let tempcor = wgs84togcj02(reqdata[i][0], reqdata[i][1]);  //坐标加密
          let tempcor = gcj02towgs84(urlbackcor[i][0], urlbackcor[i][1]);
          polylinecor.push([tempcor[0], tempcor[1]]);
        }
        // corbias.gcj02towgs84()
        let routelayerid = this.GLOBAL.token + "_route";
        // 判断是否存在某一图层，若存在则删除
        let layerids = this.GLOBAL.getlayerid(this.GLOBAL.map);
        // console.log(layerids);
        for (let i = 0; i < layerids.length; i++) {
          if (layerids[i].search(routelayerid) != -1) {
            this.GLOBAL.map.removeLayer(layerids[i]);
            this.GLOBAL.map.removeSource(layerids[i]);
          }
        }

        this.GLOBAL.map.addLayer({
          id: routelayerid,
          type: "line",
          source: {
            type: "geojson",
            data: {
              type: "Feature",
              properties: {},
              geometry: {
                type: "LineString",
                coordinates: polylinecor
              }
            }
          },
          layout: {
            "line-join": "round",
            "line-cap": "round"
          },
          paint: {
            "line-color": "rgba(255, 106, 106, 0.6)",
            "line-width": 5
          }
        });
      });
      // console.log("url:", this.urlback(url))

      // var urlbackcor = urlback(url);
      // var userid = 'sxg_';
      // var nowtime = getnowtime();
      // var sub = 'route';
      // // console.log(urlbackcor);
    }
  }
};
</script>

<style scoped>
#start{
  background-color: #272822;
}
</style>>