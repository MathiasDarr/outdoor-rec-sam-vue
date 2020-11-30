<template>

</template>

<script>
/* eslint-disable */

import { mapGetters, mapActions } from "vuex";
import axios from 'axios';


export default {
    components:{

    },

    methods:{
        ...mapActions(["fetchProducts", "fetchCategories"]),
    },
    computed: {
        ...mapGetters(["allProducts", "getCategories", "getIdToken"]),
    },
    created(){
      // this.fetchCategories()
      // this.categories = this.getCategories
// this.fetchProducts();
    },

    data(){

        return {

        }
    }
}


</script>