<template>
  <div id="app">
    <!-- <div id="particles-js"></div> -->

    <div id="border">
      <div class="background" :class="[background_class]" >
        <div class="filter"></div>
      </div>
    </div>



   <!-- <movies class="body"/> -->
   <router-view></router-view>
  </div>
</template>

<script>
import Movies from './components/Movies.vue'
import Card from './controls/card'
import Rating from './controls/rating'
import StarRating from './controls/star-rating'
import Vue from 'vue';
import VueRouter from 'vue-router'

Vue.use(VueRouter)

Vue.component('card', Card);
Vue.component('rating', Rating);
Vue.component('star-rating', StarRating);

export default {
  name: 'app',
  data() {
    return {
      background_class: 'home'
    }
  },
  components: {
    Movies
  },
  mounted() {
    this.background_class = this.$router.currentRoute.name;
  },
  watch:{
    $route (to, from){
      this.background_class = this.$router.currentRoute.name;
      // console.log('change');
        // this.show = false;
    }
  } 
}
</script>

<style lang="scss">
@import './css/main.scss';


#app {
  display: block;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  // margin-top: 60px;
  // overflow: hidden;
  // background:rgba(255,255,255,0.5);

 .body {
  //  margin: 5px;
   width: 100%;
   height: 100%;
    padding: 20px;

 overflow: hidden;

 }

}


#border {
  display: block;
  position: absolute;

  padding: 5px;
  width: 100%;
  height: 100%;;
  overflow: hidden;

  z-index: -100;

  

  .background {
  display: block;
  // position: absolute;
  
  width: 100%;
  height: 100%;
  overflow: hidden;
  margin: 0;
  // padding: 5px;
  // background-image: url("~/img/movies.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  // filter: blur(2px); 
    // -webkit-filter: grayscale(100%); /* Safari 6.0 - 9.0 */
  // filter: sepia(100%);
  // filter: grayscale(100%);

  &.home {
    background-image: url("~/img/movies.jpg");
  }

  &.movies {
    background-image: url("~/img/movies.jpg");
  }

  &.books {
    background-image: url("~/img/books.jpg");
  }

  
  &.about {
    background-image: url("~/img/about.jpg");
  }
 
 

 .filter {
   background: rgba(238, 193, 193, 0.45);

   mix-blend-mode: normal;
    display: block;
  
  width: 100%;
  height: 100%;
 }
}
}




</style>
