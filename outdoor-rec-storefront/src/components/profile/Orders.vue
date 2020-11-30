<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <!-- <BaseNavBar v-bind:categories=cate /> -->
            hello
      </v-flex>
      <v-flex md9>
            dfdf
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

import { mapGetters, mapActions } from "vuex";
import axios from 'axios';


export default {
    components:{

    },

    methods:{
        async fetch_orders(){
            try{
                var url = window.__runtime_configuration.apiEndpoint + '/orders/' + this.getEmail
                const response = await axios.get(url)
                
                var response_categories = JSON.parse(response.data.body)
                console.log(response_categories.categories)
                var categories = []
                // response_categories.forEach(function (category) {
                //   categories.push(category)
                // });
                // response_categories.forEach((category) => {
                //     categories.push(category.category)
                // });
                // this.categories = categories
            }catch(err){
                console.log(err)
            }
        },


        async await_categories(){
            await this.fetch_orders()
            // this.orders = this.getCategories
        },
    
    
    
    },
    computed: {
        ...mapGetters(["getEmail", "getIdToken"]),
    },
    created(){
      // this.fetchCategories()
      // this.categories = this.getCategories
// this.fetchProducts();
    },

    data(){

        return {
            orders: []
        }
    }
}


</script>