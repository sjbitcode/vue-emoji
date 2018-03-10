import Vue from 'vue';
import Vuex from 'vuex';
import _ from 'lodash';

Vue.use(Vuex);

export const store = new Vuex.Store({
	state: {
		title: 'Emoji Index',
		message: '',

		baseUrl: 'http://localhost:8000',

		homepageEmoji: [],
		homepageEndpoint: '/homepage?flat=true',

		categories: {},
		categoriesEndpoint: '/categories',

		stats: {},
		statsEndpoint: '/stats',

		sampleRequest: {},
		sampleRequestEndpoint: '/emoji?q=smile&limit=2'
	},

	getters: {
		categoriesUrl: state => {
			return state.baseUrl + state.categoriesEndpoint;
		},

		statsUrl: state => {
			return state.baseUrl + state.statsEndpoint;
		},

		sampleRequestUrl: state => {
			return state.baseUrl + state.sampleRequestEndpoint;
		}
	},

	mutations: {
		updateMessage: (state, payload) => {
			state.message = payload;
			console.log('Message SET TO ---> ' + state.message);
		},

		updateHomepageEmoji: (state, payload) => {
			state.homepageEmoji = payload;
			console.log('homepageEmoji SET TO ---> ' + state.homepageEmoji);
		},

		updateCategories: (state, payload) => {
			state.categories = payload;
			console.log('categories SET TO ---> ' + state.categories);
		},

		updateStats: (state, payload) => {
			state.stats = payload;
			console.log('stats SET TO ---> ' + state.stats);
		},

		updateSampleEmojiRequest: (state, payload) => {
			state.sampleRequest = payload;
			console.log('sampleRequest SET TO ---> ' + state.sampleRequest);
		}
	},

	actions: {
		fetchMessage: context => {
			console.log('Message is ', context.state.message);
			if(! context.state.message) {
				console.log('Going to fetch message');
				Vue.http.get(context.state.baseUrl)
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

				url = context.state.baseUrl + context.state.homepageEndpoint;

				Vue.http.get(url)
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
		},

		fetchCategories: context => {
			console.log('categories is ' + context.state.categories);
			if(_.isEmpty(context.state.categories)) {
				console.log('Going to fetch categories');

				url = context.state.baseUrl + context.state.categoriesEndpoint;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateCategories', data.results);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
			else {
				console.log('Not fetching categories');
			}
		},

		fetchStats: context => {
			console.log('stats is ' + context.state.stats);
			if(_.isEmpty(context.state.stats)) {
				console.log('Going to fetch stats');

				url = context.state.baseUrl + context.state.statsEndpoint;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateStats', data);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
			else {
				console.log('Not fetching stats');
			}
		},

		fetchSampleEmojiRequest: context => {
			console.log('sample request is ' + context.state.sampleRequest);
			if(_.isEmpty(context.state.sampleRequest)) {
				console.log('Going to fetch sample request');

				url = context.state.baseUrl + context.state.sampleRequestEndpoint;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateSampleEmojiRequest', data);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
			else {
				console.log('Not fetching stats');
			}
		}
	}
})