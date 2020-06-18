<template>
  <div v-show="logo">
    <van-row>
      <van-col span='12'>
        <van-search show-action placeholder="输入坐标或地名" v-model="startcor" @search="startbtn"
          background='rgba(234,236,239,1)'>
          <template #action>
            <div @click="startbtn">起点</div>
          </template>
        </van-search>
      </van-col>
      <van-col span="12">
        <van-search show-action placeholder="输入坐标或地名" v-model="endcor" @search="endbtn"
          background='rgba(234,236,239,1)'>
          <template #action>
            <div @click="endbtn">终点</div>
          </template>
        </van-search>
      </van-col>
    </van-row>

  </div>
</template>

<script>
  import Vue from "vue";
  import { Button, Field, Col, Row, Cell, Search } from "vant";
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
        startcor: null,
        endcor: '',
      }
    },
    methods: {
      startonclick (e) {
        let nowcor = e.lngLat;
        console.log('nowcor:',nowcor)
        this.startcor=nowcor.lat.toFixed(7) + ',' + nowcor.lng.toFixed(7);
        let layerids = this.GLOBAL.layerids;
        console.log(layerids);
        //检查起始点图层是否存在，若存在则删除
        for (var i = 0; i < layerids.length; i++) {
          if (layerids[i].search('startpoint') != -1) {
            map.removeLayer(layerids[i]);
            map.removeSource(layerids[i]);
          }
        }
        let startjson = {
          'type': 'FeatureCollection',
          'features': [{
            'type': 'Feature',
            'geometry': {
              'type': 'Point',
              'coordinates': [nowcor.lng, nowcor.lat]
            },
            'properties': {
              'title': 'start',
              'description': '起始点',
            }
          }]
        }
        this.GLOBAL.map.addSource('startpoint', {
          'type': "geojson",
          'data': startjson
        });

        this.GLOBAL.map.addLayer({
          'id': "startpoint",
          'type': 'symbol',
          'source': 'startpoint',
          'layout': {
            'icon-image': 'startimg',
            'icon-size': 0.2
          }
        })
        return (nowcor);
      },
      startbtn: function () {
        let map = this.GLOBAL.map
        this.GLOBAL.getlayerid(map)
        this.GLOBAL.addimg1(map)
        // console.log('ids:',this.GLOBAL.layerids)
        // map.on('click', (e)=> {
        //   this.startcor = "zzzzzzzz"
        //   let nowcor = e.lngLat;
        //   this.startcor = nowcor.lng
        //   console.log(nowcor.lng)
        // });
        map.on('click', this.startonclick)
      },
      endbtn: function () {

      }
    }
  };
</script>