import Vue from 'vue';
import Vuex from 'vuex';
import _ from 'lodash';

Vue.use(Vuex);

export const store = new Vuex.Store({
	state: {
		title: 'Emoji Index',
		message: '',
		homepageEmoji: []
	},

	mutations: {
		updateMessage: (state, payload) => {
			state.message = payload;
		},

		updateHomepageEmoji: (state, payload) => {
			state.homepageEmoji = payload;
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
		},

		fetchHomepageEmoji: context => {
			console.log('homepageEmoji is ' + context.state.homepageEmoji);
			if(_.isEmpty(context.state.homepageEmoji)) {
				console.log('Going to fetch homepageemoji');
				Vue.http.get('http://localhost:8000/homepage?flat=true')
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateHomepageEmoji', data.results);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
			else {
				console.log('Not fetching home page emojis');
			}
		}
	}
})