<template>
  <div class="main">
    <!-- <van-nav-bar title="用户登录" /> -->
    <div v-show="isshow">
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
        <van-col span="9">
          <van-button class="jumpBtn" type="primary" @click="signIn" size="small">登录</van-button>
        </van-col>
        <van-col span="9">
          <van-button class="jumpBtn" type="primary" @click="signOn" size="small">注册</van-button>
        </van-col>
        <van-col span="3">&nbsp</van-col>
      </van-row>
    </div>
    <!-- <van-popup v-model="popup_isshow">{{msg}}</van-popup> -->
  </div>
</template>

<script>
  import Vue from "vue";
  import axios from "axios"
  import { Button, Field, Col, CellGroup, Row, Dialog } from "vant";

  // Vue.use(Button)
  // Vue.use(Vant)

  export default {
    components: {
      [Button.name]: Button,
      [Field.name]: Field,
      [Col.name]: Col,
      [Row.name]: Row,
      [CellGroup.name]: CellGroup,
      [Dialog.name]: Dialog,
      // [Popup.name]: Popup
    },
    data() {
      return {
        user: 'liujishu002',
        password: '123456',
        isshow: true,
        // popup_isshow: false,
        // popup_noshow: false,
        // login_noshow: false,
        // msg: ''
      }
    },
    methods: {
      signIn: function () {
        // console.log('global var:',this.GLOBAL.token);
        console.log(this.user, this.password)
        let data = {
          username: this.user,
          password: this.password
        }
        console.log(data);
        axios({
          method: 'get',
          url: this.GLOBAL.loginurl,
          params: data
        }).then(res => {
          console.log(res.data)
          // console.log(typeof(res.data))
          let code = res.data.code
          // console.log('code:', code)
          let token = res.data.token
          this.GLOBAL.token = token
          // this.GLOBAL.logincode = code
          this.$emit('tokenVar', token)
          this.$emit('codeVar', code)
          console.log('token:', token)
          if (code == '0') {
            this.isshow = false
          } else {
            // this.popup_isshow = true
            this.msg = '登陆失败！'
            Dialog.alert({
              title: '登录提示',
              message: '登录失败！',
            }).then(() => {
              // on close
            });
          }
        })
      },
      signOn: function () {
        //register 函数
        console.log('注册！')
        let data = {
          username: this.user,
          password: this.password
        }
        axios({
          method: 'get',
          url: this.GLOBAL.registerurl,
          params: data
        }).then(res => {
          let code = res.data.code
          if (code == '0') {
            // this.popup_isshow = true
            Dialog.alert({
              title: '注册提示',
              message: '注册成功',
            }).then(() => {
              // on close
            });
          } else {
            Dialog.alert({
              title: '注册提示',
              message: '注册失败',
            }).then(() => {
              // on close
            });
          }
        })
      }
    }
  };
</script>

<style scoped>
</style>