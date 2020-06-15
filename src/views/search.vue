<template>
  <div v-show="logo">
    <van-search show-action label="地址" placeholder="请输入搜索关键词" v-model="searchvalue" background='rgba(74,144,226,0.7)'  @search="onSearch">
      <template #action>
        <div @click="onSearch">搜索</div>
      </template>
    </van-search>
  </div>
</template>

<script>
import Vue from "vue";
import { Search } from "vant";
export default {
  components: {
    [Search.name]: Search
  },
  data() {
    return {
        searchvalue:''
    };
  },
  props: ["logo"],
  methods: {
    onSearch: function() {
      console.log(this.searchvalue);
      console.log('show:',this.logo)
    }
  }
};
</script>