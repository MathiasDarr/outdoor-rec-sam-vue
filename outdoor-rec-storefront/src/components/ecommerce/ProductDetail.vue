<template>
  <v-container>
    <v-layout row>
      <v-flex md2>
        <CategoriesNavBar /> 
      </v-flex>
      <v-flex md10>
        <v-card flat>
          <v-card tile flat >
          <v-card-text> <h1>{{ vendor }} </h1> </v-card-text>
          <v-card-text> <h3>{{ productName }} </h3> </v-card-text>

          <div v-if="imageURL === ''">

          </div>
          <div v-else>
              <v-img :src="imageURL"  @click="productClick()" height="300" width="500"></v-img>    
          </div>
          
          

          <v-card-text>
            <h3> $ {{ price }} </h3>
          </v-card-text>
        </v-card>           
                  
        <v-btn rounded class="error mt4" @click="addToCart()" > Add to Cart </v-btn>
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

import CategoriesNavBar from './CategoriesNavBar'
import { mapActions } from "vuex";
import router from '../../router'


export default {
    components:{
      CategoriesNavBar
    },

    created(){
        this.vendor = this.$route.params.vendor
        this.productName = this.$route.params.productName
       
  
        this.await_product_detail()

        // console.log('The id is: ' + this.$route.params.id);
        // this.addDeleteItem({id:this.id,quantity: 1})
    },

    data () {
     return {
       quantity:1,
       price: 1.1,
       imageURL: ''
     }
  },
  methods:{
    ...mapActions(["addDeleteItem"]),
    addToCart(){
      var product = { productName: this.productName, vendor:this.vendor, quantity:this.quantity}
      this.addDeleteItem(this.id, this.quantity)
    },
    
    async await_product_detail(){
        await this.fetch_product_detail()
    },
    
    async fetch_product_detail(){
            try{
                var url = 'https://qxt70tdiql.execute-api.us-west-2.amazonaws.com/Prod/products/detail/' + this.vendor + '/' + this.productName 
                const response = await axios.get(url)
                var response_body = JSON.parse(response.data.body)
                console.log(response_body)

                var product = response_body.product
                this.imageURL = product.image_url
                this.price = product.price
            }catch(err){
                console.log(err)
            }
      },
  }


}
</script>