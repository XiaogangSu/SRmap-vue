<template>
  <div class="main" v-show="isshow">
    <!-- <van-nav-bar title="用户登录" /> -->
    <van-row type="flex" justify="center" class="line">
      <van-col span="3">&nbsp</van-col>
      <van-col span="18">
        <van-cell-group>
          <van-field placeholder="请输入用户名" type="text" v-model="user" left-icon="manager" />
        </van-cell-group>
        <van-cell-group>
          <van-field placeholder="请输入密码" type="password" v-model="password" left-icon="lock" />
        </van-cell-group>
      </van-col>
      <van-col span="3">&nbsp</van-col>
    </van-row>

    <van-row type="flex" justify="center" class="btns">
      <van-col span="3">&nbsp</van-col>
      <van-col span="18">
        <van-button class="jumpBtn" type="primary" @click="signIn" size="large">登录</van-button>
      </van-col>
      <van-col span="3">&nbsp</van-col>
    </van-row>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios"
import { Button, NavBar,Field, Col, CellGroup,Row } from "vant";

// Vue.use(Button)
// Vue.use(Vant)

export default {
  components: {
    [Button.name]: Button,
    [NavBar.name]: NavBar,
    [Field.name]: Field,
    [Col.name]:Col,
    [Row.name]:Row,
    [CellGroup.name]:CellGroup
  },
  data(){
    return{
      user:'liujishu002',
      password:'123456',
      isshow:'true'
    }
  },
  methods:{
    signIn:function () {
      // console.log('global var:',this.GLOBAL.token);
      console.log(this.user,this.password)
      let data={
        username:this.user,
        password:this.password
      }
      console.log(data);
      axios({
        method:'get',
        url:this.GLOBAL.loginurl,
        params:data
      }).then(res=>{
        console.log(res.data)
        // console.log(typeof(res.data))
        let code = res.data.code
        console.log('code:',code)
        let token = res.data.token
        this.$emit('tokenVar', token)
        this.$emit('codeVar',code)
        console.log('token:',token)
        if (code=='0'){
          this.isshow=false
        }
      })
      // if (this.user=="liujishu" && this.password=="123456"){
      //   this.isshow=false
      // }
    }
  }
};
</script>

<style scoped>
</style>

