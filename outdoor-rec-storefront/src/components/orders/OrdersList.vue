<template>
  <v-container>
      {{ getOrders.length }}


    <v-card flat class="pa-3" v-for="order in getOrders" :key="order.orderID" >
          <v-container dark>
            <v-layout row>
              <v-flex xs7 sm8 md9>
                <v-card-title>
                    {{order.order_status}}
                    <div>
                        <h4 class = "mb-0 text-left" > {{order.status}} </h4>
                    </div>
                </v-card-title>
              </v-flex>

            </v-layout>
        </v-container>
    </v-card> 
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
        ...mapActions(["setOrders"]),
        
        async fetch_orders(){
            try{
                var api_endpoint = 'https://9lw0iaam5l.execute-api.us-west-2.amazonaws.com/Prod'
                var url = api_endpoint + '/orders/' + this.getEmail
                const response = await axios.get(url, {
                headers: {
                        Authorization: this.getIdToken
                    }
                })
                
                var orders_response = JSON.parse(response.data.body)
                
                this.setOrders(orders_response.orders)
 
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
        ...mapGetters(["getEmail", "getIdToken", "getOrders"]),
    },
    created(){
        this.await_orders()

    },

    data(){

        return {
            orders: []
        }
    }
}


</script>