<template>
  <van-search show-action label="地址" placeholder="请输入搜索关键词" @search="onSearch">
    <template #action>
      <div @click="onSearch">搜索</div>
    </template>
  </van-search>
</template>

<script>
import Vue from "vue";
import { Search } from "vant";
export default {
  components: {
    [Search.name]: Search
  },
  data(){
      return{

      }
  },
  methods:{
      onSearch:function(){
          console.log('test')
      }
  }
};
</script>