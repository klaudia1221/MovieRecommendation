<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <movies/>
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
