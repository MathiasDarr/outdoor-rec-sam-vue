<template>
  <div>
    
    <v-layout row wrap>
        <v-flex md6>
          <v-card tile flat @click="productClick()">
            <v-card-text @click="productClick()">
              <h1 style="font-weight:bold; color:black">{{ productVendor }} </h1>
                <h2><router-link tag="span" :to="'/tabs'"> {{productName}}</router-link></h2>
            </v-card-text>
            <v-img :src="imageURL"  @click="productClick()"></v-img>
          </v-card>
        </v-flex>
        <v-flex md6>
          <v-card tile flat >
            <v-card-text> $ {{ productPrice }}</v-card-text>
          </v-card>
        </v-flex>
      </v-layout> 

    <router-view></router-view>
  </div>
</template>
<script>

import router from '../../router'

export default {
    props:{
        productID:String,
        imageURL:String,
        productName: String,
        productPrice: Number,
        productVendor: String
    },
    methods:{
        productClick(){
          console.log(this.imageURL)
          router.push({ path: `/product/${this.productVendor}/${this.productName}`, params: { imageURL: this.imageURL } })
        }
    }
}
</script>
<style scoped>
li a {
    text-decoration: none;
}
</style>