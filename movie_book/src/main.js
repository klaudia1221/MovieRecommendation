import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'

Vue.config.productionTip = false


// var myMixin = {
//   created: function () {
//     this.hello()
//   },
//   methods: {
//     hello: function () {
//       console.log('hello from mixin!')
//     }
//   }
// }
// Vue.$go = function() {
// }

new Vue({
  // mixins: [myMixin],
  router,
  render: h => h(App),
}).$mount('#app')
