<template>
    
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
                var url ='https://9lw0iaam5l.execute-api.us-west-2.amazonaws.com/Prod/orders'
                var body ={
                    
                }
                const response = await axios.post(url)            
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