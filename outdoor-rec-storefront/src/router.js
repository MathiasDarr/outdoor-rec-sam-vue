import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/Login'
import Register from './components/Register'
import Confirm from './components/Confirm'

import Store from './components/ecommerce/Store'
import ShoppingCart from './components/ecommerce/ShoppingCart'

import ProductList from './components/ecommerce/ProductList'
import ProductDetail from './components/ecommerce/ProductDetail'

import Profile from './components/profile/Profile'

import OrdersList from './components/orders/OrdersList'


Vue.use(Router)

export default new Router({
  mode:'history',
  base: process.env.BASE_URL,
  routes: [

    {
      path: '/',
      name: 'storefront',
      component: Store
    },
    {
      path:'/login',
      component: Login
    },

    {
      path:'/register',
      name:'register',
      component: Register
    },

    {
      path:'/confirm',
      name:'confirm',
      component: Confirm
    },
    {
      path:'/cart',
      component: ShoppingCart
    },
    {
      name: "products",
      path:"/products/:category",
      component: ProductList,
      props: true
    },

    {
      name: "profile",
      path:"/profile",
      component: Profile
    },

    {
      name:"orders",
      path: "/orders",
      component: OrdersList
    },
    { 
      path: '/product/:vendor/:productName',
      component: ProductDetail,
      props:true 
    },


  ]
})
