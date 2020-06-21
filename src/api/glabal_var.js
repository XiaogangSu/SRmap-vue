import mapboxgl from "mapbox-gl";
import axios from "axios";
const loginurl = 'http://121.199.14.136:5001/auth/get_token'
const registerurl = 'http://121.199.14.136:5001/auth/register'

export default {
    loginurl: loginurl,
    registerurl: registerurl,
    map: "",
    style: "",
    token:"",
    logincode:"",
    searchshow:false,
    routeshow:"",
    setAmap(newmap) {
        this.map = newmap
    },
    getlayerid(map) {
        // console.log('map:',this.map)
        let layers = map.getStyle().layers;
        let layersid = []
        // console.log("layers:", this.layers);
        for (let i = 0; i < layers.length; i++) {
            layersid.push(layers[i]['id']);
        }
        // console.log("layersid:",layersid)
        return(layersid)
    },
    addimg1(map) {
        map.loadImage('./style/icon/begin2.png', function (error, image) {
            if (error) throw error;
            if (!map.hasImage('startimg')) map.addImage('startimg', image);
        })
    },
    addimg2(map) {
        map.loadImage('./style/icon/begin2.png', function (error, image) {
            if (error) throw error;
            if (!map.hasImage('startimg')) map.addImage('startimg', image);
        })
    }
}