<template>
    

</template>

<script>


import axios from 'axios';


export default {


   components:{

    },

    props:{

    },


    methods:{
        ...mapActions(["fetchProducts"]),

        async fetch_products(category){
            try{
                var url = window.__runtime_configuration.apiEndpoint + '/products/category/' + category 
                const response = await axios.get(url)
                var products = response.data.products
                console.log(products)
                this.products = products
            }catch(err){
                console.log(err)
            }
        },
    },
    computed: {
        ...mapGetters(["getProducts"]),
    },
    created(){

    },

    data () {
      return {
        products : []

      }
    },


}
</script>