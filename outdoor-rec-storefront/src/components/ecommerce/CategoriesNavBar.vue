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
          v-for="category in getCategories"
          :key="category.category"
          link
        >
          <!-- <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon> -->

          <v-list-item-content @click="navigate(category)" >
            <v-list-item-title>{{ category.category}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>


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
        ...mapActions(["setCategories"]),
        
        async fetch_categories(){
            try{
                //var url = window.__runtime_configuration.apiEndpoint + '/categories'
                var url ='https://qxt70tdiql.execute-api.us-west-2.amazonaws.com/Prod/categories'
                const response = await axios.get(url)            
                var response_categories = JSON.parse(response.data.body)
                this.setCategories(response_categories.categories)
            }catch(err){
                console.log(err)
            }
        },

        async await_categories(){
            await this.fetchCategories()
            this.categories = this.getCategories
        },
        
        navigate(category){
            router.push({ name: 'products', params: { category: category.category } })
            // if(route != this.$route.path){
            //     router.push({ name: 'transcription_detail', params: { fileID: fileID } })
            // }
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
        categories : []

      }
    },
  
}
</script>