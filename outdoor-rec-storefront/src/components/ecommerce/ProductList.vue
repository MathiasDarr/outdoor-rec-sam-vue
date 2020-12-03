<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <!-- <BaseNavBar v-bind:categories=cate /> -->
        <CategoriesNavBar /> 
      </v-flex>
      
      
      
      <v-flex md9>
    <v-container fluid grid-list-md>
          <!-- xs = 600px full screen (12) -->
          <!-- md = 600px or more. half of the screen (6) -->
          <v-layout row wrap>
              <v-flex xs12 md4 v-for="item in products_page" v-bind:key=item.productName >
                    <ProductCard v-bind:productID="item.id" v-bind:productVendor="item.vendor" v-bind:productName="item.productName" v-bind:imageURL="item.image_url" v-bind:productPrice="item.price"/>
              </v-flex>
          </v-layout>
      </v-container>

      <!-- <template>
      <v-row>
        <v-col
            for="item in products_page"
            key="item.productName"
            class="d-flex child-flex"
            cols="4"
          >
          

          <template v-slot:placeholder>
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                >
                dfd 
                <ProductCard v-bind:productID="item.id" v-bind:productName="item.productName" v-bind:imageURL="item.image_url" v-bind:productPrice="item.price"/>
                </v-row>
              </template>
 
          </v-col>
        </v-row>
    </template> -->

      <!-- <v-flex xs2 md3  v-for="item in products_page" v-bind:key=item.id>
            <ProductCard v-bind:productID="item.id" v-bind:productName="item.productName" 
            v-bind:imageURL="item.image_url" v-bind:productPrice="item.price"/>
              <v-card >
                  <v-img :src="item.imageURL" height="200px" width="100"></v-img>
                  
              </v-card> -->
              
          <!-- </v-flex> -->
      

      <v-pagination
        v-model="page"
        :length="npages"
        @input="onPageChange"
        prev-icon="mdi-menu-left"
        next-icon="mdi-menu-right"
      ></v-pagination>
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

        onPageChange(){
          this.set_page()
        },

        set_page(){
          var end = (this.page)*30
          var start = (this.page-1)*30
          if(end > this.products.length){
            this.products_page = this.products.slice(start, this.products.length)
          }else{
            this.products_page = this.products.slice(start,end)
          }
        },


        async fetch_products(){
            try{
                var url = 'https://qxt70tdiql.execute-api.us-west-2.amazonaws.com/Prod' + '/products/category/' + this.category 
                const response = await axios.get(url)
                var products_body = JSON.parse(response.data.body)
                var category_products = {category:this.category, products:products_body.products}
                this.setCategoryProducts(category_products)
                this.products = this.getProductsCategoryMap[this.category]

                this.nproducts = this.products.length
                this.page = 1
                this.set_page()
                this.npages =  Math.ceil(this.nproducts/30)
                
            }catch(err){
                console.log(err)
            }
        },
    },
    computed: {
        ...mapGetters(["getProductsCategoryMap"]),
        getPage(n){
          
        }
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
        products : [],
        page:0,
        npages:0,
        products_page:[]

      }
    },



}
</script>