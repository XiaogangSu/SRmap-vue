import mapboxgl from "mapbox-gl";
import axios from "axios";
const loginurl = 'http://121.199.14.136:5001/auth/get_token'
const registerurl = 'http://121.199.14.136:5001/auth/register'

export default {
    loginurl: loginurl,
    registerurl: registerurl,
    map: "",
    style: "",
    layerid: [],
    setAmap(newmap) {
        this.map = newmap
    },
    getlayerid(map) {
        // console.log('map:',this.map)
        console.log('test')
        map.on("load", () => {
            let layers = map.getStyle().layers;
            console.log("layers:", layers);
            // let layerid = [];
            for (let i = 0; i < layers.length; i++) {
                this.layerid.push(layers[i]['id']);
            }
        });
    },
    addimg1(map) {
        map.loadImage('./style/icon/begin2.png', function (error, image) {
            if (error) throw error;
            if (!map.hasImage('startimg')) map.addImage('startimg', image);
        })
    }
}