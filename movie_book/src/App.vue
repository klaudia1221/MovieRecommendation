<template>
  <div id="app">
    <!-- <div id="particles-js"></div> -->

    <div id="border">
      <div class="background">
        <div class="filter"></div>
      </div>
    </div>

    <div id="body">

      <div class="header">
        <h1>Movies recommendation <i class="fas fa-video"></i>
        </h1>

      </div>
      
      <div class="content">
        <movies/>
      </div>
    </div>
  </div>
</template>

<script>
import Movies from './components/Movies.vue'
import Card from './controls/card'
import Vue from 'vue';

Vue.component('card', Card);

export default {
  name: 'app',
  components: {
    Movies
  }
}
</script>

<style lang="scss">
@import url('./css/main.scss');


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
  overflow: hidden;
  // background:rgba(255,255,255,0.5);



}

#body {
  // margin: 20px;

  color: white;
  
  //  display: grid;
   width: 100%;
   height: 100%;

  // grid-template-columns: 1fr;
  // grid-template-rows: auto 1fr;  
  padding: 20px;

  .header {
    width: 100%;
    font-size: 16px; 
    font-size: 2vw;

    @media (max-width: 320px) {
     /* CSS that should be displayed if width is equal to or less than 800px goes here */
     font-size: 0.7rem;
    }
    
    @media (min-width: 800px) {
     /* CSS that should be displayed if width is equal to or less than 800px goes here */
     font-size: 24px;
    }
  }


  .content {
    // margin: 20px;
    overflow: hidden;
    width: 100%;
    height: 100%;
    max-height: 100%;
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
  background-image: url("~/img/movies.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  filter: blur(2px);
 

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
