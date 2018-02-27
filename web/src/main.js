import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App.vue'
import Clipboard from 'v-clipboard'
import Tooltip from 'vue-directive-tooltip';
import "../node_modules/vue-directive-tooltip/css/index.css";
// import _ from 'lodash';

Vue.use(VueResource)
Vue.use(Clipboard);
Vue.use(Tooltip);
// Object.definePrototype(Vue.prototype, '_', { value: _ });

new Vue({
  el: '#app',
  render: h => h(App)
})
