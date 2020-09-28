<template>
  <div id="poi" v-show="logo">
    <div id="pic_container">
      <img src id="id_img1" />
      <!-- <img src="" id="id_img2"> -->
    </div>
    <div>
      <input type="file" accept="image/*" @change="changeImage()" ref="inputfiles" style="display:none" />
      <div class="pic_list_box">
        <div class="pic_list" v-show="imgDatas.length">
          <div v-for="(src,index) in imgDatas" :key="index">
            <!-- <img :src="src" width="80" height="80" alt srcset /> -->
            <!-- 利用element-ui的图片预览插件 -->
            <el-image style="width: 100px; height: 100px" :src="src" :preview-src-list="imgDatas">
            </el-image>
          </div>
        </div>
      </div>
      <img class="upload_btn" @click="upLoad" src="../../public/img_icon/upimg.png" />
    </div>

    <table id="poi_info" border="0">
      <tr>
        <th align="right" width="20px">
          <label>Name:</label>
        </th>
        <th align="left">
          <input id="poiname" type="text" v-model="poiname_val" />
        </th>
      </tr>
      <tr>
        <th align="right">
          <label>Address:</label>
        </th>
        <th align="left">
          <input id="poiaddress" type="text" v-model="address_val" />
        </th>
      </tr>
      <tr>
        <th align="right">
          <label>Type:</label>
        </th>
        <th align="left">
          <input id="poitype" type="text" v-model="type_val" />
        </th>
      </tr>
      <tr>
        <th align="right">
          <label>Phone:</label>
        </th>
        <th align="left">
          <input id="poiphone" type="text" v-model="phone_val" />
        </th>
      </tr>
      <tr>
        <th align="right">
          <button id="loc_poi" class="poi_btn" type="button" @click="locpoi">Location</button>
        </th>
        <th align="left">
          <input id="poiloc" type="text" v-model="poicor" />
        </th>
      </tr>
      <tr>
        <th align="right">
          <button type="button" id="subpoi" class="poi_btn" @click="subpoi">Finish</button>
        </th>
      </tr>
    </table>
  </div>
</template>

