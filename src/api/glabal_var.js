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
}