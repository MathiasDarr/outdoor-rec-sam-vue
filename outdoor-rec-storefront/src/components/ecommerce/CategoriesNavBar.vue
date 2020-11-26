<template>
  <div>
    <v-card  height="400" flat>
      <v-navigation-drawer
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
        {{ categories }}
    </v-card>
  </div>
</template>

<script>
/* eslint-disable */
// import router from '../../router'
import { mapGetters, mapActions } from "vuex";

export default {

    methods:{
        ...mapActions(["fetchCategories"]),
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
      this.fetchCategories()
      this.categories = this.getCategories
  },


  data () {
      return {


      }
    },
  
}
</script>