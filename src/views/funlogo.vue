<template>
  <div>
    <table id="fun" border="0px" v-show="logoshow">
      <tr>
        <th>
          <button id="searchbtn" type="button" v-on:click="showsearch()"></button>
        </th>
      </tr>
      <tr>
        <th>
          <button id="routebtn" type="button" v-on:click="showroute()"></button>
        </th>
      </tr>
      <tr>
        <th>
          <button id="addpoi" type="button" v-on:click="addpoi()"></button>
        </th>
      </tr>
    </table>
  </div>
</template>

<script>
import Vue from "vue";
export default {
  data(){
    return{
      show_var:""
    }
  },
  props:["logoshow"],
  methods: {
    showsearch:function () {
      this.show_var = 0
      this.$emit('showVar', this.show_var)
    },
    showroute:function () {
      this.show_var = 1
      this.$emit('showVar', this.show_var)
    },
    addpoi:function () {
      this.show_var = 2
      this.$emit('showVar', this.show_var)
    }
  },
};
</script>

<style scoped>
#searchbtn {
  background: url("../../public/style/icon/search1.png") no-repeat;
}
#routebtn {
  background: url("../../public/style/icon/route1.png") no-repeat;
}
#addpoi{
  background: url("../../public/style/icon/poi2.png") no-repeat;
}
#fun button {
  width: 30px;
  height: 30px;
  background-size: 70%;
  background-position: center;
  background-color: #07c160;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}
#searchbtn:hover {
    /* background: #eee; */
    background-color: rgb(75, 88, 206);
}
#routebtn:hover {
    /* background: #eee; */
    background-color: rgb(75, 88, 206);
}
#addpoi:hover {
    /* background: #eee; */
    background-color: rgb(75, 88, 206);
}
</style>