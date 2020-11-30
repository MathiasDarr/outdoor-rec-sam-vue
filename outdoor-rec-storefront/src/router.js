import Vue from 'vue'
import Router from 'vue-router'

import Login from './components/Login'
import Register from './components/Register'
import Confirm from './components/Confirm'

import Store from './components/ecommerce/Store'
import ShoppingCart from './components/ecommerce/ShoppingCart'

import ProductList from './components/ecommerce/ProductList'

import Profile from './components/profile/Profile'

import Orders from './components/profile/Orders'


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
      component: Orders

    }



    // {
    //   path: '/landing',
    //   component: Landing
    // },

    // {
    //   name: 'transcription',
    //   path: '/transcription/:id',
    //   component: Transcription

    // },

    // {
    //   path: '/transcriptions',
    //   component: TranscriptionList
    // },

    // {
    //   name:'transcription_detail',
    //   path: '/transcription_detail/:fileID/:title',
    //   component: TranscriptionDetail
    // },

    // {
    //   path: '/maestro',
    //   component: MaestroTranscriptions
    // },


    
    // {
    //   path:'/transcriber',
    //   component: Transcriber
    // },
    
    // {
    //   path:'/musiclanding',
    //   component: MusicProjectIntro
    // },

    // {
    //   path: '/transcriptions',
    //   component: TranscriptionList

    // },

    // {
    //   path:'/guitarset',
    //   component: GuitarSet
    // },

  ]
})
