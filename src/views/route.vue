<template>

    
</template>

<script>
import Vue from "vue";
import { Button, Field, Col, Row} from "vant";
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
}
</script>