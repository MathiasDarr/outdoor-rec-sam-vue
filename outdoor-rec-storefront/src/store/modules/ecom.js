/* eslint-disable */

import axios from 'axios';


const state = {
    products: [],
    cart: [],
    categories: []
};

const getters = {
  getProducts: state => state.products,
  getCategories: state => state.categories
};

const actions = {

  async fetchCategories({commit}){
    var url = window.__runtime_configuration.apiEndpoint + '/categories'
    axios.get(url).then((response) => {
      
      var response_categories = response.data.categories
      var categories = []
      
      // response_categories.forEach(function (category) {
      //   categories.push(category)
      // });

      response_categories.forEach((category) => {
        categories.push(category.subcategory)

    });


      console.log(categories)
      commit('setCategories', category)
    
    }, (error) => {
      console.log(error);
    });
  },



  async fetchProducts({commit}){
    axios.get('http://localhost:3000/products').then((response) => {
      commit('setProducts', response.data)
    }, (error) => {
      console.log(error);
    });
  },

  async addDeleteItem({commit}, product){
    console.log("The product looks like with quantity" + product.quantity)
    commit('addDeleteItem', product)
  } 


};

const mutations = {
    setCategories: (state, categories) => (state.categories = categories),
    setProducts: (state, products) => (state.products = products),
    addDeleteItem (state, product ) {

        if(state.cart.has(product.id)){
             state.cart.set(state.cart.get(product.id) + product.quantity)
        }else {
           state.cart.set(product.id, product.quantity)
        }
        // if(state.cart.get(id) == 0){
        //     state.cart.delete(id)
        // }
      },
};

export default {
  state,
  getters,
  actions,
  mutations
};
