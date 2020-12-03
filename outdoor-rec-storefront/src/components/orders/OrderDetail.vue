<template>
    <v-container>

    </v-container>
</template>

<script>

export default {
        components:{

    },

    methods:{
        async fetch_orders_detail(){
            try{
                var api_endpoint = 'https://9lw0iaam5l.execute-api.us-west-2.amazonaws.com/Prod'
                console.log(api_endpoint)
                var url = api_endpoint + '/orders/' + this.getEmail
                const response = await axios.get(url, {
                headers: {
                        Authorization: this.getIdToken
                    }
                })
                
                var response_orders = JSON.parse(response.data.body)
                console.log(response)
                var orders = []
 
            }catch(err){
                console.log(err)
            }
        },


        async await_orders(){
            await this.fetch_orders()

        },
    
    
    
    },
    computed: {
        ...mapGetters(["getEmail", "getIdToken"]),
    },
    created(){
    },

    data(){

        return {
            
        }
    }


}
</script>