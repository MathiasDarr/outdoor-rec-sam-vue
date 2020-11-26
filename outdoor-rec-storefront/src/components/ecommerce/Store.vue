<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <!-- <BaseNavBar v-bind:categories=cate /> -->
        <CategoriesNavBar /> 
      </v-flex>
      <v-flex md10>
          <!-- <v-card flat>
            <ProductList />
          </v-card> -->
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
/* eslint-disable */

// import BaseNavBar from '../BaseNavBar'
import { mapGetters, mapActions } from "vuex";
// import ProductList from './ProductList'

import CategoriesNavBar from './CategoriesNavBar'

export default {
    components:{
        CategoriesNavBar
        // BaseNavBar,
        // ProductList
    },

    methods:{
        ...mapActions(["fetchProducts", "fetchCategories"]),
    },
    computed: {
        ...mapGetters(["allProducts", "getCategories"]),
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