<script>
  import Vue from "vue";
  import ElementUI from 'element-ui';
  import 'element-ui/lib/theme-chalk/index.css';
  import axios from "axios";
  // Vue.prototype.$ajax=axios
  Vue.use(ElementUI)

  export default {
    data() {
      return {
        poicor: "",
        poiname_val: 'Navinfo',
        address_val: '北京市海淀区永丰路',
        type_val: '公司',
        phone_val: '18310870157',
        imgDatas: [],
        files
      };
    },
    props: ["logo"],
    methods: {
      changeImage() {
        console.log('上传图片测试！')
        // 上传图片事件
        var files = this.$refs.inputfiles.files;
        console.log(files)
        var that = this;
        function readAndPreview(file) {
          //Make sure `file.name` matches our extensions criteria
          if (/\.(jpe?g|png|gif)$/i.test(file.name)) {
            var reader = new FileReader();
            reader.onload = function (e) {
              if (that.imgDatas.indexOf(e.target.result) === -1) {
                that.imgDatas.push(e.target.result);
              }
            };
            reader.readAsDataURL(file);
          }
        }
        readAndPreview(files[0])
        if (files.length === 0) {
          return;
        }
        this.setUploadFile(files[0])
      },
      setUploadFile(file) {
        console.log('filetest:', file)
        let formData = new FormData()
        formData.append('file', file) // 添加到请求体

        // this.$http
        //   .post('/api/dxbase/upload?resType=EVENT', this.formData)
        //   .then(res => {
        //     console.log(res);
        //   })
        axios({
          method: 'post',
          url: this.GLOBAL.uppicurl,
          data: formData,
          headers: {
            "token": this.GLOBAL.token,
          }
        }).then(res => {
          console.log('照片上传', res)
          let redData_ob = res['data'];
          console.log(redData_ob['msg']);
          console.log(redData_ob['md5']);
          if (redData_ob.hasOwnProperty("md5")) {
            let picmd5 = redData_ob["md5"];
            console.log("picmd5:", picmd5);
            // md5list.push(picmd5);
            console.log('图片上传成功！')
          }
          else {
            alert("picture upload failed!");
          }
        })
      },
      upLoad() {
        // 触发上传图片按钮
        this.$refs.inputfiles.dispatchEvent(new MouseEvent("click"));
      },
      //选择poi点位
      locpoi_click(e) {
        var nowcor = e.lngLat;
        console.log('坐标：', nowcor)
        this.poicor = nowcor.lat.toFixed(7) + "," + nowcor.lng.toFixed(7);
        let layerids = this.GLOBAL.getlayerid(this.GLOBAL.map);
        // console.log(layerids);
        //检查poi点图层是否存在，若存在则删除
        for (var i = 0; i < layerids.length; i++) {
          if (layerids[i].search("poipoint") != -1) {
            this.GLOBAL.map.removeLayer(layerids[i]);
            this.GLOBAL.map.removeSource(layerids[i]);
          }
        }
        var poijson = {
          type: "FeatureCollection",
          features: [
            {
              type: "Feature",
              geometry: {
                type: "Point",
                coordinates: [nowcor.lng, nowcor.lat]
              },
              properties: {
                title: "poi",
                description: "poi点"
              }
            }
          ]
        };
        // source,layer用一个id名称，以便移除方便
        this.GLOBAL.map.addSource("poipoint", {
          type: "geojson",
          data: poijson
        });
        this.GLOBAL.map.addLayer({
          id: "poipoint",
          type: "symbol",
          source: "poipoint",
          layout: {
            "icon-image": "poiImg",
            "icon-size": 0.2
          }
        });
        document.getElementById("poi").style.display = "block";
        return nowcor;
      },
      locpoi: function () {
        let map = this.GLOBAL.map;
        document.getElementById("poi").style.display = "none";
        console.log("获取poi点坐标！");
        // map.off("click", endonclick);
        // map.off("click", startonclick);
        map.on("click", this.locpoi_click);
      },
      subpoi: function () {
        console.log('sub poi info!');
        console.log("token:", this.GLOBAL.token);
        let name = this.poiname_val;
        let type = this.type_val;
        let address = this.address_val;
        let phone = this.phone_val;
        let loc = this.poicor;   //string
        let cor = new Array();
        cor[0] = parseFloat(loc.split(",")[1]);
        cor[1] = parseFloat(loc.split(",")[0]);
        let poigj = { "type": "Point", "coordinates": cor }
        if (photo == '' || name == '' || type == '' || loc == '') {
          alert("Missing poi information!")
        }
        else {
          let formData = new FormData();
          // let file = $("#take_photo")[0].files[0];
          formData.append("file", file);
          let md5list = new Array();
        }
      }
    }
  };
</script>

<style scoped>
  #poi {
    width: 100%;
    height: 600px;
    background: rgb(134, 176, 237, 0.6);
  }

  .pic_list_box {
    display: flex;
  }

  .upload_btn {
    width: 50px;
    height: 50px;
    padding-left: 15px;
  }

  .pic_list {
    display: flex;
  }

  #id_img1 {
    width: 30%;
    margin: 5px;
    display: none;
  }

  #poi_info {
    position: absolute;
    left: 50px;
    border-spacing: 5px 5px;
    width: 350px;
    height: 50px;
  }

  #poi_info label {
    font-size: 18px;
    width: 100%;
  }

  #poi_info input {
    font-size: 20px;
    width: 100%;
    border-radius: 3px;
  }

  .poi_btn {
    line-height: 25px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
  }

  .poi_btn:hover {
    /* color: #444; */
    /* background: rgba(180, 27, 27, 0.315); */
    background-color: #ccc;
    /* border-color: #ccc; */
    /* text-decoration: none */
  }
</style>