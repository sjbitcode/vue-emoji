import Vue from 'vue';
import Vuex from 'vuex';
import _ from 'lodash';

Vue.use(Vuex);

export const store = new Vuex.Store({
	state: {
		title: 'Emoji Index',
		
		api_status: '\ud83e\udd1e\ud83c\udffc',
		thumbsUp: '\ud83d\udc4d\ud83c\udffc',
		thumbsDown: '\ud83d\udc4e\ud83c\udffc',

		baseUrl: 'http://localhost:8000',

		homepageEmoji: [],
		homepageEndpoint: '/homepage?flat=true',

		categories: {},
		categoriesEndpoint: '/categories',

		statsEndpoint: '/stats',
		stats: {
			'date_requested': '',
			'Total Emojis': 0,
			'Total Keywords': 0,
			'Recently Added Emojis': 0,
			'Total Main Categories': 0,
			'Total Sub Categories': 0
		},

		emojiEndpoint: '/emoji',
		sampleRequest: {},
		sampleRequestQueryParams: '?q=smile&limit=2'
	},

	getters: {
		homepageUrl: state => {
			return state.baseUrl + state.homepageEndpoint;
		},

		categoriesUrl: state => {
			return state.baseUrl + state.categoriesEndpoint;
		},

		statsUrl: state => {
			return state.baseUrl + state.statsEndpoint;
		},

		sampleRequestUrl: state => {
			return state.baseUrl + state.emojiEndpoint + state.sampleRequestQueryParams;
		}
	},

	mutations: {
		updateMessage: (state, payload) => {
			if (payload === 'good') {
				state.api_status = state.thumbsUp;
			}
			else if (payload === 'bad') {
				state.api_status = state.thumbsDown;
			}
			console.log('Message SET TO ---> ' + state.message);
			console.log('API Status SET TO ---> ' + state.api_status);
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
			console.log('stats SET TO ---> ', state.stats);
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

				const url = context.state.baseUrl;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateMessage', 'good');
				})
				.catch(error => {
					context.commit('updateMessage', 'bad');
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

				const url = context.getters.homepageUrl;

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

				// const url = context.state.baseUrl + context.state.categoriesEndpoint;
				const url = context.getters.categoriesUrl;

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
			console.log('stats is ', context.state.stats);
			if(context.state.stats['Total Emojis'] === 0) {
				console.log('Going to fetch stats');

				// const url = context.state.baseUrl + context.state.statsEndpoint;
				const url = context.getters.statsUrl;

				Vue.http.get(url)
				.then(data => {
					//context.commit('updateStats', data.json())
					return data.json();
				})
				.then(data => {
					//debugger;
					console.log('stats DATA is ', data);
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

				const url = context.getters.sampleRequestUrl;
				// const url = context.state.baseUrl + context.state.sampleRequestQueryParams;

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