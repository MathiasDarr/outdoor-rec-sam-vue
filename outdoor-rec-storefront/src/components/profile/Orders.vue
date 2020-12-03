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
                var api_endpoint = 'https://9lw0iaam5l.execute-api.us-west-2.amazonaws.com/Prod'
                console.log(api_endpoint)
                var url = api_endpoint + '/orders/' + this.getEmail
                const response = await axios.get(url, {
                headers: {
                        Authorization: this.getIdToken
                    }
                })
                
                var response_orders = JSON.parse(response.data.body)
                console.log(response)
                var orders = []
 
            }catch(err){
                console.log(err)
            }
        },


        async await_orders(){
            await this.fetch_orders()
            // this.orders = this.getCategories
        },
    
    
    
    },
    computed: {
        ...mapGetters(["getEmail", "getIdToken"]),
    },
    created(){
        this.await_orders()
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