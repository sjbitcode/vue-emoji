import Vue from 'vue'
import App from './App.vue'
import Clipboard from 'v-clipboard'
import Tooltip from 'vue-directive-tooltip';
import "../node_modules/vue-directive-tooltip/css/index.css";


Vue.use(Clipboard);
Vue.use(Tooltip);

new Vue({
  el: '#app',
  render: h => h(App)
})
