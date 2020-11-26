<template>
  <div>
    <v-card  height="400" flat>
        {{ categories }}
      <!-- <v-navigation-drawer
        absolute >
        <v-list
          dense
          nav
          class="py-0">
            
              <v-list-item
                v-for="item in categories"
                :key="item.subcategory"
                link >
              <v-list-item-content @click="navigate(item.subcategory)">

                <v-list-item-title>{{ item.subcategory }}</v-list-item-title>

          </v-list-item-content>
         </v-list-item>
        </v-list>
      </v-navigation-drawer>
        {{ categories }} -->
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
                    categories.push(category.subcategory)
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
    this.fetch_categories()
//   this.await_categories();
  },


  data () {
      return {
        categories : ''

      }
    },
  
}
</script>