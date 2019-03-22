import Vue from 'vue'
import VueRouter from 'vue-router'

import Movies from './components/Movies.vue'
import Books from './components/Books.vue'
import About from './components/About.vue'


Vue.use(VueRouter)

const routes = [
  { path: '/', component: Movies, name: 'home' },
  { path: '/movies', component: Movies, name: 'movies' },
  { path: '/books', component: Books, name: 'books' },
  { path: '/about', component: About, name: 'about' },
]

export default new VueRouter({
  mode: 'history',
  routes // short for `routes: routes`
})


