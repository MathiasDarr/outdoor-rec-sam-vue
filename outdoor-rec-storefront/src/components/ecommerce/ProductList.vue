<template>
  <v-container>
    <v-layout>
      <v-flex md3>
        <!-- <BaseNavBar v-bind:categories=cate /> -->
        <CategoriesNavBar /> 
      </v-flex>
      
      
      
      <v-flex md9>
        <v-container fluid grid-list-md>
          <v-layout row wrap>
            <v-flex xs12 md4 v-for="item in products_page" v-bind:key=item.productName >
              
              <ProductCard v-bind:productID="item.id" v-bind:productVendor="item.vendor" v-bind:productName="item.productName"
               v-bind:imageURL="item.image_url" v-bind:productPrice="item.price"/>
            </v-flex>
          </v-layout>
        </v-container>

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
  
      this.fetch_products()
      
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