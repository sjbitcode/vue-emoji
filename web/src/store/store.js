import Vue from 'vue';
import Vuex from 'vuex';
import _ from 'lodash';

Vue.use(Vuex);

export const store = new Vuex.Store({
	state: {
		title: 'Emoji Index',
		message: ''
	},

	mutations: {
		updateMessage: (state, payload) => {
			state.message = payload;
		}
	},

	actions: {
		fetchMessage: context => {
			console.log('Message is ', context.state.message);
			if(! context.state.message) {
				console.log('Going to fetch message');
				Vue.http.get('http://localhost:8000/')
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateMessage', data.message);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
			else {
				console.log('Not fetching the message');
			}
		}
	}
})