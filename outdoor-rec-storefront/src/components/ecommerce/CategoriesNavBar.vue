<template>
  <div>
    <v-card flat > 
          <!-- height="400" flat> -->
    <v-navigation-drawer permanent>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            Categories
          </v-list-item-title>
          <v-list-item-subtitle>
            
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav >
        <v-list-item
          v-for="category in categories"
          :key="category"
          link
        >
          <!-- <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon> -->

          <v-list-item-content>
            <v-list-item-title>{{ category}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


      <!-- <v-navigation-drawer
        absolute >
        <v-list
          dense
          nav
          class="py-0">
              <v-list-item v-for="item in categories"
                :key="item"
                link >
              <v-list-item-content @click="navigate(item)">
                
                <v-list-item-title>{{ item }}</v-list-item-title>

          </v-list-item-content>
         </v-list-item>
        </v-list>
      </v-navigation-drawer> -->
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */

import router from '../../router'
import { mapGetters, mapActions } from "vuex";
import axios from 'axios';

export default {

    methods:{
        ...mapActions(["fetchCategories"]),
        
        async fetch_categories(){
            try{
                var url = window.__runtime_configuration.apiEndpoint + '/categories'
                const response = await axios.get(url)
                
                var response_categories = response.data.categories
                var categories = []
                // response_categories.forEach(function (category) {
                //   categories.push(category)
                // });
                response_categories.forEach((category) => {
                    categories.push(category.category)
                });
                this.categories = categories
            }catch(err){
                console.log(err)
            }
        },



        async await_categories(){
            await this.fetchCategories()
            this.categories = this.getCategories
            console.log('THE CATEGORIESW ARE')
            console.log(this.categories)
        },
        
        navigate(route){
            if(route != this.$route.path){
            router.push(route)
            }
        }
    },
    computed: {
        ...mapGetters(["getCategories"]),
    },

  created(){
    var categories = this.getCategories
    if(categories.length == 0){
        this.fetch_categories()    
    }

//   this.await_categories();
  },


  data () {
      return {
        categories : ''

      }
    },
  
}
</script>