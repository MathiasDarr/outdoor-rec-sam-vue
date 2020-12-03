<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <!-- <BaseNavBar v-bind:categories=cate /> -->
        <CategoriesNavBar /> 
      </v-flex>
      <v-flex md9>
        {{ products }}
          <!-- <v-card flat>
            <ProductList />
          </v-card> -->
      </v-flex>

    </v-layout>
  </v-container>
</template>


<!--
<template>
  <v-container fluid="">
    <v-layout row wrap>
      <v-card flat>

       <v-layout row>
        <v-flex xs3 md3 offset-sm1 v-for="item in getProducts" v-bind:key=item.id>
            <ProductCard v-bind:productID="item.id" v-bind:productName="item.productName" 
            v-bind:imageURL="item.imageURL" v-bind:productPrice="item.price"/>
              <v-card >
                  <v-img :src="item.imageURL" height="200px" width="100"></v-img> 
              </v-card>
          </v-flex>

       </v-layout>


      </v-card>
        
          <v-flex md6 offset-1>

          </v-flex>
          <v-flex md3 offset-1>

            <v-card  tile flat >
    
              <v-btn icon>
                <router-link to="/cart">
                <v-icon  >mdi-cart</v-icon>
                </router-link>
              </v-btn>
        
            </v-card>
          </v-flex> 
      </v-layout>
  </v-container>
</template>
-->


<script>
/* eslint-disable */




import { mapGetters, mapActions } from "vuex";
import ProductCard from './ProductCard'
import CategoriesNavBar from './CategoriesNavBar'
import axios from 'axios';


export default {
    components:{
        ProductCard,
        CategoriesNavBar
    },

    props:{

    },

    methods:{
        ...mapActions(["setCategoryProducts"]),

        async fetch_products(){
            try{
                var url = 'https://qxt70tdiql.execute-api.us-west-2.amazonaws.com/Prod' + '/products/category/' + this.category 
                const response = await axios.get(url)
                var products_body = JSON.parse(response.data.body)
                var category_products = {category:this.category, products:products_body.products}
                this.setCategoryProducts(category_products)
                this.products = this.getProductsCategoryMap[this.category]

            }catch(err){
                console.log(err)
            }
        },
    },
    computed: {
        ...mapGetters(["getProductsCategoryMap"]),
    },
    created(){
      

      this.category = this.$route.params.category
      console.log(this.category)
      this.fetch_products()
      


      // this.fetch_products('mens-boots')
      //   console.log("DFDFDF")
      // this.fetchProducts();
    },

    data () {
      return {
        products : []

      }
    },



}
</script>