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


          <v-img :src="imageURL"  @click="productClick()"></v-img>    
  
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
        // console.log(this.productName)
        console.log(this.imageURL)
// console.log('The id is: ' + this.$route.params.id);
        // this.addDeleteItem({id:this.id,quantity: 1})
    },

    data () {
     return {
       
       productName: "Atmos 65",
       price:"180.00",
       id: this.$route.params.id,
       quantity:1,
       
     }
  },
  methods:{
    ...mapActions(["addDeleteItem"]),

  }


}
</script>