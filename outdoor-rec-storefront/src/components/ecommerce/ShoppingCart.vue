<template>
  <v-container>
    <v-layout>
      <v-flex md2>
        <BaseNavBar v-bind:items=items />
      </v-flex>
          
      <v-flex md10>
        <v-card flat>
          <v-card-title>
            Dakobed Shopping Cart
          </v-card-title>
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from "vuex";



      // </v-flex>

export default {

  components:{

  },


  created(){
      // let productIDs = Array.from( this.getCart.keys() );
      // let quantities = Array.from(this.getCart.values())
      // console.log("products " + productIDs )
      // console.log("quantities " + quantities )
      // const products = [] 
      //   // console.log(products)
      // for (var i = 0; i < [productIDs.length]; i++) {
      //   products.push({id:productIDs.indexOf(i), quantity:quantities.indexOf(i)})
      // }
      // products.forEach(data => console.log("product ID " + data.id + " and the quantities  " + data.quantity))

    },

    data () {
     return {

        items: [
          { title: 'Microservices Project', icon: 'mdi-view-dashboard', route:'/ecommerce' }, 
          { title: 'Ecommerce Store', icon: 'mdi-image', route:'/storefront' },
          { title: 'Shopping Cart', icon: 'mdi-image', route:'/cart' },
        ],

        products:[]
     
     }
  },
    computed:{
        ...mapGetters(["getCart"]),
    },
    methods:{
        ...mapActions(["changeProductCartCount"]),
    }
}

</script>
