import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import App from './App.vue'
import Clipboard from 'v-clipboard'
import Buefy from 'buefy'
import Routes from './routes'
import VueHighlightJS from 'vue-highlight.js';
import 'buefy/lib/buefy.css'
import 'csshake/dist/csshake.min.css';
import 'highlight.js/styles/dracula.css';


Vue.use(VueResource);
Vue.use(VueRouter);
Vue.use(Clipboard);
Vue.use(Buefy, {
	defaultIconPack: 'fab'
});
Vue.use(VueHighlightJS);


const router = new VueRouter({
	routes: Routes,
	mode: 'history'
});

// Filters
Vue.filter('format-code', function(value) {
	value = JSON.parse(value)
	value += '\ufe0f'
	return value
});


new Vue({
  el: '#app',
  render: h => h(App),
  router: router
})
