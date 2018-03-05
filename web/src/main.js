import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App.vue'
import Clipboard from 'v-clipboard'
import Buefy from 'buefy'
import 'buefy/lib/buefy.css'


Vue.use(VueResource)
Vue.use(Clipboard);
Vue.use(Buefy, {
	defaultIconPack: 'fab'
});


// Filters
Vue.filter('format-code', function(value) {
	value = JSON.parse(value)
	value += '\ufe0f'
	return value
});


new Vue({
  el: '#app',
  render: h => h(App)
})
