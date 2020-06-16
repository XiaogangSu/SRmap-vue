import mapboxgl from "mapbox-gl";
import axios from "axios";
const loginurl = 'http://121.199.14.136:5001/auth/get_token'
const registerurl = 'http://121.199.14.136:5001/auth/register'

export default {
    loginurl: loginurl,
    registerurl: registerurl,
    map: "",
    style: "",
    setAmap(newmap) {
        this.map = newmap
    },
    // getlayer() {
    //     console.log('map:',this.map)
    //     console.log('map:',this.map.getLayer())
    //     let layers = this.map.getStyle().layers;
    //     console.log('test1')
    //     let layerid = [];
    //     for (let i = 0; i < layers.length; i++) {
    //         layerid.push(layers[i]['id']);
    //     }
    //     return (layerid);
    // }
}