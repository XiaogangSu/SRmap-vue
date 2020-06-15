<template>
  <div v-show="logo">
    <van-row>
      <van-col span='12'>
        <van-search show-action placeholder="输入坐标或地名" v-model="startcor" @search="startbtn" background='rgba(234,236,239,1)'>
          <template #action>
            <div @click="startbtn">起点</div>
          </template>
        </van-search>
      </van-col>
      <van-col span="12">
        <van-search show-action placeholder="输入坐标或地名" v-model="endcor" @search="endbtn" background='rgba(234,236,239,1)'>
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
    data(){
      return{
        startcor:'',
        endcor:'',
      }
    },
    methods:{
      startbtn: function(){
        let map = this.GLOBAL.map
        map.on('click', function(e) {   
            console.log('我的被点击了')           
        });
        let startcor = this.startcor
      },
      endbtn: function(){
        
      }
    }
  };
</script>